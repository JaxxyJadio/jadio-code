# UI/style/menus.py
"""
JADIO CODE - Menu Styles with JADIO Color System
Menu bars, dropdown menus, context menus, tabs, tree views
"""

from .color_loader import ColorLoader
from .fonts import Fonts

class Menus:
    """Menu and navigation component styles using JADIO signature colors"""
    
    @classmethod
    def get_menu_styles(cls):
        # Load colors using ColorLoader
        get_color = ColorLoader.get_color
        
        return f"""
        /* =================================================================
           MENU BAR & MENUS - JADIO BRANDED
        ================================================================= */
        QMenuBar {{
            background-color: {get_color('jadio_toolbar')};
            color: {get_color('jadio_pearl')};
            border: none;
            border-bottom: 1px solid {get_color('jadio_border')};
            padding: 4px 8px;
            font-family: {Fonts.UI_FONT};
            font-size: {Fonts.SIZE_MEDIUM};
            font-weight: 500;
            spacing: 8px;
        }}
        QMenuBar::item {{
            background-color: transparent;
            padding: 8px 12px;
            margin: 0 2px;
            border-radius: 6px;
            color: {get_color('jadio_pearl')};
        }}
        QMenuBar::item:selected {{
            background-color: {get_color('jadio_hover')};
            color: {get_color('jadio_pure')};
        }}
        QMenuBar::item:pressed {{
            background-color: {get_color('jadio_active')};
            color: {get_color('jadio_pure')};
        }}
        
        /* SEARCH BOX IN MENU BAR */
        QMenuBar QLineEdit {{
            background-color: {get_color('jadio_charcoal')};
            border: 1px solid {get_color('jadio_border')};
            color: {get_color('jadio_pearl')};
            padding: 6px 12px;
            border-radius: 6px;
            min-width: 200px;
            max-width: 300px;
            font-family: {Fonts.UI_FONT};
            font-size: {Fonts.SIZE_NORMAL};
            margin: 2px 8px;
        }}
        QMenuBar QLineEdit:focus {{
            border: 1px solid {get_color('jadio_crimson')};
            background-color: {get_color('jadio_carbon')};
            color: {get_color('jadio_pure')};
        }}
        QMenuBar QLineEdit::placeholder {{
            color: {get_color('jadio_steel')};
        }}
        
        /* DROPDOWN MENUS */
        QMenu {{
            background-color: {get_color('jadio_panel')};
            color: {get_color('jadio_pearl')};
            border: 1px solid {get_color('jadio_border')};
            padding: 8px 4px;
            font-family: {Fonts.UI_FONT};
            font-size: {Fonts.SIZE_NORMAL};
            border-radius: 8px;
        }}
        QMenu::item {{
            background-color: transparent;
            padding: 8px 24px 8px 16px;
            margin: 1px 4px;
            border-radius: 6px;
            min-width: 150px;
            color: {get_color('jadio_pearl')};
        }}
        QMenu::item:selected {{
            background-color: {get_color('jadio_crimson')};
            color: {get_color('jadio_pure')};
        }}
        QMenu::item:disabled {{
            color: {get_color('jadio_disabled')};
            background-color: transparent;
        }}
        QMenu::separator {{
            height: 1px;
            background-color: {get_color('jadio_divider')};
            margin: 4px 8px;
        }}
        QMenu::icon {{
            padding-left: 8px;
        }}
        
        /* CONTEXT MENUS */
        QMenu[class="context"] {{
            background-color: {get_color('jadio_panel')};
            border: 1px solid {get_color('jadio_border_light')};
            border-radius: 8px;
            padding: 6px 2px;
        }}
        QMenu[class="context"]::item {{
            padding: 6px 20px 6px 12px;
            margin: 1px 2px;
            border-radius: 4px;
        }}
        QMenu[class="context"]::item:selected {{
            background-color: {get_color('jadio_crimson')};
        }}
        
        /* =================================================================
           TABS - MODERN JADIO DESIGN
        ================================================================= */
        QTabWidget {{
            background-color: {get_color('jadio_midnight')};
            border: none;
        }}
        QTabWidget::pane {{
            background-color: {get_color('jadio_midnight')};
            border: 1px solid {get_color('jadio_border')};
            border-top: none;
            border-radius: 0px 0px 6px 6px;
        }}
        QTabWidget::tab-bar {{
            alignment: left;
        }}
        
        QTabBar {{
            background-color: {get_color('jadio_charcoal')};
            border: none;
            qproperty-drawBase: 0;
            font-family: {Fonts.UI_FONT};
        }}
        QTabBar::tab {{
            background-color: {get_color('jadio_charcoal')};
            color: {get_color('jadio_silver')};
            padding: 10px 20px;
            margin-right: 2px;
            border: 1px solid {get_color('jadio_border')};
            border-bottom: none;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
            min-width: 100px;
            font-size: {Fonts.SIZE_NORMAL};
            font-weight: 500;
        }}
        QTabBar::tab:selected {{
            background-color: {get_color('jadio_midnight')};
            color: {get_color('jadio_pure')};
            border-bottom: 2px solid {get_color('jadio_crimson')};
            border-left: 1px solid {get_color('jadio_border')};
            border-right: 1px solid {get_color('jadio_border')};
            border-top: 1px solid {get_color('jadio_border')};
            font-weight: 600;
        }}
        QTabBar::tab:hover:!selected {{
            background-color: {get_color('jadio_hover')};
            color: {get_color('jadio_pearl')};
        }}
        QTabBar::tab:!selected {{
            margin-top: 2px;
            background-color: {get_color('jadio_graphite')};
        }}
        
        /* TAB CLOSE BUTTONS */
        QTabBar::close-button {{
            image: none;
            background-color: transparent;
            border: none;
            padding: 2px;
            margin: 2px;
            border-radius: 3px;
            width: 16px;
            height: 16px;
        }}
        QTabBar::close-button:hover {{
            background-color: {get_color('jadio_error')};
            border-radius: 3px;
        }}
        QTabBar::close-button:pressed {{
            background-color: {get_color('jadio_cherry')};
        }}
        
        /* TAB SCROLL BUTTONS */
        QTabBar QToolButton {{
            background-color: {get_color('jadio_charcoal')};
            border: 1px solid {get_color('jadio_border')};
            border-radius: 4px;
            padding: 2px;
        }}
        QTabBar QToolButton:hover {{
            background-color: {get_color('jadio_hover')};
        }}
        
        /* =================================================================
           TREE VIEW (FILE EXPLORER) - JADIO STYLED
        ================================================================= */
        QTreeView {{
            background-color: {get_color('jadio_panel')};
            border: none;
            outline: none;
            color: {get_color('jadio_pearl')};
            font-family: {Fonts.UI_FONT};
            font-size: {Fonts.SIZE_NORMAL};
            alternate-background-color: {get_color('jadio_charcoal')};
            show-decoration-selected: 1;
            gridline-color: {get_color('jadio_border_dark')};
        }}
        QTreeView::item {{
            padding: 6px 8px;
            border: none;
            min-height: 28px;
            background-color: transparent;
            border-radius: 4px;
            margin: 1px 2px;
        }}
        QTreeView::item:hover {{
            background-color: {get_color('jadio_hover')};
            color: {get_color('jadio_pure')};
        }}
        QTreeView::item:selected {{
            background-color: {get_color('jadio_crimson')};
            color: {get_color('jadio_pure')};
        }}
        QTreeView::item:selected:active {{
            background-color: {get_color('jadio_crimson')};
        }}
        QTreeView::item:selected:!active {{
            background-color: {get_color('jadio_ruby')};
        }}
        
        /* TREE BRANCHES & EXPANSION */
        QTreeView::branch {{
            background-color: transparent;
        }}
        QTreeView::branch:has-siblings:!adjoins-item {{
            border-image: none;
            border: none;
        }}
        QTreeView::branch:has-siblings:adjoins-item {{
            border-image: none;
            border: none;
        }}
        QTreeView::branch:!has-children:!has-siblings:adjoins-item {{
            border-image: none;
            border: none;
        }}
        QTreeView::branch:has-children:!has-siblings:closed,
        QTreeView::branch:closed:has-children:has-siblings {{
            background-color: transparent;
            border: none;
        }}
        QTreeView::branch:open:has-children:!has-siblings,
        QTreeView::branch:open:has-children:has-siblings {{
            background-color: transparent;
            border: none;
        }}
        
        /* TREE HEADER */
        QTreeView QHeaderView::section {{
            background-color: {get_color('jadio_toolbar')};
            color: {get_color('jadio_pearl')};
            padding: 8px 4px;
            border: none;
            border-bottom: 1px solid {get_color('jadio_border')};
            border-right: 1px solid {get_color('jadio_border_dark')};
            font-weight: 600;
            font-family: {Fonts.UI_FONT};
        }}
        QTreeView QHeaderView::section:hover {{
            background-color: {get_color('jadio_hover')};
        }}
        
        /* =================================================================
           LIST VIEW - SIMILAR TO TREE VIEW
        ================================================================= */
        QListView {{
            background-color: {get_color('jadio_panel')};
            border: none;
            outline: none;
            color: {get_color('jadio_pearl')};
            font-family: {Fonts.UI_FONT};
            font-size: {Fonts.SIZE_NORMAL};
            alternate-background-color: {get_color('jadio_charcoal')};
        }}
        QListView::item {{
            padding: 8px 12px;
            border: none;
            min-height: 24px;
            background-color: transparent;
            border-radius: 4px;
            margin: 1px 2px;
        }}
        QListView::item:hover {{
            background-color: {get_color('jadio_hover')};
            color: {get_color('jadio_pure')};
        }}
        QListView::item:selected {{
            background-color: {get_color('jadio_crimson')};
            color: {get_color('jadio_pure')};
        }}
        QListView::item:selected:active {{
            background-color: {get_color('jadio_crimson')};
        }}
        QListView::item:selected:!active {{
            background-color: {get_color('jadio_ruby')};
        }}
        
        /* =================================================================
           TABLE VIEW - DATA TABLES
        ================================================================= */
        QTableView {{
            background-color: {get_color('jadio_midnight')};
            alternate-background-color: {get_color('jadio_charcoal')};
            color: {get_color('jadio_pearl')};
            gridline-color: {get_color('jadio_border_dark')};
            selection-background-color: {get_color('jadio_crimson')};
            selection-color: {get_color('jadio_pure')};
            border: 1px solid {get_color('jadio_border')};
            font-family: {Fonts.UI_FONT};
        }}
        QTableView::item {{
            padding: 6px 8px;
            border: none;
        }}
        QTableView::item:hover {{
            background-color: {get_color('jadio_hover')};
        }}
        QTableView::item:selected {{
            background-color: {get_color('jadio_crimson')};
            color: {get_color('jadio_pure')};
        }}
        QTableView QHeaderView::section {{
            background-color: {get_color('jadio_toolbar')};
            color: {get_color('jadio_pearl')};
            padding: 8px 4px;
            border: none;
            border-bottom: 1px solid {get_color('jadio_border')};
            border-right: 1px solid {get_color('jadio_border_dark')};
            font-weight: 600;
        }}
        QTableView QHeaderView::section:hover {{
            background-color: {get_color('jadio_hover')};
        }}
        """