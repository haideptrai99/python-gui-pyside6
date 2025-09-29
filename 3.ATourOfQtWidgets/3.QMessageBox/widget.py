from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox, QPushButton, QVBoxLayout, QWidget


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message Box")
        self.setMinimumSize(700, 700)
        # create PushButton
        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)
        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)
        # add button to the layout
        layout = QVBoxLayout()
        layout.addWidget(button_critical)
        layout.addWidget(button_warning)
        self.setLayout(layout)

    @Slot()
    def button_clicked_critical(self):
        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle("Message title")
        message.setText("Something happened !!")
        message.setInformativeText("This is more information")
        message.setIcon(QMessageBox.Icon.Critical)
        message.setStandardButtons(
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
        )
        message.setDefaultButton(QMessageBox.StandardButton.Ok)
        ret = message.exec()
        if ret == QMessageBox.StandardButton.Ok:
            print("Ok button clicked")
        else:
            print("Cancel button clicked")

    @Slot()
    def button_clicked_warning(self):
        ret = QMessageBox.warning(
            self,
            "Message title",
            "Warning message",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
        )
        if ret == QMessageBox.StandardButton.Ok:
            print("Ok button clicked")
        else:
            print("Cancel button clicked")
