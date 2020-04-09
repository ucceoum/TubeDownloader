import pytube
from PyQt5.QtCore import QThread, pyqtSignal
import os
from urllib import error
class Downloader(QThread) :
    sig1 = pyqtSignal()
    sig2 = pyqtSignal()
    sig_err = pyqtSignal()
    sig_comp = pyqtSignal()
    def __init__(self, parent, idx, url, streamIndex) :
        QThread.__init__(self)
        self.url = url
        self.thIdx = idx
        self.filename = ""
        self.main = parent
        self.progressed = 0
        self.go = True
        self.failed = False
        self.counted = False
        self.err_msg = ""
        self.streamIndex = streamIndex-1

    def setTube(self) :
        self.err_msg = ""
        self.tube = None
        self.tubeC = None
        self.tube = pytube.YouTube(self.url)
        if self.streamIndex == 0 :
            self.tubeC = self.tube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        elif self.streamIndex == 1 :
            self.tubeC = self.tube.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()
        else :
            self.tubeC = self.tube.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()

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
            self.progressed = prog
            self.sig2.emit()

    def downCompleted(self, stream=None, file_path=None) :
        self.failed = False
        self.err_msg = ""
        self.sig_comp.emit()


    def counterBack(self) :
        if self.counted :
            self.main.counter += 1
            self.counted = False

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
            print("e type",type(e))
            if type(e) == pytube.exceptions.RegexMatchError :
                self.err_msg = "영상을 찾을 수 없습니다."
            elif type(e) == KeyError :
                self.err_msg = "차단된 영상이거나 Live 영상입니다."
            elif type(e) == error.URLError :
                self.err_msg = "URL로딩 오류, 재시작 : 더블클릭"
            elif type(e) == error.HTTPError :
                self.err_msg = "연령제한이 있는 영상입니다."
            else :
                self.err_msg = "로딩 오류, 재시작 : 더블클릭"
        if self.err_msg != "" :
            print("exception - setTube() ,", self.url," idx :",self.thIdx)
            self.sig_err.emit()
            self.failed = True
            self.counterBack()
            return
        try :
            if self.go :
                self.tubeC.download(self.dir, self.filename[0:(len(self.filename)-4)], skip_existing=False)
        except Exception as e :
            print("Exception e = ",e)

            print("download exception")
            self.err_msg = "다운로드 오류"
            self.sig_err.emit()
            self.failed = True
            self.counterBack()
            if os.path.exists(self.dir+"/"+self.filename) :
                os.remove(r'{}'.format((self.dir+"/"+self.filename)))
            return
        if os.path.exists(self.dir+"/"+self.filename) or os.path.exists(self.dir+"/"+self.filename[0:(len(self.filename)-4)]+".mp3") :
            self.progressed = 100
            self.failed = False
            self.err_msg = ""
            self.sig2.emit()
        self.counterBack()
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
            file = self.dir+"/"+self.filename
            fileC = os.path.splitext(self.dir+"/"+self.filename)
            try :
                os.rename(file.replace("/","\\"), fileC[0][:len(fileC[0])-7] + '.mp3' )
            except Exception as e :
                print(e)
                print("mp3 path exception")
            self.filename = self.filename[0:len(self.filename)-11] + '.mp3'
