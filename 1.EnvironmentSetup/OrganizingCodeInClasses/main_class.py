import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class ShowButton(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAnimated(False)
        self.setWindowTitle("Button class")
        button = QPushButton("Press me")
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = ShowButton()
window.show()
app.exec()
