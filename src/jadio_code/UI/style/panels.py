# UI/style/panels.py
"""
JADIO CODE - Panel Styles with JADIO Color System
Layout, splitters, input fields, scrollbars, and all other components
"""

from .color_loader import ColorLoader
from .fonts import Fonts

class Panels:
    """Panel and layout component styles using JADIO signature colors"""
    
    @classmethod
    def get_panel_styles(cls):
        # Load colors using ColorLoader
        get_color = ColorLoader.get_color
        
        return f"""
        /* =================================================================
           SPLITTERS & LAYOUT - JADIO STYLED
        ================================================================= */
        QSplitter {{
            background-color: {get_color('jadio_midnight')};
            border: none;
        }}
        QSplitter::handle {{
            background-color: {get_color('jadio_border')};
            border: none;
        }}
        QSplitter::handle:horizontal {{
            width: 2px;
            margin: 2px 0;
        }}
        QSplitter::handle:vertical {{
            height: 2px;
            margin: 0 2px;
        }}
        QSplitter::handle:hover {{
            background-color: {get_color('jadio_crimson')};
        }}
        QSplitter::handle:pressed {{
            background-color: {get_color('jadio_electric')};
        }}
        
        /* =================================================================
           INPUT FIELDS - JADIO THEMED
        ================================================================= */
        QLineEdit {{
            background-color: {get_color('jadio_charcoal')};
            border: 1px solid {get_color('jadio_border')};
            color: {get_color('jadio_pearl')};
            padding: 8px 12px;
            font-family: {Fonts.CODE_FONT};
            font-size: {Fonts.SIZE_NORMAL};
            border-radius: 6px;
            selection-background-color: {get_color('jadio_electric')};
        }}
        QLineEdit:focus {{
            border: 1px solid {get_color('jadio_crimson')};
            background-color: {get_color('jadio_carbon')};
            color: {get_color('jadio_pure')};
        }}
        QLineEdit:disabled {{
            background-color: {get_color('jadio_graphite')};
            color: {get_color('jadio_disabled')};
            border: 1px solid {get_color('jadio_border_dark')};
        }}
        QLineEdit::placeholder {{
            color: {get_color('jadio_steel')};
        }}
        
        /* TEXT EDIT AREAS */
        QTextEdit, QPlainTextEdit {{
            background-color: {get_color('jadio_charcoal')};
            border: 1px solid {get_color('jadio_border')};
            color: {get_color('jadio_pearl')};
            padding: 8px;
            font-family: {Fonts.CODE_FONT};
            font-size: {Fonts.SIZE_NORMAL};
            border-radius: 6px;
            selection-background-color: {get_color('jadio_electric')};
        }}
        QTextEdit:focus, QPlainTextEdit:focus {{
            border: 1px solid {get_color('jadio_crimson')};
            background-color: {get_color('jadio_carbon')};
            color: {get_color('jadio_pure')};
        }}
        QTextEdit::placeholder, QPlainTextEdit::placeholder {{
            color: {get_color('jadio_steel')};
        }}
        
        /* =================================================================
           SCROLLBARS - JADIO DESIGN
        ================================================================= */
        /* VERTICAL SCROLLBAR */
        QScrollBar:vertical {{
            background-color: {get_color('jadio_obsidian')};
            width: 12px;
            border: none;
            margin: 0;
            border-radius: 6px;
        }}
        QScrollBar::handle:vertical {{
            background-color: {get_color('jadio_hover')};
            border-radius: 6px;
            min-height: 20px;
            margin: 2px;
        }}
        QScrollBar::handle:vertical:hover {{
            background-color: {get_color('jadio_active')};
        }}
        QScrollBar::handle:vertical:pressed {{
            background-color: {get_color('jadio_crimson')};
        }}
        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {{
            height: 0px;
            background: none;
            border: none;
        }}
        QScrollBar::add-page:vertical,
        QScrollBar::sub-page:vertical {{
            background: none;
        }}
        
        /* HORIZONTAL SCROLLBAR */
        QScrollBar:horizontal {{
            background-color: {get_color('jadio_obsidian')};
            height: 12px;
            border: none;
            margin: 0;
            border-radius: 6px;
        }}
        QScrollBar::handle:horizontal {{
            background-color: {get_color('jadio_hover')};
            border-radius: 6px;
            min-width: 20px;
            margin: 2px;
        }}
        QScrollBar::handle:horizontal:hover {{
            background-color: {get_color('jadio_active')};
        }}
        QScrollBar::handle:horizontal:pressed {{
            background-color: {get_color('jadio_crimson')};
        }}
        QScrollBar::add-line:horizontal,
        QScrollBar::sub-line:horizontal {{
            width: 0px;
            background: none;
            border: none;
        }}
        QScrollBar::add-page:horizontal,
        QScrollBar::sub-page:horizontal {{
            background: none;
        }}
        
        /* =================================================================
           TOOLBARS & STATUS BARS - JADIO BRANDING
        ================================================================= */
        QToolBar {{
            background-color: {get_color('jadio_toolbar')};
            border: none;
            border-bottom: 1px solid {get_color('jadio_border')};
            padding: 4px;
            spacing: 6px;
            font-family: {Fonts.UI_FONT};
            color: {get_color('jadio_pearl')};
        }}
        QToolBar::separator {{
            width: 1px;
            background-color: {get_color('jadio_divider')};
            margin: 4px 8px;
        }}
        
        QStatusBar {{
            background-color: {get_color('jadio_statusbar')};
            color: {get_color('jadio_pearl')};
            border: none;
            border-top: 1px solid {get_color('jadio_border')};
            padding: 4px 8px;
            font-family: {Fonts.UI_FONT};
            font-weight: 500;
        }}
        QStatusBar::item {{
            border: none;
        }}
        
        /* =================================================================
           COMBO BOXES & DROPDOWNS - JADIO STYLED
        ================================================================= */
        QComboBox {{
            background-color: {get_color('jadio_charcoal')};
            border: 1px solid {get_color('jadio_border')};
            color: {get_color('jadio_pearl')};
            padding: 6px 12px;
            border-radius: 6px;
            min-width: 80px;
            font-family: {Fonts.UI_FONT};
            font-size: {Fonts.SIZE_NORMAL};
        }}
        QComboBox:hover {{
            border: 1px solid {get_color('jadio_crimson')};
            background-color: {get_color('jadio_hover')};
        }}
        QComboBox:focus {{
            border: 1px solid {get_color('jadio_electric')};
            background-color: {get_color('jadio_carbon')};
        }}
        QComboBox::drop-down {{
            border: none;
            width: 20px;
            background-color: transparent;
        }}
        QComboBox::down-arrow {{
            image: none;
            border: none;
            width: 0px;
            height: 0px;
        }}
        QComboBox QAbstractItemView {{
            background-color: {get_color('jadio_panel')};
            border: 1px solid {get_color('jadio_border')};
            selection-background-color: {get_color('jadio_crimson')};
            color: {get_color('jadio_pearl')};
            outline: none;
            font-family: {Fonts.UI_FONT};
            border-radius: 6px;
            padding: 4px;
        }}
        QComboBox QAbstractItemView::item {{
            padding: 6px 12px;
            border-radius: 4px;
        }}
        QComboBox QAbstractItemView::item:hover {{
            background-color: {get_color('jadio_hover')};
        }}
        QComboBox QAbstractItemView::item:selected {{
            background-color: {get_color('jadio_crimson')};
            color: {get_color('jadio_pure')};
        }}
        
        /* =================================================================
           CHECK BOXES & RADIO BUTTONS - JADIO DESIGN
        ================================================================= */
        QCheckBox {{
            color: {get_color('jadio_pearl')};
            spacing: 8px;
            font-family: {Fonts.UI_FONT};
        }}
        QCheckBox::indicator {{
            width: 16px;
            height: 16px;
            border: 1px solid {get_color('jadio_border')};
            border-radius: 4px;
            background-color: {get_color('jadio_charcoal')};
        }}
        QCheckBox::indicator:hover {{
            border: 1px solid {get_color('jadio_crimson')};
            background-color: {get_color('jadio_hover')};
        }}
        QCheckBox::indicator:checked {{
            background-color: {get_color('jadio_crimson')};
            border: 1px solid {get_color('jadio_crimson')};
        }}
        QCheckBox::indicator:checked:hover {{
            background-color: {get_color('jadio_ruby')};
            border: 1px solid {get_color('jadio_ruby')};
        }}
        QCheckBox:disabled {{
            color: {get_color('jadio_disabled')};
        }}
        QCheckBox::indicator:disabled {{
            background-color: {get_color('jadio_graphite')};
            border: 1px solid {get_color('jadio_border_dark')};
        }}
        
        QRadioButton {{
            color: {get_color('jadio_pearl')};
            spacing: 8px;
            font-family: {Fonts.UI_FONT};
        }}
        QRadioButton::indicator {{
            width: 16px;
            height: 16px;
            border: 1px solid {get_color('jadio_border')};
            border-radius: 8px;
            background-color: {get_color('jadio_charcoal')};
        }}
        QRadioButton::indicator:hover {{
            border: 1px solid {get_color('jadio_crimson')};
            background-color: {get_color('jadio_hover')};
        }}
        QRadioButton::indicator:checked {{
            background-color: {get_color('jadio_crimson')};
            border: 1px solid {get_color('jadio_crimson')};
        }}
        QRadioButton::indicator:checked:hover {{
            background-color: {get_color('jadio_ruby')};
            border: 1px solid {get_color('jadio_ruby')};
        }}
        QRadioButton:disabled {{
            color: {get_color('jadio_disabled')};
        }}
        QRadioButton::indicator:disabled {{
            background-color: {get_color('jadio_graphite')};
            border: 1px solid {get_color('jadio_border_dark')};
        }}
        
        /* =================================================================
           PROGRESS BARS & SLIDERS - JADIO BRANDING
        ================================================================= */
        QProgressBar {{
            background-color: {get_color('jadio_charcoal')};
            border: 1px solid {get_color('jadio_border')};
            border-radius: 6px;
            text-align: center;
            color: {get_color('jadio_pearl')};
            font-family: {Fonts.UI_FONT};
            font-weight: 600;
            padding: 2px;
        }}
        QProgressBar::chunk {{
            background-color: {get_color('jadio_crimson')};
            border-radius: 4px;
        }}
        QProgressBar[value="100"]::chunk {{
            background-color: {get_color('jadio_success')};
        }}
        
        QSlider::groove:horizontal {{
            background-color: {get_color('jadio_charcoal')};
            height: 6px;
            border-radius: 3px;
            border: 1px solid {get_color('jadio_border')};
        }}
        QSlider::handle:horizontal {{
            background-color: {get_color('jadio_crimson')};
            width: 18px;
            height: 18px;
            border-radius: 9px;
            margin: -6px 0;
            border: 2px solid {get_color('jadio_pure')};
        }}
        QSlider::handle:horizontal:hover {{
            background-color: {get_color('jadio_ruby')};
        }}
        QSlider::handle:horizontal:pressed {{
            background-color: {get_color('jadio_cherry')};
        }}
        
        /* =================================================================
           SPECIFIC COMPONENT OVERRIDES - IDE SECTIONS
        ================================================================= */
        
        /* TERMINAL SPECIFIC */
        QWidget[objectName="terminal"] {{
            background-color: {get_color('jadio_void')};
            color: {get_color('jadio_term_white')};
            font-family: {Fonts.CODE_FONT};
            border: 1px solid {get_color('jadio_border_dark')};
        }}
        
        /* EDITOR SPECIFIC */
        QWidget[objectName="editor"] {{
            background-color: {get_color('jadio_midnight')};
            color: {get_color('jadio_pearl')};
            font-family: {Fonts.CODE_FONT};
            border: none;
        }}
        
        /* SIDEBAR SPECIFIC */
        QWidget[objectName="sidebar"] {{
            background-color: {get_color('jadio_sidebar')};
            border-right: 1px solid {get_color('jadio_border')};
            min-width: 48px;
            max-width: 48px;
        }}
        
        /* AIGENT SPECIFIC */
        QWidget[objectName="aigent"] {{
            background-color: {get_color('jadio_panel')};
            border-left: 1px solid {get_color('jadio_border')};
            color: {get_color('jadio_pearl')};
        }}
        
        /* FILE EXPLORER */
        QWidget[objectName="explorer"] {{
            background-color: {get_color('jadio_panel')};
            color: {get_color('jadio_pearl')};
        }}
        
        /* SEARCH PANEL */
        QWidget[objectName="search"] {{
            background-color: {get_color('jadio_panel')};
            color: {get_color('jadio_pearl')};
        }}
        
        /* SOURCE CONTROL */
        QWidget[objectName="git"] {{
            background-color: {get_color('jadio_panel')};
            color: {get_color('jadio_pearl')};
        }}
        
        /* EXTENSIONS PANEL */
        QWidget[objectName="extensions"] {{
            background-color: {get_color('jadio_panel')};
            color: {get_color('jadio_pearl')};
        }}
        
        /* SETTINGS PANEL */
        QWidget[objectName="settings"] {{
            background-color: {get_color('jadio_panel')};
            color: {get_color('jadio_pearl')};
        }}
        
        /* =================================================================
           ADVANCED UI ELEMENTS
        ================================================================= */
        
        /* TABS */
        QTabWidget::pane {{
            border: 1px solid {get_color('jadio_border')};
            background-color: {get_color('jadio_midnight')};
        }}
        QTabBar::tab {{
            background-color: {get_color('jadio_charcoal')};
            color: {get_color('jadio_silver')};
            padding: 8px 16px;
            margin-right: 2px;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
        }}
        QTabBar::tab:selected {{
            background-color: {get_color('jadio_midnight')};
            color: {get_color('jadio_pure')};
            border-bottom: 2px solid {get_color('jadio_crimson')};
        }}
        QTabBar::tab:hover:!selected {{
            background-color: {get_color('jadio_hover')};
            color: {get_color('jadio_pearl')};
        }}
        
        /* MENUS */
        QMenu {{
            background-color: {get_color('jadio_panel')};
            border: 1px solid {get_color('jadio_border')};
            color: {get_color('jadio_pearl')};
            padding: 4px;
            border-radius: 6px;
        }}
        QMenu::item {{
            padding: 8px 16px;
            border-radius: 4px;
        }}
        QMenu::item:selected {{
            background-color: {get_color('jadio_crimson')};
            color: {get_color('jadio_pure')};
        }}
        QMenu::separator {{
            height: 1px;
            background-color: {get_color('jadio_divider')};
            margin: 4px 8px;
        }}
        """