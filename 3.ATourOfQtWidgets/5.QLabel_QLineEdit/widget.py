from PySide6.QtCore import Slot
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("demo Label and Qline edit")
        self.setMinimumSize(400, 100)
        # create label
        label = QLabel("Enter your name")
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Enter your name")
        # self.line_edit.textChanged.connect(self.line_edit_text_change)
        # self.line_edit.cursorPositionChanged.connect(self.cursor_position_change)
        # enter finish
        self.line_edit.editingFinished.connect(self.editing_finish)
        # return finish = enter finish
        # self.line_edit.returnPressed.connect(self.return_pressed)
        # self.line_edit.selectionChanged.connect(self.selection_changed)
        # self.line_edit.textEdited.connect(self.text_edited)

        # create button
        button = QPushButton("Grab data")
        button.clicked.connect(self.button_clicked)
        self.text_result = QLabel("")

        # create layout
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_result)

        self.setLayout(v_layout)

    def button_clicked(self):
        print(f"Hello {self.line_edit.text()}")
        self.text_result.setText(f"Hello {self.line_edit.text()}")

    def line_edit_text_change(self):
        print(f"text changed {self.line_edit.text()}")
        self.text_result.setText(f"text changed {self.line_edit.text()}")

    @Slot(int, int)
    def cursor_position_change(self, old, new):
        print(f"cursor position changed old:{old} to new:{new}")

    @Slot()
    def editing_finish(self):
        print("editing finish")
        self.text_result.setText(f"text finish {self.line_edit.text()}")

    def return_pressed(self):
        print("return pressed")
        self.text_result.setText(f"return pressed {self.line_edit.text()}")

    def selection_changed(self):
        print("selection changed")
        self.text_result.setText(f"selection changed {self.line_edit.selectedText()}")

    @Slot()
    def text_edited(self, new_text):
        print(f"text edited new text:{new_text}")
