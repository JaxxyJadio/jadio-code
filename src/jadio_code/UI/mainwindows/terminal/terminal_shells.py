from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from style.buttons import Buttons

class TerminalShells(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(2)

        for label in ["Shell 1", "Shell 2", "Shell 3"]:
            btn = QPushButton(label)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setFixedHeight(32)
            btn.setFlat(True)
            btn.setCheckable(True)
            layout.addWidget(btn)

        layout.addStretch()
        self.setLayout(layout)

        # Apply your centralized button QSS
        self.setStyleSheet(Buttons.get_button_styles())
