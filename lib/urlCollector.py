from PyQt5.QtCore import QThread, pyqtSignal
from pytube import Playlist
import time

class UrlCollector(QThread) :
    sig = pyqtSignal()

    def __init__(self, parent) :
        QThread.__init__(self)
        self.main = parent

    def urlCollect(self) :
        tmp_streamIndex = self.main.comboBox.currentIndex()
        self.url = self.main.urlEdit.text().strip()
        plist = Playlist(self.url).video_urls
        tmp_streamIndexList = [tmp_streamIndex for _ in range(len(plist))]
        self.main.urlList += plist
        self.main.streamIndexList += tmp_streamIndexList
        self.main.total += len(plist)
        self.main.sig_title.emit()

    def run(self) :
        self.urlCollect()
        while len(self.main.urlList) > self.main.urlCheck :
            if self.main.counter > 0 :
                self.main.counter -= 1
                self.sig.emit()
                continue
            time.sleep(2)
        self.main.showStatusMsg("")
