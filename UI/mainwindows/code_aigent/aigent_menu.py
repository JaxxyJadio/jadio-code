from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt6.QtCore import QSize


class AigentMenu(QWidget):
    """
    The top light-blue bar of the AIGENT panel.
    Always present. Contains session and chat controls.
    Example buttons:
    - Refresh Chat
    - New Chat
    - Old Chats
    - Settings
    - Help
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Overall horizontal layout
        layout = QHBoxLayout()
        layout.setContentsMargins(4, 2, 4, 2)
        layout.setSpacing(6)

        # Define example buttons
        buttons = [
            ("Refresh", self.handle_refresh),
            ("New Chat", self.handle_new_chat),
            ("Old Chats", self.handle_old_chats),
            ("Settings", self.handle_settings),
            ("Help", self.handle_help)
        ]

        for label, slot in buttons:
            btn = QPushButton(label)
            btn.setMinimumHeight(32)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #007acc;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    padding: 4px 8px;
                }
                QPushButton:hover {
                    background-color: #3399ff;
                }
            """)
            btn.clicked.connect(slot)
            layout.addWidget(btn)

        layout.addStretch()

        self.setLayout(layout)
        self.setFixedHeight(40)  # Fixed height for consistent top bar

    # Example signal handlers
    def handle_refresh(self):
        print("Refresh button clicked.")

    def handle_new_chat(self):
        print("New Chat button clicked.")

    def handle_old_chats(self):
        print("Old Chats button clicked.")

    def handle_settings(self):
        print("Settings button clicked.")

    def handle_help(self):
        print("Help button clicked.")
