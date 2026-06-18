from PySide6.QtWidgets import QMainWindow, QWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        container = QWidget()
        self.setCentralWidget(container)
