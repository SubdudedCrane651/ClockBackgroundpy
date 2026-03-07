import sys
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QFont, QPalette, QColor
import ctypes

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import os
os.environ["QT_LOGGING_RULES"] = "qt.qpa.fonts=false"

def make_click_through(hwnd):
    # WS_EX_TRANSPARENT = 0x20
    # WS_EX_LAYERED = 0x80000
    styles = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
    ctypes.windll.user32.SetWindowLongW(hwnd, -20, styles | 0x20 | 0x80000)

class DesktopClock(QLabel):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Tool |
            Qt.WindowStaysOnBottomHint |
            Qt.X11BypassWindowManagerHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        font = QFont("Segoe UI", 32, QFont.Bold)
        self.setFont(font)

        palette = QPalette()
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        self.setPalette(palette)

        self.update_time()

        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)

        self.resize(300, 80)
        self.move(30, 30)

        self.show()

        hwnd = self.winId().__int__()
        make_click_through(hwnd)

    def update_time(self):
        self.setText(QTime.currentTime().toString("HH:mm:ss"))

app = QApplication(sys.argv)
clock = DesktopClock()
sys.exit(app.exec_())