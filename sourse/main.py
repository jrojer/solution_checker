# Author: Rusanov jrojer Aleksei
# main.py; 
# 2016-04-10 16:51; 

import sys
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
        QtCore.QObject.connect(self.ui.select_input_button,QtCore.SIGNAL("clicked()"),    self.SelectInput )
        QtCore.QObject.connect(self.ui.select_pdflatex_button,QtCore.SIGNAL("clicked()"),    self.SelectPdflatex )

        self.input_file_path    = ''
        self.pdflatex_file_path = ''
        self.fo_tex = 0
        self.tex_file_path = ''
        self.tex_filename = 'results.tex'


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

    def isBadFile(self,name): #check extension
        ending = name[len(name)-4:]
        if ending != '.txt' and ending != '.tex':
            return True
        return False

    def SelectInput(self):

        fd = QtGui.QFileDialog(self)

        self.input_file_path = fd.getOpenFileName()

        if self.input_file_path == '' : return

        if self.isBadFile(self.input_file_path):
            self.ui.input_file_field.setText(RedText('> Error: Unsupported file format'))
            self.input_file_path = ''
            return

        self.ui.input_file_field.setText(self.input_file_path)

    def isNotPdflatex(self,name):
        ending = name[len(name)-12:]
        if ending != 'pdflatex.exe' :
            return True
        return False

    def SelectPdflatex(self):

        fd = QtGui.QFileDialog(self)

        self.pdflatex_file_path = fd.getOpenFileName()

        if self.pdflatex_file_path == '' : return

        if self.isNotPdflatex(self.pdflatex_file_path):
            self.ui.pdflatex_field.setText(RedText('> Error: pdflatex.exe expected'))
            self.pdflatex_file_path = ''
            return

        self.ui.pdflatex_field.setText(self.pdflatex_file_path)

    def Print(self,text):
        print (text,file=self.fo_tex)
    def PPrint(self,expr):
        print ('\n$$\n',sympy.latex(expr),'\n$$\n',file=self.fo_tex)
        
    def InitiateTexFile(self):
        from pathlib import Path
        try:
            cur_dir       = Path('.')
            self.tex_file_path = str(cur_dir/self.tex_filename)
            self.tex_file_path = str(cur_dir/self.tex_filename)
            self.fo_tex   = open(self.tex_file_path,'w')
        except OSError:
            self.ui.input_file_field.setText(Redtext('.tex file cannot be created'))
            return False
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
        return True

    def RunPdflatexAndOpenPdf(self):
        import subprocess
        print ('> Starting pdflatex.exe')
        args = [self.pdflatex_file_path,
                '-interaction=batchmode',
                '-halt-on-error',
                '-no-shell-escape',
                self.tex_file_path
        ]
        tex_process = subprocess.call(args)
        print ('> pdflatex.exe exited')
        pdf_filename = self.tex_filename.replace('.tex','.pdf')
        import os
        os.system("start "+pdf_filename )

    def FilesArePresent(self):
        if self.isNotPdflatex(self.pdflatex_file_path):
            self.ui.pdflatex_field.setText(RedText('select file'))
            return False
        if self.isBadFile(self.input_file_path):
            self.ui.input_file_field.setText(RedText('select file'))
            return False
        return True
    def CheckODEs(self,fo):
        ''' read text file fo, solve ODEs, print results, close file '''
        funvar = FindFuncAndVar(fo)
        print ('> function and variable has been determined')
        if  (funvar[0] == '' or funvar[1] == '') :
            self.ui.input_file_field.setText(RedText('Error: Function or Variable is not specified'))
            return

        # reset fo
        fo.close()
        fo = open(self.input_file_path,'r')
        #
        print('> Parsing input file')
        for i,data in enumerate(ParseTex(fo)):

            eqs  =  LatexToSympy(data+funvar)
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
        
    def ShowProcessingMessage(self):
        
        
        self.proc_mes = QtGui.QWidget()
        ui = Ui_Form()
        ui.setupUi(self.proc_mes)
        self.proc_mes.show()
    #
    def HideProcessingMessage(self):
        self.proc_mes.hide()
    def Run(self):
	
        #self.ShowProcessingMessage()
		
        print ( '> Running')
         
        if not self.FilesArePresent(): return
        
        # open input file
        try:
            fo = open(self.input_file_path,'r')
        except (FileNotFoundError, NameError ) as e:
            self.ui.input_file_field.setText(RedText('cannot open file'))
            return
        #
        
        # initiate tex file	
        ret_code = self.InitiateTexFile()
        if ret_code == False:
            self.ui.input_file_field.setText(RedText('cannot create TeX file'))
            self.ui.pdflatex_field.setText(RedText('cannot create TeX file'))
        #
        '''
        # Print
        self.Print('File:')
        self.Print(self.input_file_path)
        self.Print('')
        #
        '''
		
        self.CheckODEs(fo) # fo will be closed there
       
        
        self.Print('\end{document}')
        self.fo_tex.close()
        
        print ('> Parsing finished')
        #self.HideProcessingMessage()
        self.RunPdflatexAndOpenPdf()




if __name__=='__main__':

    app = QtGui.QApplication(sys.argv)
    myapp = Start()
    myapp.show()
    sys.exit(app.exec_())
