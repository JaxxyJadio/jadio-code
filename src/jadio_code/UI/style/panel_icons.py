# UI/style/panel_icons.py
"""
Sidebar panels and IDE sections icons
"""

from .icon_loader import IconLoader

class PanelIcons(IconLoader):
    """Icons for IDE sidebar panels and sections"""
    
    # =================================================================
    # SIDEBAR PANELS
    # =================================================================
    
    @classmethod
    def explorer(cls): return cls.load_icon("explorer.svg")
    
    @classmethod
    def search_panel(cls): return cls.load_icon("searchpanel.svg")
    
    @classmethod
    def source_control(cls): return cls.load_icon("sourcecontrol.svg")
    
    @classmethod
    def run_debug(cls): return cls.load_icon("rundebug.svg")
    
    @classmethod
    def extensions(cls): return cls.load_icon("extensions.svg")
    
    @classmethod
    def settings(cls): return cls.load_icon("settings.svg")
    
    @classmethod
    def terminal(cls): return cls.load_icon("terminal.svg")
    
    @classmethod
    def problems(cls): return cls.load_icon("problems.svg")
    
    @classmethod
    def output(cls): return cls.load_icon("output.svg")
    
    @classmethod
    def chat(cls): return cls.load_icon("chat.svg")
    
    # =================================================================
    # TERMINAL VARIANTS
    # =================================================================
    
    @classmethod
    def cmd(cls): return cls.load_icon("cmd.svg")
    
    @classmethod
    def powershell(cls): return cls.load_icon("powershell.svg")
    
    @classmethod
    def bash(cls): return cls.load_icon("bash.svg")
    
    @classmethod
    def new_terminal(cls): return cls.load_icon("newterminal.svg")
    
    @classmethod
    def clear_terminal(cls): return cls.load_icon("clearterminal.svg")