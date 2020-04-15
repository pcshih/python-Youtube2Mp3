import os
import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from pytube import Playlist,YouTube
import ffmpeg

from Ui_MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # ui init
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MainWindow Title
        self.setWindowTitle('Youtube2Mp3')

        # set window icon
        icon_path = self.resource_path('icon/icon_window.png')
        self.setWindowIcon(QtGui.QIcon(icon_path))

        # save place
        self.save_dir = '轉換的音樂'
        os.makedirs(self.save_dir, exist_ok=True)

        # convert button
        self.ui.convertButton.clicked.connect(self.convert)

        # status label
        self.ui.statusLabel.setText('')

    # for packaging one file on pyinstaller
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath('.')

        return os.path.join(base_path, relative_path)

    def convert(self):
        url_text = self.ui.urlEdit.text()
        if url_text is not '':
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            try:
                video = YouTube(url_text)
                video_name = video.title
                if video_name=='Youtube':
                    self.convert()
                mp4_file_path = os.path.join(self.save_dir, f'{video_name}.mp4')
                video.streams.filter(progressive=True, file_extension='mp4').first().download(output_path=self.save_dir, filename=video_name)
                mp3_file_path = os.path.join(self.save_dir, f'{video_name}.mp3')
                stream = ffmpeg.input(mp4_file_path)
                stream = ffmpeg.output(stream, mp3_file_path)
                ffmpeg.run(stream, overwrite_output=True)
                os.remove(mp4_file_path)
            except: # fail to convert
                self.ui.statusLabel.setText('轉換失敗，請重試一次')
            else:
                self.ui.statusLabel.setText('轉換成功')
            
            QtWidgets.QApplication.restoreOverrideCursor()
            self.ui.urlEdit.setText('')

        else:
            self.ui.statusLabel.setText('請輸入 Youtube 網址')
        



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
