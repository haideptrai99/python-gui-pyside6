# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName("Widget")
        Widget.resize(310, 460)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button = QPushButton(Widget)
        self.button.setObjectName("button")

        self.verticalLayout_2.addWidget(self.button)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.value_label = QLabel(Widget)
        self.value_label.setObjectName("value_label")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.value_label.setFont(font)

        self.horizontalLayout.addWidget(self.value_label)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName("radioButton_3")

        self.verticalLayout.addWidget(self.radioButton_3)

        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox = QComboBox(Widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName("lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.textEdit = QTextEdit(Widget)
        self.textEdit.setObjectName("textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", "Form", None))
        self.button.setText(QCoreApplication.translate("Widget", "Click", None))
        self.label_2.setText(QCoreApplication.translate("Widget", "Value : ", None))
        self.value_label.setText(QCoreApplication.translate("Widget", "[Value]", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", "GroupBox", None))
        self.radioButton.setText(QCoreApplication.translate("Widget", "RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("Widget", "RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("Widget", "RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", "One", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget", "Two", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Widget", "Three", None))

    # retranslateUi
