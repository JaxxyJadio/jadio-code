import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSplitter
from PyQt6.QtCore import Qt

# IMPORT YOUR MODULES
from mainwindows.explorer.explorer_controller import ExplorerController
from mainwindows.editor.editor_controller import EditorController
from mainwindows.terminal.terminal_controller import TerminalController
from mainwindows.code_aigent.aigent_controller import AigentController
from menubar import MenuBar

# IMPORT STYLING
from style import Styles
from style.color_loader import Colors  # <-- THIS is your dynamic loader

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JADIO CODE")
        self.resize(1200, 800)
        self.setMinimumSize(800, 600)

        # Load colors before applying styles
        Colors.load_colors()

        # Set up menu bar
        self.setMenuBar(MenuBar(self))

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        central_widget.setLayout(main_layout)

        # Main Splitter: Explorer | Middle | AIGent
        main_splitter = QSplitter(Qt.Orientation.Horizontal)

        # LEFT: Explorer (narrow vertical sidebar like VS Code)
        explorer = ExplorerController()
        explorer.setFixedWidth(250)
        main_splitter.addWidget(explorer)

        # MIDDLE: Editor + Terminal stack
        middle_widget = QWidget()
        middle_layout = QVBoxLayout()
        middle_layout.setContentsMargins(0, 0, 0, 0)
        middle_layout.setSpacing(0)
        middle_widget.setLayout(middle_layout)

        editor = EditorController()
        middle_layout.addWidget(editor, stretch=4)

        terminal = TerminalController()
        middle_layout.addWidget(terminal, stretch=2)

        main_splitter.addWidget(middle_widget)

        # RIGHT: Code.AIGent panel
        agent_panel = AigentController()
        main_splitter.addWidget(agent_panel)
        main_splitter.setSizes([250, 650, 300])

        # Add splitter to main layout
        main_layout.addWidget(main_splitter)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Ensure colors loaded for Styles
    Colors.load_colors()

    # Apply the complete dark stylesheet
    app.setStyleSheet(Styles.get_complete_stylesheet())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
