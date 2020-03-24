from PyQt5.QtCore import *
# from bs4 import BeautifulSoup
# import urllib.request
# import re
from pytube import Playlist
import time



class UrlCollector(QThread) :
    sig = pyqtSignal()

    def __init__(self, parent) :
        QThread.__init__(self)
        self.main = parent

    def urlCollect(self) :
        # v = re.compile('\/watch\?v=.+;index=[0-9]+')
        # rt = urllib.request.urlopen(self.url)
        # soup = BeautifulSoup(rt, "html.parser")
        # tmp_list = list(set(v.findall(str(soup))))
        # for i in range(len(tmp_list)) :
        #     tmp_list[i] = "https://www.youtube.com/"+tmp_list[i]
        #     self.main.urlList.append(tmp_list[i])
        self.url = self.main.urlEdit.text().strip()

        #pop() 뒤에서부터 ..
        self.main.urlList = list(reversed(Playlist(self.url).video_urls)) + self.main.urlList
        print("len(self.main.urlList)",len(self.main.urlList))

    def run(self) :
        self.urlCollect()
        # for i in self.main.urlList :
        #     print(i)
        while len(self.main.urlList) > 0 :
            if self.main.counter > 0 :
                self.main.counter -= 1
                # print("self.main.counter",self.main.counter)

                self.sig.emit()

                continue
            time.sleep(2)   #렉조금 줄여줌.
        self.main.showStatusMsg("")
