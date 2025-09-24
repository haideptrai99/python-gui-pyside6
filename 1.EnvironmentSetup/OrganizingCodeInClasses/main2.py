from button_holder import ButtonHolder
from PySide6.QtWidgets import QApplication

app = QApplication()
window = ButtonHolder()
window.show()
app.exec()
