from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QPainter
from PyQt6.QtSvg import QSvgRenderer
from style.colors import Colors
from style.icons import Icons

class AigentSidebar(QWidget):
    """
    VS Code Activity Bar style sidebar – vertical buttons on far right
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(48)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 8, 0, 8)
        layout.setSpacing(0)

        self.buttons = []
        buttons_config = [
            ("Search", Icons.SEARCH_NAMES),
            ("AI Chat", Icons.AI_NAMES),
            ("Settings", Icons.SETTINGS_NAMES),
            ("Plugins", Icons.EXTENSIONS_NAMES),
            ("Analytics", ['chart-bar', 'analytics', 'graph', 'chart', 'trending-up']),
        ]
        for label, icon_names in buttons_config:
            btn = self.create_activity_button(label, icon_names)
            layout.addWidget(btn)
            self.buttons.append(btn)

        layout.addStretch()
        self.setLayout(layout)

        # — removed default selection —
        # if self.buttons:
        #     self.buttons[0].setChecked(True)

    def create_activity_button(self, label, icon_names):
        btn = QPushButton()
        btn.setCheckable(True)
        btn.setToolTip(label)
        btn.clicked.connect(lambda checked, t=label: self.handle_button_click(t))
        btn.setFlat(True)
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                border: none;
            }}
            QPushButton:hover {{
                background-color: {Colors.OVERLAY_LIGHT};
            }}
            QPushButton:checked {{
                background-color: {Colors.OVERLAY_MEDIUM};
            }}
        """)
        svg = Icons.load_icon(icon_names, label.lower())
        if svg and not svg.startswith("data:"):
            if 'currentColor' in svg:
                svg = svg.replace('currentColor', Colors.TEXT_PRIMARY)
            btn.setIcon(self.svg_to_qicon(svg))
            btn.setIconSize(QSize(24, 24))
        else:
            btn.setText(label[0])
        btn.setFixedSize(48, 48)
        return btn

    def svg_to_qicon(self, svg_content: str) -> QIcon:
        data = svg_content.encode('utf-8')
        renderer = QSvgRenderer(data)
        pixmap = QPixmap(24, 24)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        return QIcon(pixmap)

    def handle_button_click(self, button_name):
        print(f"AIGent mode switched to: {button_name}")
        sender = self.sender()
        for btn in self.buttons:
            btn.setChecked(btn == sender)
