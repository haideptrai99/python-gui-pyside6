import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Our fist main window app")
button = QPushButton()
button.setText("Press me")
window.setCentralWidget(button)
window.show()
app.exec()
