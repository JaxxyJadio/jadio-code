from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QPixmap, QPainter
from PyQt6.QtSvg import QSvgRenderer
from style.icons import Icons
from style.buttons import Buttons

class ExplorerSidebar(QWidget):
    """
    Vertical, icon-only, VS Code-style sidebar for Explorer - left side
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(48)

        layout = QVBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(2)

        self.buttons = []
        buttons_config = [
            ("Files",      Icons.EXPLORER_NAMES),
            ("Search",     Icons.SEARCH_PANEL_NAMES),
            ("Git",        Icons.SOURCE_CONTROL_NAMES),
            ("Debug",      Icons.RUN_DEBUG_NAMES),
            ("Extensions", Icons.EXTENSIONS_NAMES),
        ]

        for tooltip, icon_names in buttons_config:
            btn = self.create_icon_button(tooltip, icon_names)
            btn.setCheckable(True)
            btn.setProperty("class", "sidebar")
            btn.clicked.connect(lambda checked, t=tooltip: self.handle_button_click(t))
            layout.addWidget(btn)
            self.buttons.append(btn)

        layout.addStretch()
        self.setLayout(layout)

        # Do not set any button checked by default
        # Apply centralized QSS
        self.setStyleSheet(Buttons.get_button_styles())

    def create_icon_button(self, tooltip, icon_names):
        btn = QPushButton()
        btn.setToolTip(tooltip)
        btn.setFlat(True)
        btn.setText("")

        svg = Icons.load_icon(icon_names, tooltip.lower())
        if svg and not svg.startswith("data:"):
            btn.setIcon(self.svg_to_qicon(svg))
            btn.setIconSize(QSize(20, 20))

        btn.setFixedSize(44, 44)
        return btn

    def svg_to_qicon(self, svg_content: str) -> QIcon:
        data = svg_content.encode("utf-8")
        renderer = QSvgRenderer(data)

        pixmap = QPixmap(24, 24)
        pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        return QIcon(pixmap)

    def handle_button_click(self, button_name):
        sender = self.sender()
        for btn in self.buttons:
            btn.setChecked(btn is sender)
        print(f"ExplorerSidebar clicked: {button_name}")
