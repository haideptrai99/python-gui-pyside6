from PySide6.QtWidgets import QApplication
from rocket_widget import RockWidget

app = QApplication()
window = RockWidget()
window.show()
app.exec()
