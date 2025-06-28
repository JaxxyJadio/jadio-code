from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QPixmap, QPainter
from PyQt6.QtSvg import QSvgRenderer
from style.icons import Icons
from style.buttons import Buttons

class TerminalMenu(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(2)

        buttons_config = [
            {"tooltip": "New Terminal",   "icon_names": Icons.NEW_SHELL_NAMES,     "action": self.new_shell},
            {"tooltip": "Kill Terminal",  "icon_names": Icons.KILL_SHELL_NAMES,    "action": self.kill_shell},
            {"tooltip": "Clear",          "icon_names": Icons.CLEAR_TERMINAL_NAMES,"action": self.clear_terminal},
            {"tooltip": "Scroll Lock",    "icon_names": Icons.SCROLL_LOCK_NAMES,   "action": self.toggle_scroll_lock},
            {"tooltip": "Split",          "icon_names": Icons.SPLIT_HORIZONTAL_NAMES,"action": self.split_terminal},
            {"tooltip": "Settings",       "icon_names": Icons.SETTINGS_NAMES,      "action": self.open_settings},
        ]

        for cfg in buttons_config:
            btn = self.create_icon_button(cfg["tooltip"], cfg["icon_names"])
            btn.clicked.connect(cfg["action"])
            btn.setProperty("class", "toolbar")
            layout.addWidget(btn)

        layout.addStretch()
        self.setLayout(layout)

        # apply centralized styles
        self.setStyleSheet(Buttons.get_button_styles())

    def create_icon_button(self, tooltip, icon_names):
        btn = QPushButton()
        btn.setToolTip(tooltip)
        btn.setFlat(True)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setFixedSize(36, 36)

        svg = Icons.load_icon(icon_names, tooltip.lower())
        if svg and not svg.startswith("data:"):
            btn.setIcon(self.svg_to_qicon(svg, Qt.GlobalColor.transparent))
            btn.setIconSize(QSize(20, 20))

        return btn

    def svg_to_qicon(self, svg_content, transparent_color):
        # tint currentColor to your primary text via centralized QSS,
        # so here just render as-is
        data = svg_content.encode("utf-8")
        renderer = QSvgRenderer(data)

        pixmap = QPixmap(20, 20)
        pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        return QIcon(pixmap)

    # Placeholder actions
    def new_shell(self):             pass
    def kill_shell(self):            pass
    def clear_terminal(self):        pass
    def toggle_scroll_lock(self):    pass
    def split_terminal(self):        pass
    def open_settings(self):         pass
