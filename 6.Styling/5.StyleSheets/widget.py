from infodialog import InfoDialog
from PySide6.QtWidgets import QDialog, QWidget
from ui_widget import Ui_Widget


class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User data")
        self.provide_info_button.clicked.connect(self.provide_info)

        self.info_dialog = InfoDialog()

    def provide_info(self):
        ret = self.info_dialog.exec()
        if ret == QDialog.DialogCode.Accepted:
            self.info_label.setText(
                "Your position is "
                + self.info_dialog.position
                + " and your favorite os is "
                + self.info_dialog.favorite_os
            )
        else:
            print("Dialog rejected")
