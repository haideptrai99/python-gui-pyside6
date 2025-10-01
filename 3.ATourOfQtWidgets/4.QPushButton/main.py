from PySide6.QtWidgets import QApplication
from widget import Widget

app = QApplication()
window = Widget()
window.show()
app.exec()
