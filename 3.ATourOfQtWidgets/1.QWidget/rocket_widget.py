from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget


class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("demo widget")
        button1 = QPushButton("Button 1")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Button 2")
        button2.clicked.connect(self.button2_clicked)
        widget_layout = QHBoxLayout()
        widget_layout.addWidget(button1)
        widget_layout.addWidget(button2)
        self.setLayout(widget_layout)

    def button1_clicked(self):
        print("button 1 click")

    def button2_clicked(self):
        print("button 2 click")
