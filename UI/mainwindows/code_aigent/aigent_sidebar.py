from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import QSize


class AigentSidebar(QWidget):
    """
    The vertical grey sidebar attached on the far right of AIGENT.
    Always rendered. Fixed width. Contains vertical stack of buttons.
    Mirrors VS Code's Activity Bar but on the right.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Overall vertical layout for stacked buttons
        layout = QVBoxLayout()
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(8)

        # Create 5 placeholder buttons for now
        self.buttons = []
        for i in range(1, 6):
            btn = QPushButton(f"Btn {i}")
            btn.setFixedHeight(40)
            btn.setMinimumWidth(40)
            btn.setMaximumWidth(50)
            btn.setCheckable(True)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #333;
                    color: #eee;
                    border: none;
                    border-radius: 4px;
                }
                QPushButton:checked {
                    background-color: #555;
                }
            """)
            layout.addWidget(btn)
            self.buttons.append(btn)

        # Stretch to keep them top-aligned
        layout.addStretch()

        self.setLayout(layout)

        # Set fixed width for the sidebar itself
        self.setMinimumWidth(50)
        self.setMaximumWidth(60)

        # Example signal connections placeholder
        # btn.clicked.connect(lambda: self.handleButton(i))
        # Define handleButton() later to switch modes, etc.

