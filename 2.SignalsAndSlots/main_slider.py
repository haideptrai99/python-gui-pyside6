from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider


# The slot : responds when something happens
def respond_to_slider(data):
    print("slider moved to : ", data)


app = QApplication()
slider = QSlider()
slider.setOrientation(Qt.Orientation.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

# You just do the connection. The Qt system takes care of
#  passing the data from the signal to the slot.
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
