from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton

class TerminalMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(4)

        # Example buttons you might want
        self.new_button = QPushButton("New Shell")
        self.kill_button = QPushButton("Kill Shell")
        self.clear_button = QPushButton("Clear")
        self.scroll_lock_button = QPushButton("Scroll Lock")
        self.split_button = QPushButton("Split")
        self.settings_button = QPushButton("Settings")

        # Add them to layout
        layout.addWidget(self.new_button)
        layout.addWidget(self.kill_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.scroll_lock_button)
        layout.addWidget(self.split_button)
        layout.addWidget(self.settings_button)

        layout.addStretch()

        self.setLayout(layout)
