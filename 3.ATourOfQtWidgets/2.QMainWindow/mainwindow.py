from PySide6.QtCore import QSize, Slot
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QPushButton, QStatusBar, QToolBar


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom main window")
        # build menu once during initialization
        self._build_menus()

    def _build_menus(self):
        menu_bar = self.menuBar()
        # menu File
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction("New")
        file_menu.addAction("Open")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.app.quit)

        # menu Edit
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        # other Menus
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        # toolbars
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(10, 10))
        self.addToolBar(toolbar)
        toolbar.addAction(quit_action)

        # using QAction
        action1 = QAction("Some Action", self)
        action1.setToolTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        # using Action with icon
        action2 = QAction(QIcon("start.png"), "Some other action", self)
        action2.setToolTip("Status message for some other action")
        action2.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action2)

        # add Separator
        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click here", self))

        # add Status bar
        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage("Status bar")

    def quit_app(self):
        self.app.quit()

    @Slot()
    def toolbar_button_click(self):
        print("action triggered")
