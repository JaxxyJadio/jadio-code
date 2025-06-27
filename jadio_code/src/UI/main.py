import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSplitter
from PyQt6.QtCore import Qt

# IMPORT YOUR MODULES
from mainwindows.explorer.explorer_controller import ExplorerController
from mainwindows.editor.editor_controller import EditorController
from mainwindows.terminal.terminal_controller import TerminalController
from mainwindows.code_aigent.aigent_controller import AigentController

class JadioMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JADIO CODE")
        self.resize(1200, 800)
        self.setMinimumSize(800, 600)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # Main Splitter: divides Editor stack and AIGent
        main_splitter = QSplitter(Qt.Orientation.Horizontal)

        # -----------------------------------------
        # LEFT SIDE: Editor stack
        # -----------------------------------------
        left_widget = QWidget()
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)
        left_widget.setLayout(left_layout)

        # Explorer at the top
        explorer = ExplorerController()
        left_layout.addWidget(explorer, stretch=1)

        # Editor in the middle
        editor = EditorController()
        left_layout.addWidget(editor, stretch=4)

        # Terminal at the bottom
        terminal = TerminalController()
        left_layout.addWidget(terminal, stretch=2)

        main_splitter.addWidget(left_widget)

        # -----------------------------------------
        # RIGHT SIDE: Code.AIGent panel
        # -----------------------------------------
        agent_panel = AigentController()
        main_splitter.addWidget(agent_panel)
        main_splitter.setSizes([900, 300])

        # Add splitter to main layout
        main_layout.addWidget(main_splitter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JadioMainWindow()
    window.show()
    sys.exit(app.exec())
