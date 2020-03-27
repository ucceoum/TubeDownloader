# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tube_ui_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(550, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(550, 700))
        MainWindow.setMaximumSize(QtCore.QSize(550, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QtCore.QRect(-1, 25, 550, 500))
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QtCore.QRect(-1, -1, 52, 25))
        self.prevButton.setObjectName("prevButton")
        self.homeButton = QtWidgets.QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QtCore.QRect(49, -1, 52, 25))
        self.homeButton.setObjectName("homeButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(99, -1, 52, 25))
        self.nextButton.setObjectName("nextButton")
        self.urlEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.urlEdit.setGeometry(QtCore.QRect(150, 0, 250, 23))
        self.urlEdit.setObjectName("urlEdit")
        self.goButton = QtWidgets.QPushButton(self.centralwidget)
        self.goButton.setGeometry(QtCore.QRect(399, -1, 52, 25))
        self.goButton.setObjectName("goButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 525, 200, 22))
        self.comboBox.setObjectName("comboBox")
        self.pathEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pathEdit.setGeometry(QtCore.QRect(200, 525, 270, 22))
        self.pathEdit.setReadOnly(True)
        self.pathEdit.setObjectName("pathEdit")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(469, 524, 32, 24))
        self.toolButton.setObjectName("toolButton")
        self.downButton = QtWidgets.QPushButton(self.centralwidget)
        self.downButton.setGeometry(QtCore.QRect(449, -1, 52, 25))
        self.downButton.setObjectName("downButton")
        self.downAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.downAllButton.setGeometry(QtCore.QRect(499, -1, 52, 25))
        self.downAllButton.setObjectName("downAllButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 546, 551, 134))
        self.listWidget.setDragEnabled(True)
        self.listWidget.setObjectName("listWidget")
        self.clrButton = QtWidgets.QPushButton(self.centralwidget)
        self.clrButton.setGeometry(QtCore.QRect(499, 524, 52, 24))
        self.clrButton.setObjectName("clrButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tube Downloader"))
        self.prevButton.setText(_translate("MainWindow", "←"))
        self.homeButton.setText(_translate("MainWindow", "HOME"))
        self.nextButton.setText(_translate("MainWindow", "→"))
        self.goButton.setText(_translate("MainWindow", "GO"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.downButton.setText(_translate("MainWindow", "↓"))
        self.clrButton.setText(_translate("MainWindow", "clear"))
        self.downAllButton.setText(_translate("MainWindow", "↓+"))

from PyQt5 import QtWebEngineWidgets

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
