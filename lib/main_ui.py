from PyQt5.QtCore import Qt, QSize, QRect, QUrl, QMetaObject, QCoreApplication
from PyQt5.QtGui import QIcon, QPixmap, QIcon
from PyQt5.QtWidgets import QSizePolicy, QWidget, QPushButton, QLineEdit, QComboBox, QToolButton, QStatusBar, QListWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(550, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(550, 700))
        MainWindow.setMaximumSize(QSize(550, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.webEngineView = QWebEngineView(self.centralwidget)
        self.webEngineView.setGeometry(QRect(-1, 25, 550, 500))
        self.webEngineView.setUrl(QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.prevButton = QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QRect(-1, -1, 53, 25))
        self.prevButton.setObjectName("prevButton")
        self.homeButton = QPushButton(self.centralwidget)
        self.homeButton.setGeometry(QRect(49, -1, 53, 25))
        self.homeButton.setObjectName("homeButton")
        self.nextButton = QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QRect(99, -1, 53, 25))
        self.nextButton.setObjectName("nextButton")
        self.urlEdit = QLineEdit(self.centralwidget)
        self.urlEdit.setGeometry(QRect(150, 0, 251, 23))
        self.urlEdit.setObjectName("urlEdit")
        self.goButton = QPushButton(self.centralwidget)
        self.goButton.setGeometry(QRect(399, -1, 53, 25))
        self.goButton.setObjectName("goButton")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QRect(-1, 525, 202, 22))
        self.comboBox.setObjectName("comboBox")
        self.pathEdit = QLineEdit(self.centralwidget)
        self.pathEdit.setGeometry(QRect(200, 525, 271, 22))
        self.pathEdit.setReadOnly(True)
        self.pathEdit.setObjectName("pathEdit")
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QRect(469, 524, 33, 24))
        self.toolButton.setObjectName("toolButton")
        self.downButton = QPushButton(self.centralwidget)
        self.downButton.setGeometry(QRect(449, -1, 53, 25))
        self.downButton.setObjectName("downButton")
        self.downAllButton = QPushButton(self.centralwidget)
        self.downAllButton.setGeometry(QRect(499, -1, 53, 25))
        self.downAllButton.setObjectName("downAllButton")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QRect(-1, 546, 552, 134))
        self.listWidget.setDragEnabled(True)
        self.listWidget.setObjectName("listWidget")
        self.clrButton = QPushButton(self.centralwidget)
        self.clrButton.setGeometry(QRect(499, 524, 52, 24))
        self.clrButton.setObjectName("clrButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        icon = QIcon()
        icon.addPixmap(QPixmap("resource/icon.png"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tube Downloader"))
        self.prevButton.setText(_translate("MainWindow", "←"))
        self.homeButton.setText(_translate("MainWindow", "HOME"))
        self.nextButton.setText(_translate("MainWindow", "→"))
        self.goButton.setText(_translate("MainWindow", "GO"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.downButton.setText(_translate("MainWindow", "↓"))
        self.clrButton.setText(_translate("MainWindow", "clear"))
        self.downAllButton.setText(_translate("MainWindow", "↓+"))
