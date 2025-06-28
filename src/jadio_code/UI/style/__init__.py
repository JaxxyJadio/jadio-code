# UI/styles/__init__.py
"""
JADIO CODE - Modular Styling System
"""

from .colors import Colors
from .fonts import Fonts
from .buttons import Buttons
from .menus import Menus
from .panels import Panels
from .icons import Icons

class Styles:
    """
    Main styles interface - combines all style modules
    """
    
    @classmethod
    def get_complete_stylesheet(cls):
        """Get the complete stylesheet for the entire application"""
        return f"""
        {Fonts.get_font_styles()}
        {Buttons.get_button_styles()}
        {Menus.get_menu_styles()}
        {Panels.get_panel_styles()}
        """
