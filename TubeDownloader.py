import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import *
# from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl

from lib.main_ui import Ui_MainWindow
from lib.downConfirm import DownConfirm
import pytube
from threading import Thread
from PyQt5.QtCore import *

from lib.downloader import Downloader
from lib.item import Item
from lib.urlCollector import UrlCollector




#https://doc.qt.io/archives/qt-4.8/qtgui-module.html
#https://doc.qt.io/qt-5/qthread.html
#https://python-pytube.readthedocs.io/en/latest/api.html
#https://www.riverbankcomputing.com/static/Docs/PyQt5/api/qtcore/qtcore-module.html
#내 재생목록+관련 재생목록
#구독채널 downAll?
#urlopen error [WinError 10060] 연결된 구성원으로부터 응답이 없어 연결하지 못했거나, 호스트로부터 응답이 없어 연결이 끊어졌습니다.
#statusmessage
#import 정리
#addbar thread?(렉)
#mp3변환시 다른프로세스가 사용중.. ***?
#url - 페이지 - 버튼
#downallprocess 증발  *** pytube문제?
#addbar clone   XXXXXXXXXXXXXX
#다운로드 수 표시(13/100)?
#실패시 파일이름 or 재시작 (urlopen 에러)
#HTTP Error 403 : Forbidden                      (settube())
#'streamingData' - 국가 차단?                     (settube())
#Remote end closed connection without response   (settube())
#get_ytplayer_config : could not find match for config_patterns (settube())
#더블클릭-멈춤(재시작 추가후)
#counter관리 다시   ***

#Exception
#'formats' : livestream


class TubeMain(QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()
        self.downList = []
        self.setupUi(self)
        self.homeURL = "https://www.youtube.com"
        self.go_home()
        self.downPath = self.pathEdit.text().strip()
        self.itemList = []
        self.itemList2 = []
        self.urlList = []
        self.trashList = []
        self.counter = 10   #동시 다운로드 수
        # self.total = 0
        self.defaultDownPath = str(os.getcwd()).replace("\\","/")+"/downloads"
        self.comboBox.addItem("select one")
        self.comboBox.addItem("720p↓  /mp4")
        self.comboBox.addItem("720p↑ (video only)  /mp4")
        self.comboBox.addItem("(audio only)  /mp3")
        self.pathEdit.setText(self.defaultDownPath)
        self.th_downAll = UrlCollector(self)
        self.initSignal()

    def initSignal(self) :
        self.homeButton.clicked.connect(self.go_home)
        self.prevButton.clicked.connect(self.go_prev)
        self.nextButton.clicked.connect(self.go_next)
        self.urlEdit.returnPressed.connect(lambda: self.go_URL(self.urlEdit.text().strip()))
        self.goButton.clicked.connect(lambda: self.go_URL(self.urlEdit.text().strip()))
        self.toolButton.clicked.connect(self.setDownPath)
        self.listWidget.itemActivated.connect(self.activateItem)
        self.webEngineView.loadStarted.connect(lambda: self.showStatusMsg(self.urlEdit.text().strip() + "로딩중"))
        self.webEngineView.loadFinished.connect(lambda: self.showStatusMsg(""))
        self.webEngineView.urlChanged.connect(self.set_urlEdit)
        self.downButton.clicked.connect(lambda: self.downProcess(self.urlEdit.text().strip()))
        self.downAllButton.clicked.connect(self.downAllConfirm)
        self.th_downAll.sig.connect(lambda: self.downProcess(None, True))

    def showStatusMsg(self, msg) :
        self.statusbar.showMessage(msg)

    def go_URL(self, url) :
        if not url.startswith("http") :
            url = "http://"+url
        self.webEngineView.load(QUrl(url))

    def set_urlEdit(self) :
        self.showStatusMsg("")
        self.urlEdit.setText(self.webEngineView.url().toString())
        if self.urlEdit.text().strip().startswith("https://www.youtube.com/watch") :
            self.downButton.setEnabled(True)
        else :
            self.downButton.setEnabled(False)

        if self.urlEdit.text().strip().startswith("https://www.youtube.com/playlist?list") or self.urlEdit.text().strip().find("&list=") >= 0:
            self.downAllButton.setEnabled(True)
        else :
            self.downAllButton.setEnabled(False)

    def showStatusMsg(self, msg) :
        self.statusbar.showMessage(msg)

    @pyqtSlot()
    def go_home(self) :
        # print("go_home")
        self.go_URL(self.homeURL)

    def go_prev(self) :
        # print("go_prev")
        self.webEngineView.back()

    def go_next(self) :
        # print("go_next")
        self.webEngineView.forward()


    def setDownPath(self) :
        fpath = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if fpath == "" :
            fpath = self.defaultDownPath
        self.pathEdit.setText(fpath)
        self.downPath = fpath

    def activateItem(self, item) :
        if self.downList[int(item.whatsThis())].failed == True :
            if not self.downList[int(item.whatsThis())].isRunning() :
                self.downList[int(item.whatsThis())].counted=False
                self.downList[int(item.whatsThis())].start()
            return

        if self.downList[int(item.whatsThis())].progressed < 100 :
            print("downloading ",self.downList[int(item.whatsThis())].progressed)
            return
        path = self.downList[int(item.whatsThis())].dir+"/"+self.downList[int(item.whatsThis())].filename
        if not os.path.exists(self.downList[int(item.whatsThis())].dir+"/"+self.downList[int(item.whatsThis())].filename) :
            print("file not exists",self.downList[int(item.whatsThis())].dir+"/"+self.downList[int(item.whatsThis())].filename)
            return
        print("item activated",path)
        os.startfile(path)

    def cancelB(self, idx) :
        self.downList[int(idx)].go = False
        self.itemList2[int(idx)].setHidden(True)

    def setFilename(self, th) :
        if th.streamIndex == 2 :
            if th.filename.endswith("(audio).mp3"):
                self.itemList[th.thIdx].label.setText(th.filename[0:len(th.filename)-11])
            elif th.filename.endswith("(audio).mp4"):
                self.itemList[th.thIdx].label.setText(th.filename[0:len(th.filename)-11])
            else :
                self.itemList[th.thIdx].label.setText(th.filename[0:len(th.filename)-4])
        else :
            self.itemList[th.thIdx].label.setText(th.filename[0:len(th.filename)-4])

    def setProgressBar(self, th) :
        self.itemList[th.thIdx].pgb.setValue(th.progressed)

    def tube_err(self, th) :
        self.itemList[th.thIdx].label.setText(f"({th.err_msg} 재시작 : 더블클릭){th.filename[0:len(th.filename)-4]}")
        self.itemList[th.thIdx].label.setStyleSheet('color:red;')

    def tube_comp(self, th) :
        self.itemList[th.thIdx].pgb.setValue(100)
        self.itemList[th.thIdx].label.setStyleSheet('color:green;')

    def downProcess(self, url=None, counted=False) :

        if self.comboBox.currentIndex() == 0 :
            QMessageBox.about(self, "파일형식선택", "파일 형식을 선택해주세요.")
            return

        if url == None :
            try :
                url = self.urlList.pop()
            except Exception as e :
                print("pop() exception",e)
                return

        th = Downloader(len(self.downList), url, self)
        filename = "===파일을 불러오는 중입니다.==="
        th.sig1.connect(lambda: self.setFilename(th))
        th.sig2.connect(lambda: self.setProgressBar(th))
        th.sig_err.connect(lambda: self.tube_err(th))
        th.sig_comp.connect(lambda: self.tube_comp(th))
        self.addDownBar(filename)
        if counted :
            th.counted = True
        th.start()
        self.downList.append(th)

    def downAllConfirm(self) :
        if self.comboBox.currentIndex() == 0 :
            QMessageBox.about(self, "파일형식선택", "파일 형식을 선택해주세요.")
            return
        Dialog = QtWidgets.QDialog()
        dc = DownConfirm()
        dc.setupUi(Dialog)
        Dialog.exec_()
        if dc.confirmed :
            self.downAllProcess()

    def downAllProcess(self) :
        # print("downallprocess",self.urlEdit.text().strip())
        self.showStatusMsg("재생목록을 불러오는 중입니다.")
        if self.th_downAll.isRunning() :
            tmpTh = Thread(target=self.th_downAll.urlCollect)
            tmpTh.start()
            self.trashList.append(tmpTh)
            return
        self.th_downAll.start()

    def downAllProcess_2(self) :
        self.showStatusMsg("")
        # print("downallprocess2")
        for i in range(len(self.urlList)) :
            self.downProcess(self.urlList[i])

    def addDownBar(self, filename) :
        # print("addbar --")
        item = QListWidgetItem(self.listWidget)
        tem1 = Item(filename)
        item.setWhatsThis(str(len(self.itemList)))
        item.setSizeHint(tem1.sizeHint())
        tem1.pb.clicked.connect(lambda: self.cancelB(item.whatsThis()))
        self.listWidget.setItemWidget(item, tem1)
        self.listWidget.addItem(item)
        self.itemList.append(tem1)
        self.itemList2.append(item)



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = TubeMain()
    window.show()
    app.exec_()
