from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget
from code_aigent.topbox.topbox_modelsettings import TopboxModelSettings
from code_aigent.topbox.topbox_lan import TopboxLan
from code_aigent.topbox.topbox_tools import TopboxTools
from code_aigent.topbox.topbox_context import TopboxContext


class TopBox(QWidget):
    """
    The ORANGE section of Code.AIGent.
    Contains:
      - AI_MODEL_SETTINGS
      - LAN_SETTINGS
      - AI_TOOL_SET
      - LONG_CONTEXT
    Shows only ONE of these at a time.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Overall vertical layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # -------------------------------
        # 1️⃣ Button bar (tab selector)
        # -------------------------------
        button_bar = QHBoxLayout()
        button_bar.setContentsMargins(4, 4, 4, 4)
        button_bar.setSpacing(6)

        self.buttons = []

        sections = [
            ("Model Settings", 0),
            ("LAN Settings", 1),
            ("Tools", 2),
            ("Context", 3)
        ]

        for label, index in sections:
            btn = QPushButton(label)
            btn.setCheckable(True)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    border: none;
                    padding: 4px 8px;
                    border-radius: 4px;
                }
                QPushButton:checked {
                    background-color: #007acc;
                }
            """)
            btn.clicked.connect(lambda checked, i=index: self.show_panel(i))
            button_bar.addWidget(btn)
            self.buttons.append(btn)

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
