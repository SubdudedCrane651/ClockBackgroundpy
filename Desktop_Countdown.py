import sys
import json
from datetime import datetime
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QGuiApplication, QColor, QPalette
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class CountdownBox(QWidget):
    def __init__(self, title, target_datetime, text_color):
        super().__init__()

        self.target = target_datetime

        # Window style
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Layout
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)

        # Title
        self.label_title = QLabel(title)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_title.setFont(QFont("Segoe UI", 12, QFont.Weight.Bold))

        # Time
        self.label_time = QLabel("")
        self.label_time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_time.setFont(QFont("Segoe UI", 11))

        # Transparent black background
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(0, 0, 0, 160))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(text_color))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        layout.addWidget(self.label_title)
        layout.addWidget(self.label_time)
        self.setLayout(layout)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_countdown)
        self.timer.start(1000)

        self.update_countdown()

    def update_countdown(self):
        now = datetime.now()
        delta = self.target - now

        if delta.total_seconds() <= 0:
            self.label_time.setText("00d 00h 00m 00s")
            return

        days = delta.days
        hours, rem = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(rem, 60)

        self.label_time.setText(f"{days:02d}d {hours:02d}h {minutes:02d}m {seconds:02d}s")


def load_events(json_path):
    with open(json_path, "r") as f:
        return json.load(f)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    import os, sys, json

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

json_path = resource_path("events.json")

with open(json_path, "r") as f:
    events = json.load(f)

    boxes = []

    # Create countdown boxes from JSON
    for event in events:
        title = event["event"]
        target = datetime.strptime(event["date"], "%Y-%m-%d %H:%M:%S")
        color = event["color"]

        box = CountdownBox(title, target, color)
        box.adjustSize()
        boxes.append(box)

    # Position all boxes at top-right
    screen = QGuiApplication.primaryScreen().availableGeometry()
    x = screen.right() - boxes[0].width() - 20

    y_offset = 20
    for box in boxes:
        box.move(x, screen.top() + y_offset)
        box.show()
        y_offset += box.height() + 20
        
    print("Countdown boxes are running. Close this to exit the application.")        

    sys.exit(app.exec())
