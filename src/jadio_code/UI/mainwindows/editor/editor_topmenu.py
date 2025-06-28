from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QPixmap, QPainter
from PyQt6.QtSvg import QSvgRenderer
from style.colors import Colors
from style.icons import Icons

class EditorTopMenu(QWidget):
    """
    Horizontal editor menu – icons are 20×20 with 2px gutters, total height 24px,
    and use white translucent overlays on hover/pressed.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(24)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(2)
        self.setLayout(layout)

        buttons_config = [
            ("Close Tab", Icons.CLOSE_TAB_NAMES),
            ("Split View", Icons.SPLIT_HORIZONTAL_NAMES),
            ("Run", Icons.RUN_NAMES),
            ("Format", Icons.FORMAT_NAMES),
        ]

        for tooltip, icon_names in buttons_config:
            btn = self.create_icon_button(tooltip, icon_names)
            layout.addWidget(btn)

        layout.addStretch()

    def create_icon_button(self, tooltip: str, icon_names) -> QPushButton:
        btn = QPushButton()
        btn.setToolTip(tooltip)
        btn.setFlat(True)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setFixedSize(24, 24)
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                border: none;
                padding: 0;
                margin: 0;
            }}
            QPushButton:hover {{
                background-color: rgba(255, 255, 255, 0.1);
            }}
            QPushButton:pressed {{
                background-color: rgba(255, 255, 255, 0.2);
            }}
        """)

        svg = Icons.load_icon(icon_names, tooltip.lower())
        if svg and not svg.startswith("data:"):
            if 'currentColor' in svg:
                svg = svg.replace('currentColor', Colors.TEXT_PRIMARY)
            btn.setIcon(self.svg_to_qicon(svg))
            btn.setIconSize(QSize(20, 20))

        return btn

    def svg_to_qicon(self, svg_content: str) -> QIcon:
        data = svg_content.encode('utf-8')
        renderer = QSvgRenderer(data)
        pixmap = QPixmap(20, 20)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        return QIcon(pixmap)
