# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downconfirm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class DownConfirm(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 90)
        Dialog.setStyleSheet("background-color:rgb(255, 255, 255)")
        Dialog.setMinimumSize(QtCore.QSize(200, 90))
        Dialog.setMaximumSize(QtCore.QSize(200, 90))
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 180, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.yesButton = QtWidgets.QPushButton(Dialog)
        self.yesButton.setGeometry(QtCore.QRect(40, 50, 50, 25))
        self.yesButton.setObjectName("yesButton")
        self.noButton = QtWidgets.QPushButton(Dialog)
        self.noButton.setGeometry(QtCore.QRect(110, 50, 50, 25))
        self.noButton.setObjectName("noButton")
        self.confirmed = False
        self.yesButton.clicked.connect(lambda:self.checking(True,Dialog))
        self.noButton.clicked.connect(lambda:self.checking(False,Dialog))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def checking(self, yes, dialog) :
        self.confirmed = yes
        dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "다운로드 확인"))
        self.label_2.setText(_translate("Dialog", "재생목록의 동영상을 모두 \n다운로드 하시겠습니까?"))
        self.yesButton.setText(_translate("Dialog", "네"))
        self.noButton.setText(_translate("Dialog", "아니오"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     dc = DownConfirm()
#     dc.setupUi(Dialog)
#     Dialog.exec_()
#     sys.exit(app.exec_())
