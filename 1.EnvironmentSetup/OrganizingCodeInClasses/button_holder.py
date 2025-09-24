from PySide6.QtWidgets import QMainWindow, QPushButton


class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Class button holder")
        button = QPushButton("press me now baby !!")
        self.setCentralWidget(button)
