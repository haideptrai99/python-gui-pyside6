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
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QSizePolicy, QVBoxLayout, QWidget
import resource_rc


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName("Widget")
        Widget.resize(400, 68)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.provide_info_button = QPushButton(Widget)
        self.provide_info_button.setObjectName("provide_info_button")
        icon = QIcon()
        icon.addFile(":/images/information.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.provide_info_button.setIcon(icon)

        self.verticalLayout.addWidget(self.provide_info_button)

        self.info_label = QLabel(Widget)
        self.info_label.setObjectName("info_label")

        self.verticalLayout.addWidget(self.info_label)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", "Form", None))
        self.provide_info_button.setText(QCoreApplication.translate("Widget", "Provide Info", None))
        self.info_label.setText(QCoreApplication.translate("Widget", "Some text", None))

    # retranslateUi
