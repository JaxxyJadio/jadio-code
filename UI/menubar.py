from PyQt6.QtWidgets import QMenuBar, QMenu, QAction, QLineEdit, QWidgetAction

class AppMenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Define top-level menu names exactly as your diagram
        top_menus = [
            "File", "Edit", "Selection", "LAN", "LLM",
            "JADIONET", "Code Doctor", "Plugins", "Settings", "Help"
        ]

        for menu_name in top_menus:
            menu = QMenu(menu_name, self)
            # Add 10 placeholder items to each menu
            for i in range(1, 11):
                action = QAction(f"{menu_name} Option {i}", self)
                # Connect all actions to a no-op lambda for now
                action.triggered.connect(lambda checked, name=menu_name, idx=i: print(f"Selected: {name} Option {idx}"))
                menu.addAction(action)
            self.addMenu(menu)

        # Add search box on the far right
        search_action = QWidgetAction(self)
        search_field = QLineEdit()
        search_field.setPlaceholderText("Search...")
        search_action.setDefaultWidget(search_field)
        self.addAction(search_action)
