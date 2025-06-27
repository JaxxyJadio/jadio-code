from PyQt6.QtWidgets import QWidget, QVBoxLayout
from .editor_tabs import EditorTabs
from .editor_topmenu import EditorTopMenu
from .editor_code import EditorCode

class EditorController(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Layout manager for the whole editor
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 1. Tabs at the very top
        self.tabs = EditorTabs()
        layout.addWidget(self.tabs)

        # 2. Top menu bar with split/close/run etc
        self.topmenu = EditorTopMenu()
        layout.addWidget(self.topmenu)

        # 3. Actual code editing area
        self.code_area = EditorCode()
        layout.addWidget(self.code_area, stretch=1)  # Fills most space

        # Apply layout
        self.setLayout(layout)
