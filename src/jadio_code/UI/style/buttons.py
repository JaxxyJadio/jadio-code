# UI/style/buttons.py
"""
JADIO Code Button Component Styles - Fixed to use ColorLoader
"""

from .color_loader import ColorLoader
from .fonts import Fonts

class Buttons:
    """Button component styles using JADIO signature colors via ColorLoader"""
    
    @classmethod
    def get_button_styles(cls):
        # Load colors using ColorLoader
        get_color = ColorLoader.get_color
        
        return f"""
        /* =================================================================
           BUTTONS - CORE STYLES WITH JADIO COLORS
        ================================================================= */
        QPushButton {{
            background-color: {get_color('jadio_charcoal')};
            border: 1px solid {get_color('jadio_border')};
            color: {get_color('jadio_pearl')};
            font-family: {Fonts.UI_FONT};
            font-size: {Fonts.SIZE_NORMAL};
            font-weight: 500;
            padding: 8px 16px;
            min-height: 28px;
            border-radius: 6px;
            text-align: center;
        }}
        
        QPushButton:hover {{
            background-color: {get_color('jadio_hover')};
            border: 1px solid {get_color('jadio_crimson')};
            color: {get_color('jadio_pure')};
        }}
        
        QPushButton:pressed {{
            background-color: {get_color('jadio_active')};
            border: 1px solid {get_color('jadio_crimson')};
            color: {get_color('jadio_pure')};
        }}
        
        QPushButton:checked {{
            background-color: {get_color('jadio_crimson')};
            border: 1px solid {get_color('jadio_crimson')};
            color: {get_color('jadio_pure')};
        }}
        
        QPushButton:disabled {{
            background-color: {get_color('jadio_graphite')};
            color: {get_color('jadio_disabled')};
            border: 1px solid {get_color('jadio_border_dark')};
        }}
        
        QPushButton:default {{
            background-color: {get_color('jadio_electric')};
            border: 1px solid {get_color('jadio_electric')};
            color: {get_color('jadio_pure')};
            font-weight: 600;
        }}
        
        QPushButton:default:hover {{
            background-color: {get_color('jadio_azure')};
            border: 1px solid {get_color('jadio_azure')};
        }}
        
        /* =================================================================
           ICON BUTTONS - SIDEBAR AND TOOLBAR
        ================================================================= */
        QPushButton[class="icon"],
        QPushButton[class="sidebar"],
        QPushButton[class="toolbar"] {{
            background-color: transparent;
            border: none;
            padding: 6px;
            margin: 2px;
            min-width: 32px;
            max-width: 32px;
            min-height: 32px;
            max-height: 32px;
            border-radius: 6px;
            color: {get_color('jadio_silver')};
        }}
        
        QPushButton[class="icon"]:hover,
        QPushButton[class="sidebar"]:hover,
        QPushButton[class="toolbar"]:hover {{
            background-color: {get_color('jadio_hover')};
            color: {get_color('jadio_pure')};
        }}
        
        QPushButton[class="icon"]:pressed,
        QPushButton[class="sidebar"]:pressed,
        QPushButton[class="toolbar"]:pressed {{
            background-color: {get_color('jadio_active')};
            color: {get_color('jadio_pure')};
        }}
        
        QPushButton[class="icon"]:checked,
        QPushButton[class="sidebar"]:checked,
        QPushButton[class="toolbar"]:checked {{
            background-color: {get_color('jadio_crimson')};
            color: {get_color('jadio_pure')};
        }}
        
        /* =================================================================
           BUTTON VARIANTS - JADIO STYLED
        ================================================================= */
        
        /* Flat Buttons */
        QPushButton[flat="true"] {{
            background-color: transparent;
            border: none;
            padding: 8px 16px;
            color: {get_color('jadio_pearl')};
            border-radius: 6px;
        }}
        
        QPushButton[flat="true"]:hover {{
            background-color: {get_color('jadio_hover')};
            color: {get_color('jadio_pure')};
        }}
        
        QPushButton[flat="true"]:pressed {{
            background-color: {get_color('jadio_active')};
        }}
        
        /* Size Variants */
        QPushButton[class="small"] {{
            font-size: {Fonts.SIZE_SMALL};
            padding: 4px 12px;
            min-height: 24px;
            border-radius: 4px;
        }}
        
        QPushButton[class="small"]:hover {{
            background-color: {get_color('jadio_hover')};
            border-color: {get_color('jadio_crimson')};
        }}
        
        QPushButton[class="large"] {{
            font-size: {Fonts.SIZE_MEDIUM};
            padding: 12px 24px;
            min-height: 40px;
            font-weight: 600;
            border-radius: 8px;
        }}
        
        QPushButton[class="large"]:hover {{
            background-color: {get_color('jadio_hover')};
            border-color: {get_color('jadio_crimson')};
        }}
        
        QPushButton[class="compact"] {{
            padding: 4px 12px;
            min-height: 24px;
            font-size: {Fonts.SIZE_SMALL};
            border-radius: 4px;
        }}
        
        QPushButton[class="compact"]:hover {{
            background-color: {get_color('jadio_hover')};
            border-color: {get_color('jadio_crimson')};
        }}
        
        /* Menu Buttons */
        QPushButton[class="menu"] {{
            background-color: transparent;
            border: none;
            text-align: left;
            padding: 8px 12px;
            border-radius: 6px;
            color: {get_color('jadio_pearl')};
        }}
        
        QPushButton[class="menu"]:hover {{
            background-color: {get_color('jadio_hover')};
            color: {get_color('jadio_pure')};
        }}
        
        QPushButton[class="menu"]:pressed {{
            background-color: {get_color('jadio_active')};
        }}
        
        /* =================================================================
           SEMANTIC BUTTONS - STATUS COLORS
        ================================================================= */
        
        /* Success Button */
        QPushButton[class="success"] {{
            background-color: {get_color('jadio_success')};
            border: 1px solid {get_color('jadio_success')};
            color: {get_color('jadio_pure')};
        }}
        
        QPushButton[class="success"]:hover {{
            background-color: {get_color('jadio_forest')};
            border-color: {get_color('jadio_forest')};
        }}
        
        /* Warning Button */
        QPushButton[class="warning"] {{
            background-color: {get_color('jadio_warning')};
            border: 1px solid {get_color('jadio_warning')};
            color: {get_color('jadio_void')};
        }}
        
        QPushButton[class="warning"]:hover {{
            background-color: {get_color('jadio_amber')};
            border-color: {get_color('jadio_amber')};
        }}
        
        /* Error/Danger Button */
        QPushButton[class="danger"],
        QPushButton[class="error"] {{
            background-color: {get_color('jadio_error')};
            border: 1px solid {get_color('jadio_error')};
            color: {get_color('jadio_pure')};
        }}
        
        QPushButton[class="danger"]:hover,
        QPushButton[class="error"]:hover {{
            background-color: {get_color('jadio_cherry')};
            border-color: {get_color('jadio_cherry')};
        }}
        
        /* Info Button */
        QPushButton[class="info"] {{
            background-color: {get_color('jadio_info')};
            border: 1px solid {get_color('jadio_info')};
            color: {get_color('jadio_pure')};
        }}
        
        QPushButton[class="info"]:hover {{
            background-color: {get_color('jadio_azure')};
            border-color: {get_color('jadio_azure')};
        }}
        
        /* =================================================================
           STYLE VARIANTS
        ================================================================= */
        
        /* Ghost Button */
        QPushButton[class="ghost"] {{
            background-color: transparent;
            border: 1px solid {get_color('jadio_border')};
            color: {get_color('jadio_pearl')};
        }}
        
        QPushButton[class="ghost"]:hover {{
            background-color: {get_color('jadio_hover')};
            border-color: {get_color('jadio_crimson')};
            color: {get_color('jadio_pure')};
        }}
        
        /* Minimal Button */
        QPushButton[class="minimal"] {{
            background-color: transparent;
            border: none;
            color: {get_color('jadio_pearl')};
            padding: 6px 12px;
            border-radius: 4px;
        }}
        
        QPushButton[class="minimal"]:hover {{
            background-color: {get_color('jadio_hover')};
            color: {get_color('jadio_pure')};
        }}
        
        /* Rounded Button */
        QPushButton[class="rounded"] {{
            border-radius: 20px;
            padding: 8px 20px;
        }}
        
        QPushButton[class="rounded"]:hover {{
            background-color: {get_color('jadio_hover')};
            border-color: {get_color('jadio_crimson')};
        }}
        
        /* Toggle Button */
        QPushButton[class="toggle"] {{
            background-color: {get_color('jadio_charcoal')};
            border: 1px solid {get_color('jadio_border')};
            color: {get_color('jadio_pearl')};
        }}
        
        QPushButton[class="toggle"]:hover {{
            background-color: {get_color('jadio_hover')};
            border-color: {get_color('jadio_crimson')};
        }}
        
        QPushButton[class="toggle"]:checked {{
            background-color: {get_color('jadio_electric')};
            border: 1px solid {get_color('jadio_electric')};
            color: {get_color('jadio_pure')};
        }}
        
        /* =================================================================
           SPECIAL BUTTONS - IDE SPECIFIC
        ================================================================= */
        
        /* Primary Action Button */
        QPushButton[class="primary"] {{
            background-color: {get_color('jadio_crimson')};
            border: 1px solid {get_color('jadio_crimson')};
            color: {get_color('jadio_pure')};
            font-weight: 600;
        }}
        
        QPushButton[class="primary"]:hover {{
            background-color: {get_color('jadio_ruby')};
            border-color: {get_color('jadio_ruby')};
        }}
        
        /* Secondary Action Button */
        QPushButton[class="secondary"] {{
            background-color: {get_color('jadio_electric')};
            border: 1px solid {get_color('jadio_electric')};
            color: {get_color('jadio_pure')};
        }}
        
        QPushButton[class="secondary"]:hover {{
            background-color: {get_color('jadio_azure')};
            border-color: {get_color('jadio_azure')};
        }}
        
        /* Accent Button */
        QPushButton[class="accent"] {{
            background-color: {get_color('jadio_gold')};
            border: 1px solid {get_color('jadio_gold')};
            color: {get_color('jadio_void')};
            font-weight: 600;
        }}
        
        QPushButton[class="accent"]:hover {{
            background-color: {get_color('jadio_amber')};
            border-color: {get_color('jadio_amber')};
        }}
        
        /* Toolbar Separator (not a button, but related) */
        QToolBar::separator {{
            background: {get_color('jadio_divider')};
            width: 1px;
            height: 1px;
            margin: 2px;
        }}
        """