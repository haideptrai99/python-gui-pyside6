import sys

from PySide6 import QtWidgets
from widget import Widget
from dump_qt_ui import generate_qss_skeleton

app = QtWidgets.QApplication(sys.argv)

# Open the css styles file and read in the css-alike styling code
with open("styles/style.css", "r") as f:
    style = f.read()
    # Set the stylesheet of the application
    app.setStyleSheet(style)

window = Widget()
window.show()
generate_qss_skeleton(app)
app.exec()
