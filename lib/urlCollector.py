from PyQt5.QtCore import QThread, pyqtSignal
from pytube import Playlist
import time



class UrlCollector(QThread) :
    sig = pyqtSignal()

    def __init__(self, parent) :
        QThread.__init__(self)
        self.main = parent

    def urlCollect(self) :
        self.url = self.main.urlEdit.text().strip()
        plist = list(reversed(Playlist(self.url).video_urls))
        self.main.urlList = plist + self.main.urlList
        print("len(self.main.urlList)",len(self.main.urlList))
        self.main.total += len(plist)
        self.main.sig_title.emit()

    def run(self) :
        self.urlCollect()
        while len(self.main.urlList) > 0 :
            if self.main.counter > 0 :
                self.main.counter -= 1
                self.sig.emit()
                continue
            time.sleep(2)
        self.main.showStatusMsg("")
