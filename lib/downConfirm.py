# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, QRect, Qt, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QLabel, QPushButton
class DownConfirm(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 90)
        Dialog.setStyleSheet("background-color:rgb(255, 255, 255)")
        Dialog.setMinimumSize(QSize(200, 90))
        Dialog.setMaximumSize(QSize(200, 90))
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(10, 10, 180, 30))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.yesButton = QPushButton(Dialog)
        self.yesButton.setGeometry(QRect(40, 50, 50, 25))
        self.yesButton.setObjectName("yesButton")
        self.noButton = QPushButton(Dialog)
        self.noButton.setGeometry(QRect(110, 50, 50, 25))
        self.noButton.setObjectName("noButton")
        self.confirmed = False
        self.yesButton.clicked.connect(lambda:self.checking(True,Dialog))
        self.noButton.clicked.connect(lambda:self.checking(False,Dialog))
        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def checking(self, yes, dialog) :
        self.confirmed = yes
        dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "다운로드 확인"))
        self.label_2.setText(_translate("Dialog", "재생목록의 동영상을 모두 \n다운로드 하시겠습니까?"))
        self.yesButton.setText(_translate("Dialog", "네"))
        self.noButton.setText(_translate("Dialog", "아니오"))
