# Author: Rusanov jrojer Aleksei
# main.py; 
# 2016-04-10 16:51; 

#apr 24
## 17:37 pdflatex subprocess tex file error check testing
## 20:34 . Added input file verification, 
###        diffrent output filenames support,
###        log files deletion, changed function names
#apr 25
## introduced working directory
## 12:18 builded Realese

import sys
import subprocess
from pathlib import Path, PureWindowsPath
from PyQt4 import QtCore, QtGui 
from UI_MainWindow import *
from UI_AboutWidget import *
from UI_ProcessingMessage import *
# main activity
import sympy
#
# my modules
from ParseTex import *
from LatexToSympy import *
from Checker import *
from ColorText import *
#

class Start(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.run_button,QtCore.SIGNAL("clicked()"),    self.Run )
        QtCore.QObject.connect(self.ui.about_button,QtCore.SIGNAL("clicked()"),    self.About )
        QtCore.QObject.connect(self.ui.select_input_button,QtCore.SIGNAL("clicked()"),    self.SelectInputFile )
        QtCore.QObject.connect(self.ui.select_pdflatex_button,QtCore.SIGNAL("clicked()"),    self.SelectPdflatexFile )

        self.input_file_path    = ''
        self.pdflatex_file_path = ''
        self.fo_tex = 0
        self.tex_file_path = ''
        self.tex_filename = ''
        self.working_dir = ''


    def AboutClose(self):
        self.about_widget.hide()

    def About(self):
        # A help window popups
        self.about_widget = QtGui.QWidget()  # create widget
        self.about = Ui_About() # get designer's code
        self.about.setupUi(self.about_widget) # apply designer's code
        QtCore.QObject.connect( self.about.OK_button,QtCore.SIGNAL("clicked()"),   self.AboutClose )
        self.about_widget.show()
    #

    def isNot_TeX_File(self,name): #check extension
        ending = name[-4:]
        if ending != '.tex':
            return True
        return False

    def SelectInputFile(self):

        fd = QtGui.QFileDialog(self)

        self.input_file_path = fd.getOpenFileName()

        if self.input_file_path == '' : return

        if self.isNot_TeX_File(self.input_file_path):
            self.ui.input_file_field.setText(RedText('> Error: Unsupported file format'))
            self.input_file_path = ''
            return

        self.ui.input_file_field.setText(self.input_file_path)
        
        print('> got input file path:',self.input_file_path)
        
        
        
        self.tex_filename = PureWindowsPath(self.input_file_path).name # Potential Error
        self.tex_filename = self.tex_filename[:-4]+'_results.tex'
        
        self.working_dir = str( PureWindowsPath(self.input_file_path).parents[0] )
        print('> working dir set to :', self.working_dir)
        print('> tex file name set to :', self.tex_filename)
        
        
    def isNotPdflatexFile(self,name):
        ending = name[len(name)-12:]
        if ending != 'pdflatex.exe' :
            return True
        return False

    def SelectPdflatexFile(self):

        fd = QtGui.QFileDialog(self)

        self.pdflatex_file_path = fd.getOpenFileName()
        
        print('> selected file:', self.pdflatex_file_path)
        

        if self.pdflatex_file_path == '' : return

        if self.isNotPdflatexFile(self.pdflatex_file_path):
            self.ui.pdflatex_field.setText(RedText('> Error: pdflatex.exe expected'))
            self.pdflatex_file_path = ''
            return

        self.ui.pdflatex_field.setText(self.pdflatex_file_path)

    def Print(self,text):
        print (text,file=self.fo_tex)
    def PPrint(self,expr):
        print ('\n$$\n',sympy.latex(expr),'\n$$\n',file=self.fo_tex)
        
    def InitiateTexFile(self):
                
        try:
            #cur_dir       = Path('.')
            cur_dir = Path(self.working_dir)
            #print('> current directory is set to: ',cur_dir)
            self.tex_file_path = str(cur_dir/self.tex_filename)
            self.fo_tex   = open(self.tex_file_path,'w') #TODO close ??
        except OSError:
            self.ui.input_file_field.setText(Redtext('.tex file cannot be created'))
            return True
        initial_string = '''
        
        \documentclass{article}
        \\usepackage[utf8]{inputenc}
        \\usepackage{amsthm}
        \\usepackage{amsmath}

        \\begin{document}

        '''
        #        \\usepackage[russian]{babel}
        self.Print(initial_string)
        print('> TeX file has been created')
        return False

    def RunPdflatexAndOpenPdf(self):
                
        print ('> Starting pdflatex.exe')
        args = [ self.pdflatex_file_path,
                '-interaction=batchmode',
                '-halt-on-error',
                '-no-shell-escape',
                self.tex_file_path
        ]
        tex_process = subprocess.call(args,cwd=self.working_dir)
        
        print('> pdflatex process return code : ', tex_process)
        
        (Path(self.working_dir)/(self.tex_filename[:-4]+'.log')).unlink()
        (Path(self.working_dir)/(self.tex_filename[:-4]+'.aux')).unlink()
        
        print ('> .aux and .log files deleted')
        
        print('> Openning pdf file...')
        pdf_filename = str ( Path(self.working_dir)/(self.tex_filename.replace('.tex','.pdf')) )
        import os
        os.system("start "+pdf_filename )

    def FilesArePresent(self):
        if self.isNotPdflatexFile(self.pdflatex_file_path):
            self.ui.pdflatex_field.setText(RedText('select file'))
            return False
        if self.isNot_TeX_File(self.input_file_path):
            self.ui.input_file_field.setText(RedText('select file'))
            return False
        return True
    def CheckODEs(self,fo):
        ''' read text file fo, solve ODEs, print results, close file '''
        funvar = FindFuncAndVar(fo)
        
        if  (funvar[0] == '' or funvar[1] == '') :
            self.ui.input_file_field.setText(RedText('ERROR: Function or Variable is not specified'))
            print('> ERROR: Function or Variable is not specified')
            return True
            
        print ('> function and variable defined')

        # reset fo
        fo.close()
        fo = open(self.input_file_path,'r')
        #
        print('> input file reopened')
        print('> Parsing input file ...')
        for i,data in enumerate(ParseTex(fo)):

            print('>> iteration :',i )
            print('>> data :',data)
            eqs  =  LatexToSympy(data+funvar)
            print('>> Checking solution ...')
            res  =  Check(eqs[0],eqs[1])

            self.Print('ODE number: '+str(i+1))
            self.PPrint(eqs[0])
            if res[0] == False :
                self.Print  ('Given solution:') 
                self.PPrint (eqs[1])
                self.Print  (' is INCORRECT') # RED letters
                self.Print  ('')
                self.Print  ('The correct one is:') 
                self.PPrint (res[1]) 
            else:
                self.Print('Solution:')
                self.PPrint(eqs[1])
                self.Print ('CORRECT') # GREEN letters
                self.Print ('')
            
        fo.close()
        return False
    '''        
    def ShowProcessingMessage(self):
        
        
        self.proc_mes = QtGui.QWidget()
        ui = Ui_Form()
        ui.setupUi(self.proc_mes)
        self.proc_mes.show()
    #
    def HideProcessingMessage(self):
        self.proc_mes.hide()
    '''        
    def VerifyInputFile(self):
      
        print('> Verifying input file...')
        args = [self.pdflatex_file_path,
        '-interaction=batchmode',
        '-halt-on-error',
        '-no-shell-escape',
        '-draftmode',
#        '-quiet',
        self.input_file_path
        ]

        tex_process = subprocess.call(args,cwd=self.working_dir)
        
        print('> pdflatex process return code : ', tex_process)
        
        Path(self.input_file_path[:-4]+'.aux').unlink()

        if tex_process != 0 :
            return True # error occured
        else:    
            Path(self.input_file_path[:-4]+'.log').unlink()
            
        return False # no error
        
    def Run(self):
	
        #self.ShowProcessingMessage()
		
        print ( '> RUNNING ...')
         
        if not self.FilesArePresent(): 
            print('> ERROR : select files')
            return
        
        
        error_occured = self.VerifyInputFile()
        if error_occured :
            print ('> ERROR: cannot compile the input file')
            self.ui.input_file_field.setText(RedText('ERROR: See .log file for details'))
            #TODO
            # ErrorMessage # look at log file
            return
            
            
        # open input file
        try:
            fo = open(self.input_file_path,'r')
        except (FileNotFoundError, NameError ) as e:
            self.ui.input_file_field.setText(RedText('cannot open file'))
            print('> ERROR: cannot open file')
            return
        #
        
        
        # initiate tex file	
        error_occured = self.InitiateTexFile()
        if error_occured :
            self.ui.input_file_field.setText(RedText('cannot create TeX file'))
            self.ui.pdflatex_field.setText(RedText('cannot create TeX file'))
            print('> ERROR: cannot create TeX file')
        #
       		
        error_occured = self.CheckODEs(fo) # fo will be closed there
        if error_occured :
            print ('> ODE checker ERROR')
            #TODO
            # ErrorMessage # look at log file
            return
        
        self.Print('\end{document}')
        self.fo_tex.close()
        
        print ('> Parsing finished')
        #self.HideProcessingMessage()
        self.RunPdflatexAndOpenPdf()




if __name__=='__main__':
    print('> Launching GUI ...')
    app = QtGui.QApplication(sys.argv)
    myapp = Start()
    myapp.show()
    sys.exit(app.exec_())
