import sys

from mainwindow import MainWindow
from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)
w = MainWindow(app)
w.show()
app.exec()
