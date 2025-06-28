from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QPixmap, QPainter
from style import Styles
from style.icons import Icons

class AigentMenu(QWidget):
    """
    Collapsible AIGent menu - starts collapsed, expands to show all buttons
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setFixedHeight(40)
        self.expanded = False

        layout = QHBoxLayout()
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(2)

        self.create_collapsed_layout(layout)
        self.setLayout(layout)

    def create_collapsed_layout(self, layout):
        """Collapsed state with only the toggle button"""
        self.clear_layout(layout)

        self.toggle_button = self.create_icon_button(
            tooltip="Expand AIGent Menu",
            icon_names=Icons.CHAT_NAMES,
            action=self.toggle_menu
        )
        layout.addWidget(self.toggle_button)
        layout.addStretch()

    def create_expanded_layout(self, layout):
        """Expanded state with all action buttons"""
        self.clear_layout(layout)

        self.toggle_button = self.create_icon_button(
            tooltip="Collapse AIGent Menu",
            icon_names=Icons.CHAT_NAMES,
            action=self.toggle_menu
        )
        layout.addWidget(self.toggle_button)

        buttons_config = [
            {
                "tooltip": "Refresh AIGent sessions",
                "icon_names": Icons.REFRESH_NAMES,
                "action": self.handle_refresh
            },
            {
                "tooltip": "Start a new chat",
                "icon_names": Icons.SEND_NAMES,
                "action": self.handle_new_chat
            },
            {
                "tooltip": "View old chat history",
                "icon_names": Icons.MESSAGE_NAMES,
                "action": self.handle_old_chats
            },
            {
                "tooltip": "AIGent Settings",
                "icon_names": Icons.SETTINGS_NAMES,
                "action": self.handle_settings
            },
            {
                "tooltip": "Help & Documentation",
                "icon_names": Icons.INFO_NAMES,
                "action": self.handle_help
            }
        ]

        for config in buttons_config:
            btn = self.create_icon_button(
                tooltip=config["tooltip"],
                icon_names=config["icon_names"],
                action=config["action"]
            )
            layout.addWidget(btn)

        layout.addStretch()

    def create_icon_button(self, tooltip, icon_names, action):
        """Icon-only button using the Icons system"""
        btn = QPushButton()
        btn.setToolTip(tooltip)

        icon_svg = Icons.load_icon(icon_names, tooltip.lower())

        if icon_svg and not icon_svg.startswith('data:'):
            try:
                icon = self.svg_to_qicon(icon_svg)
                btn.setIcon(icon)
                btn.setIconSize(QSize(16, 16))
            except Exception:
                pass

        if action:
            btn.clicked.connect(action)

        return btn

    def svg_to_qicon(self, svg_content):
        """Convert SVG string to QIcon"""
        svg_bytes = svg_content.encode('utf-8')
        renderer = QSvgRenderer(svg_bytes)

        pixmap = QPixmap(16, 16)
        pixmap.fill(Qt.transparent)

        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()

        return QIcon(pixmap)

    def toggle_menu(self):
        """Toggle between collapsed and expanded states"""
        self.expanded = not self.expanded
        layout = self.layout()

        if self.expanded:
            self.create_expanded_layout(layout)
        else:
            self.create_collapsed_layout(layout)

    def clear_layout(self, layout):
        """Remove all widgets from layout"""
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    # Action handlers
    def handle_refresh(self):
        print("Refresh clicked.")

    def handle_new_chat(self):
        print("New Chat clicked.")

    def handle_old_chats(self):
        print("Old Chats clicked.")

    def handle_settings(self):
        print("Settings clicked.")

    def handle_help(self):
        print("Help clicked.")
