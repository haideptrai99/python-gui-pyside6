import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication
from widget import Widget

app = QApplication(sys.argv)

app.setStyle("Fusion")
darkPalette = app.palette()  # [Credit] Palette code source :
# https://gist.github.com/QuantumCD/6245215#file-qt-5-dark-fusion-palette
darkPalette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
darkPalette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
darkPalette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
darkPalette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
darkPalette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
darkPalette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
darkPalette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
darkPalette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
darkPalette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
darkPalette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
darkPalette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
darkPalette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
darkPalette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)

app.setPalette(darkPalette)

window = Widget()
window.show()

app.exec()
