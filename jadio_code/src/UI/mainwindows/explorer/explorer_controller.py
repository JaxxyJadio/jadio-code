from PyQt6.QtWidgets import QWidget, QVBoxLayout
from .explorer_menu import ExplorerMenu
from .explorer_sidebar import ExplorerSidebar

class ExplorerController(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Top menu bar
        self.menu = ExplorerMenu()
        layout.addWidget(self.menu)

        # Sidebar file tree
        self.sidebar = ExplorerSidebar()
        layout.addWidget(self.sidebar, stretch=1)

        self.setLayout(layout)
