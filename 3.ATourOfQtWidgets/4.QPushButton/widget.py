from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Slot


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("demo PushButton")
        self.setMinimumSize(700, 700)

        button = QPushButton("Press me")
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)

        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)

    @Slot()
    def button_clicked(self):
        print("button clicked")

    @Slot()
    def button_pressed(self):
        print("button pressed")

    @Slot()
    def button_released(self):
        print("button released")
