from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from code_aigent.aigent_menu import AigentMenu
from code_aigent.topbox.topbox_controller import TopBox
from code_aigent.chatwindow.aigent_chat_controller import ChatWindow
from code_aigent.bottombox.bottombox_controller import BottomBox
from code_aigent.aigent_sidebar import AigentSidebar


class AigentController(QWidget):
    """
    The MASTER container for the entire Code.AIGent right-side panel.
    Always present. Always renders:
        - AigentMenu (top)
        - TopBox
        - ChatWindow
        - BottomBox
        - AigentSidebar (grey vertical buttons)
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        # Top-level horizontal layout: splits main content + sidebar
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ---------------------------------------------
        # LEFT SIDE: MainContent vertical layout
        # ---------------------------------------------
        main_content = QWidget()
        main_content_layout = QVBoxLayout()
        main_content_layout.setContentsMargins(0, 0, 0, 0)
        main_content_layout.setSpacing(0)

        # 1️⃣ AigentMenu (top blue bar)
        self.menu = AigentMenu()
        main_content_layout.addWidget(self.menu)

        # 2️⃣ TopBox (orange section)
        self.topbox = TopBox()
        main_content_layout.addWidget(self.topbox)

        # 3️⃣ ChatWindow (yellow section) - stretchable
        self.chatwindow = ChatWindow()
        main_content_layout.addWidget(self.chatwindow, stretch=1)

        # 4️⃣ BottomBox (blue section)
        self.bottombox = BottomBox()
        main_content_layout.addWidget(self.bottombox)

        main_content.setLayout(main_content_layout)

        # ---------------------------------------------
        # RIGHT SIDE: AigentSidebar (grey button bar)
        # ---------------------------------------------
        self.sidebar = AigentSidebar()

        # Add both to the top-level horizontal layout
        main_layout.addWidget(main_content)
        main_layout.addWidget(self.sidebar)

        self.setLayout(main_layout)
