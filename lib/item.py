
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget,QBoxLayout,QProgressBar,QLabel,QPushButton
from PyQt5.QtCore import Qt, QMargins

class Item(QWidget):
    def __init__(self, filename):
        QWidget.__init__(self, flags=Qt.Widget)
        self.layout = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout.setContentsMargins(QMargins())
        self.pgb = QtWidgets.QProgressBar(self)
        self.pgb.setProperty("value", 0)
        self.pgb.setTextVisible(False)
        self.pgb.setObjectName("pgb")
        self.label = QtWidgets.QLabel(self)
        self.label.setMinimumSize(250,30)
        self.label.setObjectName("label")
        self.label.setMaximumSize(250,30)
        self.label.setText(filename)
        self.pb = QPushButton("X")
        self.pb.setMinimumSize(30,30)
        self.pb.setMaximumSize(30,30)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.pgb)
        self.layout.addWidget(self.pb)
        self.layout.setSizeConstraint(QBoxLayout.SetDefaultConstraint)
        self.setLayout(self.layout)
