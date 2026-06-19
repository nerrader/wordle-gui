from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from wordle_gui.views.topbar import Topbar


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setMinimumSize(1024, 768)
        container = QWidget()
        container.setObjectName("main_container")
        self.setCentralWidget(container)

        topbar = Topbar()
        master_layout = QVBoxLayout()
        master_layout.addWidget(topbar, alignment=Qt.AlignmentFlag.AlignTop)
        master_layout.setContentsMargins(0, 0, 0, 0)

        container.setLayout(master_layout)
