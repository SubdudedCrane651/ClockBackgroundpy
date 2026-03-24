import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import os
os.environ["QT_LOGGING_RULES"] = "qt.qpa.fonts=false"


# ---------------- 3D SHADOW TEXT LABEL ---------------- #

class ShadowText(QtWidgets.QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.font = QtGui.QFont("Segoe UI", 48, QtGui.QFont.Bold)
        self.setStyleSheet("color: white;")

    def sizeHint(self):
        fm = QtGui.QFontMetrics(self.font)
        height = fm.height() + 20   # extra space for shadow
        width = fm.width(self.text()) + 10
        return QtCore.QSize(width, height)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setFont(self.font)

        text = self.text()
        fm = QtGui.QFontMetrics(self.font)
        baseline = fm.ascent()

        # Shadow
        painter.setPen(QtGui.QColor(0, 0, 0, 180))
        painter.drawText(4, 4 + baseline, text)

        # Main text
        painter.setPen(QtGui.QColor(255, 255, 255))
        painter.drawText(0, baseline, text)


# ---------------- MAIN WINDOW ---------------- #

class DesktopClock(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Transparent, click-through, no border
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.WindowStaysOnBottomHint |
            QtCore.Qt.Tool
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        # 3D Clock label
        self.clock_label = ShadowText()
        layout.addWidget(self.clock_label)

        self.setLayout(layout)

        # Timer for clock
        self.timer_clock = QtCore.QTimer()
        self.timer_clock.timeout.connect(self.update_clock)
        self.timer_clock.start(1000)

        # Initial update
        self.update_clock()

        # Position on desktop
        self.move(50, 50)

    # ---------------- UPDATE FUNCTIONS ---------------- #

    def update_clock(self):
        current_time = QtCore.QTime.currentTime().toString("hh:mm:ss")
        self.clock_label.setText(current_time)
        self.clock_label.repaint()


# ---------------- RUN APP ---------------- #

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    clock = DesktopClock()
    clock.show()
    sys.exit(app.exec_())