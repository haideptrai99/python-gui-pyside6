################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
)
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)


class Ui_Widget:
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName("Widget")
        Widget.resize(506, 154)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.full_name_line_edit = QLineEdit(Widget)
        self.full_name_line_edit.setObjectName("full_name_line_edit")

        self.horizontalLayout.addWidget(self.full_name_line_edit)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.occupation_line_edit = QLineEdit(Widget)
        self.occupation_line_edit.setObjectName("occupation_line_edit")

        self.horizontalLayout_2.addWidget(self.occupation_line_edit)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.submit_button = QPushButton(Widget)
        self.submit_button.setObjectName("submit_button")

        self.verticalLayout.addWidget(self.submit_button)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", "Form", None))
        self.label.setText(QCoreApplication.translate("Widget", "Fullname :", None))
        self.label_2.setText(QCoreApplication.translate("Widget", "Ocuupation :", None))
        self.submit_button.setText(QCoreApplication.translate("Widget", "Submit", None))

    # retranslateUi
