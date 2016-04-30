# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(576, 152)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(54, 24))
        self.label.setMaximumSize(QtCore.QSize(54, 24))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.pdflatex_field = QtGui.QTextBrowser(self.centralwidget)
        self.pdflatex_field.setMinimumSize(QtCore.QSize(0, 26))
        self.pdflatex_field.setMaximumSize(QtCore.QSize(16777215, 26))
        self.pdflatex_field.setObjectName(_fromUtf8("pdflatex_field"))
        self.horizontalLayout_2.addWidget(self.pdflatex_field)
        self.select_pdflatex_button = QtGui.QPushButton(self.centralwidget)
        self.select_pdflatex_button.setMinimumSize(QtCore.QSize(20, 24))
        self.select_pdflatex_button.setMaximumSize(QtCore.QSize(20, 24))
        self.select_pdflatex_button.setObjectName(_fromUtf8("select_pdflatex_button"))
        self.horizontalLayout_2.addWidget(self.select_pdflatex_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(54, 24))
        self.label_2.setMaximumSize(QtCore.QSize(54, 24))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.input_file_field = QtGui.QTextBrowser(self.centralwidget)
        self.input_file_field.setMinimumSize(QtCore.QSize(0, 26))
        self.input_file_field.setMaximumSize(QtCore.QSize(16777215, 26))
        self.input_file_field.setObjectName(_fromUtf8("input_file_field"))
        self.horizontalLayout_3.addWidget(self.input_file_field)
        self.select_input_button = QtGui.QPushButton(self.centralwidget)
        self.select_input_button.setMinimumSize(QtCore.QSize(20, 24))
        self.select_input_button.setMaximumSize(QtCore.QSize(20, 24))
        self.select_input_button.setObjectName(_fromUtf8("select_input_button"))
        self.horizontalLayout_3.addWidget(self.select_input_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.run_button = QtGui.QPushButton(self.centralwidget)
        self.run_button.setMinimumSize(QtCore.QSize(0, 24))
        self.run_button.setMaximumSize(QtCore.QSize(20000, 24))
        self.run_button.setObjectName(_fromUtf8("run_button"))
        self.horizontalLayout.addWidget(self.run_button)
        self.about_button = QtGui.QPushButton(self.centralwidget)
        self.about_button.setMaximumSize(QtCore.QSize(50, 24))
        self.about_button.setObjectName(_fromUtf8("about_button"))
        self.horizontalLayout.addWidget(self.about_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ODE Checker v.15a16", None))
        self.label.setText(_translate("MainWindow", "pdflatex", None))
        self.select_pdflatex_button.setText(_translate("MainWindow", "S", None))
        self.label_2.setText(_translate("MainWindow", "Input file", None))
        self.select_input_button.setText(_translate("MainWindow", "S", None))
        self.run_button.setText(_translate("MainWindow", "Run", None))
        self.about_button.setText(_translate("MainWindow", "About", None))

