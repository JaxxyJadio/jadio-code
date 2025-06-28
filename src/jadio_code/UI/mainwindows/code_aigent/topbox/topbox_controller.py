from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget
from .topbox_modelsettings import TopboxModelSettings
from .topbox_lan import TopboxLan
from .topbox_tools import TopboxTools
from .topbox_context import TopboxContext


class TopBox(QWidget):
    """
    The TopBox with text buttons and proper width
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Overall vertical layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # -------------------------------
        # 1️⃣ Button bar (tab selector) with text labels
        # -------------------------------
        button_bar = QHBoxLayout()
        button_bar.setContentsMargins(4, 4, 4, 4)
        button_bar.setSpacing(4)

        self.buttons = []

        # Text buttons instead of emojis
        sections = [
            ("Model", 0),    # AI Model Settings
            ("LAN", 1),      # LAN Settings  
            ("Tools", 2),    # Tools
            ("Context", 3)   # Context
        ]

        for label, index in sections:
            btn = QPushButton(label)
            btn.setCheckable(True)
            btn.clicked.connect(lambda checked, i=index: self.show_panel(i))
            button_bar.addWidget(btn)
            self.buttons.append(btn)

        # Don't stretch - keep buttons compact
        button_bar.addStretch()

        # -------------------------------
        # 2️⃣ Stacked widget for panels
        # -------------------------------
        self.stack = QStackedWidget()
        self.stack.addWidget(TopboxModelSettings())
        self.stack.addWidget(TopboxLan())
        self.stack.addWidget(TopboxTools())
        self.stack.addWidget(TopboxContext())

        # Default selection
        self.buttons[0].setChecked(True)
        self.stack.setCurrentIndex(0)

        # Add to main layout
        layout.addLayout(button_bar)
        layout.addWidget(self.stack)

        self.setLayout(layout)

    def show_panel(self, index):
        # Update stacked widget
        self.stack.setCurrentIndex(index)
        # Update button states
        for i, btn in enumerate(self.buttons):
            btn.setChecked(i == index)