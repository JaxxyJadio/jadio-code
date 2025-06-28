# UI/styles/fonts.py
"""
JADIO CODE - Font Definitions
Typography and font styles
"""

from .colors import Colors

class Fonts:
    """Font definitions and base typography styles"""
    
    # ========================================
    # FONT FAMILIES
    # ========================================
    UI_FONT = "'Segoe UI', 'Roboto', 'Arial', sans-serif"
    CODE_FONT = "'Consolas', 'Monaco', 'Courier New', monospace"
    HEADING_FONT = "'Segoe UI Semibold', 'Roboto Medium', 'Arial', sans-serif"
    DISPLAY_FONT = "'Segoe UI Light', 'Roboto Light', 'Arial', sans-serif"
    MONO_FONT = "'JetBrains Mono', 'Fira Code', 'Source Code Pro', 'Consolas', monospace"
    
    # ========================================
    # FONT SIZES
    # ========================================
    SIZE_TINY = '9px'           # Very small text
    SIZE_SMALL = '11px'         # Small text, captions
    SIZE_NORMAL = '13px'        # Default text size
    SIZE_MEDIUM = '14px'        # Medium text
    SIZE_LARGE = '16px'         # Large text
    SIZE_HEADING = '18px'       # Headings
    SIZE_TITLE = '20px'         # Titles
    SIZE_DISPLAY = '24px'       # Display text
    SIZE_HUGE = '32px'          # Very large text
    
    # ========================================
    # FONT WEIGHTS
    # ========================================
    WEIGHT_THIN = '100'
    WEIGHT_LIGHT = '300'
    WEIGHT_NORMAL = '400'
    WEIGHT_MEDIUM = '500'
    WEIGHT_SEMIBOLD = '600'
    WEIGHT_BOLD = '700'
    WEIGHT_BLACK = '900'
    
    # ========================================
    # LINE HEIGHTS
    # ========================================
    LINE_HEIGHT_TIGHT = '1.2'
    LINE_HEIGHT_NORMAL = '1.4'
    LINE_HEIGHT_LOOSE = '1.6'
    LINE_HEIGHT_CODE = '1.5'
    
    @classmethod
    def get_font_styles(cls):
        return f"""
        /* =================================================================
           BASE APPLICATION & TYPOGRAPHY
        ================================================================= */
        QApplication {{
            background-color: {Colors.BG_PRIMARY};
            color: {Colors.TEXT_PRIMARY};
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_NORMAL};
            font-weight: {cls.WEIGHT_NORMAL};
            selection-background-color: {Colors.SELECTED};
            selection-color: {Colors.TEXT_PRIMARY};
        }}
        
        QMainWindow {{
            background-color: {Colors.BG_PRIMARY};
            color: {Colors.TEXT_PRIMARY};
            border: none;
            font-family: {cls.UI_FONT};
        }}
        
        QWidget {{
            background-color: {Colors.BG_PRIMARY};
            color: {Colors.TEXT_PRIMARY};
            border: none;
            outline: none;
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_NORMAL};
            font-weight: {cls.WEIGHT_NORMAL};
        }}
        
        /* =================================================================
           LABEL TYPOGRAPHY
        ================================================================= */
        QLabel {{
            background-color: transparent;
            color: {Colors.TEXT_PRIMARY};
            border: none;
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_NORMAL};
            font-weight: {cls.WEIGHT_NORMAL};
        }}
        
        /* Label Variants */
        QLabel[class="tiny"] {{
            font-size: {cls.SIZE_TINY};
            color: {Colors.TEXT_MUTED};
        }}
        QLabel[class="small"] {{
            font-size: {cls.SIZE_SMALL};
            color: {Colors.TEXT_SECONDARY};
        }}
        QLabel[class="secondary"] {{
            color: {Colors.TEXT_SECONDARY};
        }}
        QLabel[class="tertiary"] {{
            color: {Colors.TEXT_TERTIARY};
        }}
        QLabel[class="muted"] {{
            color: {Colors.TEXT_MUTED};
            font-size: {cls.SIZE_SMALL};
        }}
        QLabel[class="disabled"] {{
            color: {Colors.TEXT_DISABLED};
        }}
        QLabel[class="accent"] {{
            color: {Colors.TEXT_ACCENT};
            font-weight: {cls.WEIGHT_SEMIBOLD};
        }}
        QLabel[class="link"] {{
            color: {Colors.TEXT_LINK};
            text-decoration: underline;
        }}
        
        /* Heading Variants */
        QLabel[class="heading"] {{
            font-family: {cls.HEADING_FONT};
            font-size: {cls.SIZE_HEADING};
            font-weight: {cls.WEIGHT_SEMIBOLD};
            color: {Colors.TEXT_PRIMARY};
        }}
        QLabel[class="title"] {{
            font-family: {cls.HEADING_FONT};
            font-size: {cls.SIZE_TITLE};
            font-weight: {cls.WEIGHT_BOLD};
            color: {Colors.TEXT_PRIMARY};
        }}
        QLabel[class="display"] {{
            font-family: {cls.DISPLAY_FONT};
            font-size: {cls.SIZE_DISPLAY};
            font-weight: {cls.WEIGHT_LIGHT};
            color: {Colors.TEXT_PRIMARY};
        }}
        
        /* Code Labels */
        QLabel[class="code"] {{
            font-family: {cls.CODE_FONT};
            font-size: {cls.SIZE_SMALL};
            background-color: {Colors.BG_TERTIARY};
            padding: 2px 4px;
            border-radius: 2px;
        }}
        QLabel[class="mono"] {{
            font-family: {cls.MONO_FONT};
        }}
        
        /* Weight Variants */
        QLabel[class="light"] {{
            font-weight: {cls.WEIGHT_LIGHT};
        }}
        QLabel[class="medium"] {{
            font-weight: {cls.WEIGHT_MEDIUM};
        }}
        QLabel[class="semibold"] {{
            font-weight: {cls.WEIGHT_SEMIBOLD};
        }}
        QLabel[class="bold"] {{
            font-weight: {cls.WEIGHT_BOLD};
        }}
        
        /* =================================================================
           CODE & EDITOR TYPOGRAPHY
        ================================================================= */
        QTextEdit[class="code"], QPlainTextEdit[class="code"] {{
            font-family: {cls.CODE_FONT};
            font-size: {cls.SIZE_NORMAL};
            line-height: {cls.LINE_HEIGHT_CODE};
        }}
        
        QTextEdit[class="mono"], QPlainTextEdit[class="mono"] {{
            font-family: {cls.MONO_FONT};
            font-size: {cls.SIZE_NORMAL};
            line-height: {cls.LINE_HEIGHT_CODE};
        }}
        
        /* Terminal specific */
        QWidget[objectName="terminal"] {{
            font-family: {cls.CODE_FONT};
            font-size: {cls.SIZE_NORMAL};
            font-weight: {cls.WEIGHT_NORMAL};
            line-height: {cls.LINE_HEIGHT_CODE};
        }}
        
        /* Editor specific */
        QWidget[objectName="editor"] {{
            font-family: {cls.CODE_FONT};
            font-size: {cls.SIZE_NORMAL};
            line-height: {cls.LINE_HEIGHT_CODE};
        }}
        
        /* =================================================================
           INPUT TYPOGRAPHY
        ================================================================= */
        QLineEdit {{
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_NORMAL};
            font-weight: {cls.WEIGHT_NORMAL};
        }}
        
        QLineEdit[class="code"] {{
            font-family: {cls.CODE_FONT};
        }}
        
        QTextEdit, QPlainTextEdit {{
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_NORMAL};
            line-height: {cls.LINE_HEIGHT_NORMAL};
        }}
        
        /* =================================================================
           BUTTON TYPOGRAPHY
        ================================================================= */
        QPushButton {{
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_NORMAL};
            font-weight: {cls.WEIGHT_MEDIUM};
        }}
        
        QPushButton[class="small"] {{
            font-size: {cls.SIZE_SMALL};
            font-weight: {cls.WEIGHT_NORMAL};
        }}
        
        QPushButton[class="large"] {{
            font-size: {cls.SIZE_MEDIUM};
            font-weight: {cls.WEIGHT_SEMIBOLD};
        }}
        
        /* =================================================================
           MENU TYPOGRAPHY
        ================================================================= */
        QMenuBar {{
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_MEDIUM};
            font-weight: {cls.WEIGHT_MEDIUM};
        }}
        
        QMenu {{
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_NORMAL};
            font-weight: {cls.WEIGHT_NORMAL};
        }}
        
        QTabBar {{
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_NORMAL};
            font-weight: {cls.WEIGHT_NORMAL};
        }}
        
        QTabBar::tab:selected {{
            font-weight: {cls.WEIGHT_MEDIUM};
        }}
        
        /* =================================================================
           STATUS & TOOLBAR TYPOGRAPHY
        ================================================================= */
        QStatusBar {{
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_SMALL};
            font-weight: {cls.WEIGHT_NORMAL};
        }}
        
        QToolBar {{
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_NORMAL};
            font-weight: {cls.WEIGHT_NORMAL};
        }}
        
        /* =================================================================
           TOOLTIPS & DIALOGS
        ================================================================= */
        QToolTip {{
            background-color: {Colors.BG_TOOLTIP};
            color: {Colors.TEXT_PRIMARY};
            border: 1px solid {Colors.BORDER_PRIMARY};
            padding: 6px 8px;
            border-radius: 4px;
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_SMALL};
            font-weight: {cls.WEIGHT_NORMAL};
        }}
        
        QDialog {{
            background-color: {Colors.BG_PRIMARY};
            color: {Colors.TEXT_PRIMARY};
            border: 1px solid {Colors.BORDER_PRIMARY};
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_NORMAL};
        }}
        
        QMessageBox {{
            background-color: {Colors.BG_PRIMARY};
            color: {Colors.TEXT_PRIMARY};
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_NORMAL};
        }}
        
        /* =================================================================
           TREE VIEWS & LISTS
        ================================================================= */
        QTreeView {{
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_NORMAL};
            font-weight: {cls.WEIGHT_NORMAL};
        }}
        
        QListView {{
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_NORMAL};
            font-weight: {cls.WEIGHT_NORMAL};
        }}
        
        QComboBox {{
            font-family: {cls.UI_FONT};
            font-size: {cls.SIZE_NORMAL};
            font-weight: {cls.WEIGHT_NORMAL};
        }}
        """