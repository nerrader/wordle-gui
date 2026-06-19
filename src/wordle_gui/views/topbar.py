from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy,
)
from PySide6.QtCore import Qt

from wordle_gui.__init__ import __version__ as game_version


class Topbar(QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

        self.setMinimumHeight(110)
        self.setMaximumHeight(200)

        self.setup_components()
        self.setup_layouts()
        self.setup_presenters()
        self.setup_styling()

    def setup_components(self) -> None:
        self.title_label = QLabel("WORDEE")
        self.title_label.setObjectName("title_label")
        self.version_label = QLabel(f"version {game_version}")
        self.version_label.setObjectName("version_label")

        self.game_icon = QPushButton()

        self.help_icon = QPushButton()
        self.statistics_icon = QPushButton()
        self.settings_icon = QPushButton()

    def setup_layouts(self) -> None:
        title_labels_layout = QVBoxLayout()
        title_labels_layout.addWidget(self.title_label)
        title_labels_layout.addWidget(self.version_label)

        logo_area_layout = QHBoxLayout()
        logo_area_layout.addLayout(title_labels_layout)
        logo_area_layout.addWidget(self.game_icon)
        logo_area_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        icon_area_layout = QHBoxLayout()
        icon_area_layout.addWidget(self.help_icon)
        icon_area_layout.addWidget(self.statistics_icon)
        icon_area_layout.addWidget(self.settings_icon)
        icon_area_layout.setAlignment(Qt.AlignmentFlag.AlignRight)

        topbar_layout = QHBoxLayout()
        topbar_layout.addLayout(logo_area_layout)
        topbar_layout.addLayout(icon_area_layout)

        self.setLayout(topbar_layout)

    def setup_presenters(self) -> None:
        pass

    def setup_styling(self) -> None:
        pass
