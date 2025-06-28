from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QPainter
from PyQt6.QtSvg import QSvgRenderer
from style.colors import Colors
from style.icons import Icons

class ExplorerMenu(QWidget):
    """
    Collapsible horizontal menu for Explorer – buttons are exactly icon-sized (20×20) with 2px gutters,
    and use the same red hover/pressed colors as the sidebar.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(24)
        self.expanded = False

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(2, 2, 2, 2)
        self.layout.setSpacing(2)

        self.create_collapsed_layout()

    def create_collapsed_layout(self):
        self._clear_layout()
        btn = self._make_button(Icons.chevron_down(), "Expand")
        btn.clicked.connect(self.toggle_menu)
        self.layout.addWidget(btn)
        self.layout.addStretch()

    def create_expanded_layout(self):
        self._clear_layout()
        toggle = self._make_button(Icons.chevron_up(), "Collapse")
        toggle.clicked.connect(self.toggle_menu)
        self.layout.addWidget(toggle)

        for tip, svg in [
            ("New File",   Icons.new_file()),
            ("New Folder", Icons.new_folder()),
            ("Refresh",    Icons.refresh()),
            ("Collapse",   Icons.load_icon(Icons.COLLAPSE_NAMES, "collapse")),
            ("Settings",   Icons.settings()),
        ]:
            b = self._make_button(svg, tip)
            self.layout.addWidget(b)

        self.layout.addStretch()

    def toggle_menu(self):
        self.expanded = not self.expanded
        if self.expanded:
            self.create_expanded_layout()
        else:
            self.create_collapsed_layout()

    def _make_button(self, svg_content: str, tooltip: str) -> QPushButton:
        btn = QPushButton()
        btn.setToolTip(tooltip)
        btn.setFlat(True)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setFixedSize(20, 20)
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                border: none;
                padding: 0;
                margin: 2px;
                min-width: 20px; max-width: 20px;
                min-height: 20px; max-height: 20px;
            }}
            QPushButton:hover {{
                background-color: rgba(255, 0, 0, 0.16);
            }}
            QPushButton:pressed {{
                background-color: rgba(255, 0, 0, 0.32);
            }}
        """)
        btn.setIcon(self._svg_to_qicon(svg_content, Colors.TEXT_PRIMARY))
        btn.setIconSize(QSize(20, 20))
        return btn

    def _svg_to_qicon(self, svg_content: str, color: str) -> QIcon:
        if 'currentColor' in svg_content:
            svg_content = svg_content.replace('currentColor', color)
        data = svg_content.encode('utf-8')
        renderer = QSvgRenderer(data)
        pix = QPixmap(20, 20)
        pix.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pix)
        renderer.render(painter)
        painter.end()
        return QIcon(pix)

    def _clear_layout(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()
