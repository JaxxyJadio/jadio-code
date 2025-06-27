from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLineEdit, QLabel

class BottomBox(QWidget):
    """
    The BLUE section (BottomBox).
    MINI TERMINAL + Input area.
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(6)

        # MINI TERMINAL STRIP
        self.mini_terminal = QLabel("Mini Terminal / Current Context")
        self.mini_terminal.setStyleSheet("background-color: #111; color: #eee; padding: 4px;")

        layout.addWidget(self.mini_terminal)

        # INPUT AREA
        input_row = QHBoxLayout()
        input_row.setSpacing(4)

        self.expand_button = QPushButton("Expand Terminal")
        self.model_button = QPushButton("Hot-Swap Model")
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Start typing...")
        self.send_button = QPushButton("Send")

        input_row.addWidget(self.expand_button)
        input_row.addWidget(self.model_button)
        input_row.addWidget(self.input_field, stretch=1)
        input_row.addWidget(self.send_button)

        layout.addLayout(input_row)

        self.setLayout(layout)
