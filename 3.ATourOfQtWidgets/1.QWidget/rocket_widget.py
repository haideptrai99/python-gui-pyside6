from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget


def button1_clicked():
    print("button 1 click")


def button2_clicked():
    print("button 2 click")


class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("demo widget")
        button1 = QPushButton("Button 1")
        button1.clicked.connect(button1_clicked)
        button2 = QPushButton("Button 2")
        button2.clicked.connect(button2_clicked)
        widget_layout = QHBoxLayout()
        widget_layout.addWidget(button1)
        widget_layout.addWidget(button2)
        self.setLayout(widget_layout)
