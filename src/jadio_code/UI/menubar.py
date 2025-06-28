from PyQt6.QtWidgets import QMenuBar, QMenu, QLineEdit, QWidgetAction
from PyQt6.QtGui import QAction

class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Professional menu structure
        top_menus = [
            "File", "Edit", "Selection", "LAN", "LLM",
            "JADIONET", "Code Doctor", "Plugins", "Settings", "Help"
        ]

        for menu_name in top_menus:
            menu = QMenu(menu_name, self)
            # Add professional menu items with separators
            for i in range(1, 11):
                action = QAction(f"{menu_name} Option {i}", self)
                action.triggered.connect(lambda checked, name=menu_name, idx=i: print(f"Selected: {name} Option {idx}"))
                menu.addAction(action)
                
                # Add separators for better organization
                if i == 3 or i == 7:
                    menu.addSeparator()
                    
            self.addMenu(menu)

        # Professional search box on the far right
        search_action = QWidgetAction(self)
        search_field = QLineEdit()
        search_field.setPlaceholderText("Search commands...")
        search_action.setDefaultWidget(search_field)
        self.addAction(search_action)