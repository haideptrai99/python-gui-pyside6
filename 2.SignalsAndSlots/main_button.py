from PySide6.QtWidgets import QApplication, QPushButton


def button_clicked(data):
    print("click me", data)


app = QApplication()
button = QPushButton("Press me")
button.setCheckable(True)
button.clicked.connect(button_clicked)
button.show()
app.exec()
