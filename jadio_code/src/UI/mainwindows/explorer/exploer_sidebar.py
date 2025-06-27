import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTreeView, QFileDialog
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtCore import QModelIndex, Qt

class ExplorerSidebar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(0)

        # File system model
        self.model = QFileSystemModel()
        self.model.setRootPath(os.path.expanduser("~"))  # Default to home dir

        # Tree view
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(os.path.expanduser("~")))
        self.tree.setHeaderHidden(True)
        self.tree.setAnimated(True)
        self.tree.setIndentation(16)
        self.tree.setSortingEnabled(True)

        # Connect double-click to open file
        self.tree.doubleClicked.connect(self.on_double_click)

        layout.addWidget(self.tree)
        self.setLayout(layout)

    def set_root_path(self, path):
        if os.path.isdir(path):
            self.tree.setRootIndex(self.model.index(path))

    def on_double_click(self, index: QModelIndex):
        path = self.model.filePath(index)
        print(f"Explorer: double-clicked {path}")
        # TODO: hook this to open file in editor
