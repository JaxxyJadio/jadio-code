from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QMenu, QAction

class ExplorerMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Layout
        layout = QHBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(4)

        # Buttons
        self.new_file_button = QPushButton("New File")
        self.new_folder_button = QPushButton("New Folder")
        self.refresh_button = QPushButton("Refresh")
        self.collapse_button = QPushButton("Collapse All")
        self.settings_button = QPushButton("Settings")

        # Tools button with dropdown
        self.tools_button = QPushButton("Tools ▼")
        self.tools_menu = QMenu()

        # Example tool scripts
        scripts = [
            "Format Code",
            "Analyze Complexity",
            "Generate Docstring",
            "Minify File",
            "Custom Script"
        ]
        for script in scripts:
            action = QAction(script, self)
            action.triggered.connect(lambda checked, s=script: self.run_tool(s))
            self.tools_menu.addAction(action)

        self.tools_button.setMenu(self.tools_menu)

        # Add widgets to layout
        layout.addWidget(self.new_file_button)
        layout.addWidget(self.new_folder_button)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.collapse_button)
        layout.addWidget(self.settings_button)
        layout.addWidget(self.tools_button)
        layout.addStretch()

        self.setLayout(layout)

    def run_tool(self, script_name):
        print(f"Selected tool: {script_name}")
        # TODO: Here you would add logic to run this script on the selected file
