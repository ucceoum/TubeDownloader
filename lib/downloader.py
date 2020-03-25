import pytube
from PyQt5.QtCore import *
import os

class Downloader(QThread) :
    sig1 = pyqtSignal()
    sig2 = pyqtSignal()
    sig_err = pyqtSignal()
    sig_comp = pyqtSignal()
    def __init__(self, idx, url, parent) :
        QThread.__init__(self)
        self.url = url
        self.thIdx = idx
        self.filename = ""
        self.main = parent
        self.progressed = 0
        self.go = True
        self.failed = False
        self.counted = False

    def setTube(self) :
        # print("setTube() - start",self.thIdx)
        self.streamIndex = self.main.comboBox.currentIndex()-1
        self.tube = pytube.YouTube(self.url)
        # print("setTube() - YouTube() ok",self.thIdx)
        self.tubeC = None
        if self.streamIndex == 0 :
            # print("index : ",self.streamIndex)
            self.tubeC = self.tube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        elif self.streamIndex == 1 :
            self.tubeC = self.tube.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()
        else :
            # print("index : ",self.streamIndex,type(self.main.streamIndex))
            self.tubeC = self.tube.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()
        # print("setTube() - streams.filter() ok",self.thIdx)
        self.filename = self.tubeC.default_filename
        self.fsize = self.tubeC.filesize
        self.dir = self.main.pathEdit.text().strip()


        if self.streamIndex == 2 :
            if os.path.exists(self.dir+"/"+self.filename[0:(len(self.filename)-4)]+".mp3") :
                self.go = False
            else :
                self.filename = self.filename[0:len(self.filename)-4]+"(audio).mp4"
        self.tube.register_on_progress_callback(self.downProgress)
        self.tube.register_on_complete_callback(self.downCompleted)
        self.sig1.emit()

    def downProgress(self, chunk, fp, bytes_remaining) :
        prog = int(((self.fsize - bytes_remaining)/self.fsize)*100)

        if prog > self.progressed :
            # print(prog)
            self.progressed = prog
            self.sig2.emit()

    def downCompleted(self, stream=None, file_path=None) :
        self.failed = False
        self.sig_comp.emit()

    def run(self) :
        try :
            for i in range(10) :
                self.setTube()
                if self.filename != "YouTube.mp4" and self.filename != "YouTube(audio).mp4" :
                    break
                else :
                    print(f"파일 이름 문제 - 쓰레드{self.thIdx} YouTube() reload")
        except Exception as e :
            print(e)
            print("exception - setTube() ,", self.url," idx :",self.thIdx)
            self.sig_err.emit()
            self.failed = True
            if self.counted :
                self.main.counter += 1
                self.counted = False
            return
        # print("시작")
        try :
            if self.go :
                self.tubeC.download(self.dir, self.filename[0:(len(self.filename)-4)], skip_existing=False)
        except Exception as e :
            print("Exception e = ",e)

            print("download exception")
            self.sig_err.emit()
            self.failed = True
            if self.counted :
                self.main.counter += 1
                self.counted = False
            if os.path.exists(self.dir+"/"+self.filename) :
                os.remove(r'{}'.format((self.dir+"/"+self.filename)))
            return

        #***
        if os.path.exists(self.dir+"/"+self.filename) or os.path.exists(self.dir+"/"+self.filename[0:(len(self.filename)-4)]+".mp3") :
            self.progressed = 100
            self.failed = False
            self.sig2.emit()
        if self.counted :
            self.main.counter += 1
            self.counted = False

        if not self.go :
            print("self.go = False, return")
            if self.streamIndex == 2 :
                if self.filename.endswith("(audio).mp4") :
                    self.filename = self.filename[0:len(self.filename)-11] + '.mp3'
                else :
                    self.filename = self.filename[0:len(self.filename)-4] + '.mp3'
                self.downCompleted()
            return

        if self.streamIndex == 2 :
            # print("path- mp3")
            file = self.dir+"/"+self.filename
            fileC = os.path.splitext(self.dir+"/"+self.filename)
            # print(self.dir+"/"+self.filename)
            # print(file)
            # print(fileC)
            try :
                os.rename(file.replace("/","\\"), fileC[0][:len(fileC[0])-7] + '.mp3' )
                pass
            except Exception as e :
                print(e)
                print("mp3 path exception")
                pass
            self.filename = self.filename[0:len(self.filename)-11] + '.mp3'
        # print("완료")
