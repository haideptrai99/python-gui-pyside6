# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
    QAction,
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
    QMainWindow,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QStatusBar,
    QTextEdit,
    QToolBar,
    QVBoxLayout,
    QWidget,
)
import resource_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        icon = QIcon()
        icon.addFile(":/images/quitIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionQuit.setIcon(icon)
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        icon1 = QIcon()
        icon1.addFile(":/images/copyIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionCopy.setIcon(icon1)
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        icon2 = QIcon()
        icon2.addFile(":/images/cutIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionCut.setIcon(icon2)
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        icon3 = QIcon()
        icon3.addFile(":/images/pasteIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionPaste.setIcon(icon3)
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        icon4 = QIcon()
        icon4.addFile(":/images/undoIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionUndo.setIcon(icon4)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        icon5 = QIcon()
        icon5.addFile(":/images/aboutIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbout.setIcon(icon5)
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        icon6 = QIcon()
        icon6.addFile(":/images/aboutQtIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbout_Qt.setIcon(icon6)
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        icon7 = QIcon()
        icon7.addFile(":/images/redoIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionRedo.setIcon(icon7)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRedo)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", "Quit", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", "Copy", None))
        self.actionCut.setText(QCoreApplication.translate("MainWindow", "Cut", None))
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", "Paste", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", "Undo", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", "About", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", "AboutQt", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", "Redo", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", "Edit", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", "toolBar", None))

    # retranslateUi
