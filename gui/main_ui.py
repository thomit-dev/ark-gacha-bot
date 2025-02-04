import json
import sys

from PySide6 import QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

from .ui_main_ui import Ui_Form

app = QApplication()

from qconfig import QConfig, tools


class MainUi(QMainWindow, Ui_Form):
    def __init__(self) -> None:
        super().__init__()
        self._allow_changes = True
        self._ignore_changes = False

        self.main_win = QtWidgets.QMainWindow()

        self.setupUi(self.main_win)
        self.tabWidget.setCurrentIndex(0)
        self.connect_tabs()

        with open("settings/settings.json") as f:
            self.data = json.load(f)

        widgets = tools.get_all_widgets(self.main_win)

        self.main_settings = QConfig(
            "main", widgets, self.data["main"], save_on_change=True
        )
        self.player_settings = QConfig(
            "player", widgets, self.data["player"], save_on_change=True
        )
        self.disc_settings = QConfig(
            "discord", widgets, self.data["discord"], save_on_change=True
        )
        self.ytrap_settings = QConfig(
            "ytrap", widgets, self.data["ytrap"], save_on_change=True
        )
        self.collection_settings = QConfig(
            "crystal", widgets, self.data["crystal"], save_on_change=True
        )
        self.berry_settings = QConfig(
            "berry", widgets, self.data["berry"], save_on_change=True
        )
        self.meat_settings = QConfig(
            "meat", widgets, self.data["meat"], save_on_change=True
        )
        self.healing_settings = QConfig(
            "healing", widgets, self.data["healing"], save_on_change=True
        )
        self.grinding_settings = QConfig(
            "grinding", widgets, self.data["grinding"], save_on_change=True
        )
        self.main_settings.set_data()
        self.player_settings.set_data()
        self.disc_settings.set_data()
        self.ytrap_settings.set_data()
        self.collection_settings.set_data()
        self.berry_settings.set_data()
        self.meat_settings.set_data()
        self.healing_settings.set_data()
        self.grinding_settings.set_data()

        self.main_settings.connect_callback(self.save)
        self.player_settings.connect_callback(self.save)
        self.disc_settings.connect_callback(self.save)
        self.ytrap_settings.connect_callback(self.save)
        self.collection_settings.connect_callback(self.save)
        self.berry_settings.connect_callback(self.save)
        self.meat_settings.connect_callback(self.save)
        self.healing_settings.connect_callback(self.save)
        self.grinding_settings.connect_callback(self.save)

    def display(self):
        self.main_win.setWindowTitle(f"Ling-Ling v2.0.1")
        self.main_win.setWindowIcon(QtGui.QIcon(("assets/gui/dust.png")))
        self.main_win.show()
        sys.exit(app.exec())

    def connect_tabs(self) -> None:

        self.general_config.clicked.connect(lambda: self.open_tab(0))
        self.ytrap_stations.clicked.connect(lambda: self.open_tab(1))
        self.crystal_station.clicked.connect(lambda: self.open_tab(2))
        self.grinding.clicked.connect(lambda: self.open_tab(3))
        self.bullets_station.clicked.connect(lambda: self.open_tab(4))
        self.feed_station.clicked.connect(lambda: self.open_tab(5))
        self.discord_settings.clicked.connect(lambda: self.open_tab(6))

    def open_tab(self, index: int) -> None:
        """Opens ui tab by index."""
        self.tabWidget.setCurrentIndex(index)

    def save(self) -> None:
        with open("settings/settings.json", "w") as f:
            json.dump(self.data, f, indent=4)
