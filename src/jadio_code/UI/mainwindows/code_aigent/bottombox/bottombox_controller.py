from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt6.QtCore import Qt, QSize
from style.colors import Colors

class BottomBox(QWidget):
    """
    BottomBox with cohesive dark theme styling
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumHeight(200)
        self.setMaximumHeight(300)

        layout = QVBoxLayout()
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)

        # Top: Mini Terminal / Current Context
        self.mini_terminal = QLabel("Mini Terminal / Current Context")
        self.mini_terminal.setFixedHeight(32)
        self.mini_terminal.setStyleSheet(f"""
            QLabel {{
                background-color: {Colors.BG_SECONDARY};
                color: {Colors.TEXT_PRIMARY};
                padding: 6px 12px;
                border-radius: 4px;
            }}
        """)
        layout.addWidget(self.mini_terminal)

        # Main: Input + side buttons
        input_main = QWidget()
        input_layout = QHBoxLayout()
        input_layout.setContentsMargins(0, 0, 0, 0)
        input_layout.setSpacing(8)

        # Text area
        self.input_area = QTextEdit()
        self.input_area.setPlaceholderText("Start typing here...")
        self.input_area.setMinimumHeight(120)
        self.input_area.setStyleSheet(f"""
            QTextEdit {{
                background-color: {Colors.BG_INPUT};
                color: {Colors.TEXT_PRIMARY};
                border: 1px solid {Colors.BORDER_PRIMARY};
                border-radius: 4px;
                padding: 8px;
            }}
            QTextEdit[placeholderText="true"] {{
                color: {Colors.TEXT_MUTED};
            }}
        """)

        # Side buttons
        right_side = QWidget()
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(4)

        button_style = f"""
            QPushButton {{
                background-color: transparent;
                color: {Colors.TEXT_PRIMARY};
                border: 1px solid {Colors.BORDER_PRIMARY};
                padding: 6px 8px;
                border-radius: 4px;
                text-align: center;
            }}
            QPushButton:hover {{
                background-color: {Colors.ERROR_LIGHT};
                border: 1px solid {Colors.ERROR};
            }}
            QPushButton:pressed {{
                background-color: {Colors.ERROR_DARK};
                border: 1px solid {Colors.ERROR_DARK};
            }}
        """

        self.expand_button = QPushButton("Expand\nTerminal")
        self.expand_button.setFixedHeight(50)
        self.expand_button.setStyleSheet(button_style)

        self.model_button = QPushButton("Change\nModel")
        self.model_button.setFixedHeight(50)
        self.model_button.setStyleSheet(button_style)

        right_layout.addWidget(self.expand_button)
        right_layout.addWidget(self.model_button)
        right_layout.addStretch()

        self.send_button = QPushButton("Send")
        self.send_button.setFixedHeight(40)
        self.send_button.setStyleSheet(button_style)
        right_layout.addWidget(self.send_button)

        right_side.setLayout(right_layout)
        right_side.setFixedWidth(100)

        input_layout.addWidget(self.input_area, stretch=1)
        input_layout.addWidget(right_side)
        input_main.setLayout(input_layout)

        layout.addWidget(input_main, stretch=1)
        self.setLayout(layout)

        # Signals
        self.send_button.clicked.connect(self.handle_send)
        self.expand_button.clicked.connect(self.handle_expand_terminal)
        self.model_button.clicked.connect(self.handle_model_swap)

    def handle_send(self):
        text = self.input_area.toPlainText().strip()
        if text:
            print(f"Sending: {text}")
            self.input_area.clear()

    def handle_expand_terminal(self):
        print("Expand Terminal clicked - should shrink chat window")

    def handle_model_swap(self):
        print("Change Model clicked - should open model selection")
