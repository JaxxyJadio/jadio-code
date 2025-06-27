from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSplitter
from PyQt6.QtCore import Qt
from .terminal_menu import TerminalMenu
from .terminal_window import TerminalWindow
from .terminal_shells import TerminalShells

class TerminalController(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Overall vertical layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Top bar
        self.menu = TerminalMenu()
        layout.addWidget(self.menu)

        # Splitter for CLI and shell list
        splitter = QSplitter(Qt.Orientation.Horizontal)

        self.window = TerminalWindow()
        self.shells = TerminalShells()

        splitter.addWidget(self.window)
        splitter.addWidget(self.shells)
        splitter.setSizes([800, 200])

        layout.addWidget(splitter)

        self.setLayout(layout)
