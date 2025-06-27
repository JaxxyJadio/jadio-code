from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton

class EditorTopMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(4)

        # Example buttons (placeholders)
        close_button = QPushButton("Close Tab")
        split_button = QPushButton("Split View")
        run_button = QPushButton("Run")
        format_button = QPushButton("Format")

        # Add buttons to layout
        layout.addWidget(close_button)
        layout.addWidget(split_button)
        layout.addWidget(run_button)
        layout.addWidget(format_button)

        # Stretch to fill right side
        layout.addStretch()

        self.setLayout(layout)
