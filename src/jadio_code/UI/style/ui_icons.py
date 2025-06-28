# UI/style/ui_icons.py
"""
UI controls and navigation icons
"""

from .icon_loader import IconLoader

class UIIcons(IconLoader):
    """Icons for UI controls and navigation"""
    
    # =================================================================
    # NAVIGATION
    # =================================================================
    
    @classmethod
    def chevron_right(cls): return cls.load_icon("chevronright.svg")
    
    @classmethod
    def chevron_down(cls): return cls.load_icon("chevrondown.svg")
    
    @classmethod
    def chevron_left(cls): return cls.load_icon("chevronleft.svg")
    
    @classmethod
    def chevron_up(cls): return cls.load_icon("chevronup.svg")
    
    @classmethod
    def arrow_right(cls): return cls.load_icon("arrowright.svg")
    
    @classmethod
    def arrow_left(cls): return cls.load_icon("arrowleft.svg")
    
    @classmethod
    def arrow_up(cls): return cls.load_icon("arrowup.svg")
    
    @classmethod
    def arrow_down(cls): return cls.load_icon("arrowdown.svg")
    
    # =================================================================
    # WINDOW CONTROLS
    # =================================================================
    
    @classmethod
    def close(cls): return cls.load_icon("close.svg")
    
    @classmethod
    def minimize(cls): return cls.load_icon("minimize.svg")
    
    @classmethod
    def maximize(cls): return cls.load_icon("maximize.svg")
    
    @classmethod
    def restore(cls): return cls.load_icon("restore.svg")
    
    # =================================================================
    # BASIC ACTIONS
    # =================================================================
    
    @classmethod
    def plus(cls): return cls.load_icon("plus.svg")
    
    @classmethod
    def minus(cls): return cls.load_icon("minus.svg")
    
    @classmethod
    def expand(cls): return cls.load_icon("expand.svg")
    
    @classmethod
    def collapse(cls): return cls.load_icon("collapse.svg")
    
    @classmethod
    def refresh(cls): return cls.load_icon("refresh.svg")
    
    @classmethod
    def search(cls): return cls.load_icon("search.svg")
    
    @classmethod
    def filter(cls): return cls.load_icon("filter.svg")
    
    @classmethod
    def sort(cls): return cls.load_icon("sort.svg")
    
    # =================================================================
    # MENU/LAYOUT
    # =================================================================
    
    @classmethod
    def menu(cls): return cls.load_icon("menu.svg")
    
    @classmethod
    def grid(cls): return cls.load_icon("grid.svg")
    
    @classmethod
    def list(cls): return cls.load_icon("list.svg")
    
    @classmethod
    def split_horizontal(cls): return cls.load_icon("splithorizontal.svg")
    
    @classmethod
    def split_vertical(cls): return cls.load_icon("splitvertical.svg")
    
    @classmethod
    def fullscreen(cls): return cls.load_icon("fullscreen.svg")