# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DownloaderUI1.ui'
#
# Created: Sat Oct 18 17:20:31 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_DownloaderUI(object):
    def setupUi(self, DownloaderUI):
        DownloaderUI.setObjectName(_fromUtf8("DownloaderUI"))
        DownloaderUI.resize(499, 300)
        self.label = QtGui.QLabel(DownloaderUI)
        self.label.setGeometry(QtCore.QRect(10, 10, 58, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.E_resourceURL = QtGui.QLineEdit(DownloaderUI)
        self.E_resourceURL.setGeometry(QtCore.QRect(80, 10, 411, 25))
        self.E_resourceURL.setObjectName(_fromUtf8("E_resourceURL"))
        self.E_verifyCode = QtGui.QLineEdit(DownloaderUI)
        self.E_verifyCode.setGeometry(QtCore.QRect(80, 40, 81, 25))
        self.E_verifyCode.setObjectName(_fromUtf8("E_verifyCode"))
        self.label_2 = QtGui.QLabel(DownloaderUI)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 58, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.B_getResource = QtGui.QPushButton(DownloaderUI)
        self.B_getResource.setGeometry(QtCore.QRect(400, 40, 87, 27))
        self.B_getResource.setObjectName(_fromUtf8("B_getResource"))
        self.E_status = QtGui.QTextEdit(DownloaderUI)
        self.E_status.setGeometry(QtCore.QRect(10, 80, 481, 201))
        self.E_status.setObjectName(_fromUtf8("E_status"))
        self.L_photo = QtGui.QLabel(DownloaderUI)
        self.L_photo.setGeometry(QtCore.QRect(170, 40, 111, 31))
        self.L_photo.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.L_photo.setFrameShape(QtGui.QFrame.WinPanel)
        self.L_photo.setFrameShadow(QtGui.QFrame.Sunken)
        self.L_photo.setObjectName(_fromUtf8("L_photo"))
        self.B_changePhoto = QtGui.QPushButton(DownloaderUI)
        self.B_changePhoto.setGeometry(QtCore.QRect(280, 40, 51, 27))
        self.B_changePhoto.setFlat(True)
        self.B_changePhoto.setObjectName(_fromUtf8("B_changePhoto"))

        self.retranslateUi(DownloaderUI)
        QtCore.QMetaObject.connectSlotsByName(DownloaderUI)

    def retranslateUi(self, DownloaderUI):
        DownloaderUI.setWindowTitle(_translate("DownloaderUI", "CSDN Downloader", None))
        self.label.setText(_translate("DownloaderUI", "资源地址：", None))
        self.label_2.setText(_translate("DownloaderUI", "验证码：", None))
        self.B_getResource.setText(_translate("DownloaderUI", "获取资源", None))
        self.L_photo.setText(_translate("DownloaderUI", "图片(点换一张获取)", None))
        self.B_changePhoto.setText(_translate("DownloaderUI", "换一张", None))

