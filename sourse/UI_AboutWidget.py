# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
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

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(427, 160)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        About.setMinimumSize(QtCore.QSize(427, 160))
        About.setMaximumSize(QtCore.QSize(427, 160))
        self.label = QtGui.QLabel(About)
        self.label.setGeometry(QtCore.QRect(20, 20, 401, 101))
        self.label.setObjectName(_fromUtf8("label"))
        self.OK_button = QtGui.QPushButton(About)
        self.OK_button.setGeometry(QtCore.QRect(320, 130, 83, 24))
        self.OK_button.setObjectName(_fromUtf8("OK_button"))

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_translate("About", "About", None))
        self.label.setText(_translate("About", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">Author:</span><span style=\" font-weight:600; font-style:italic;\"> Rusanov Aleksei</span></p><p><span style=\" font-weight:600;\">aleksei.s.rusanov@gmail.com</span></p><p><span style=\" font-weight:600; font-style:italic;\">Herzen State University</span></p><p><span style=\" font-weight:600; font-style:italic;\">The application checks the correctness of solutions of ODEs</span></p></body></html>", None))
        self.OK_button.setText(_translate("About", "OK", None))

