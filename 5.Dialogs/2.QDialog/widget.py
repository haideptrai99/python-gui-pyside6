from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QDialog
from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("QDialog Demo")
