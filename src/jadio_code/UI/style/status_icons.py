# UI/style/status_icons.py
"""
Status and notification icons
"""

from .icon_loader import IconLoader

class StatusIcons(IconLoader):
    """Icons for status and notifications"""
    
    # =================================================================
    # STATUS INDICATORS
    # =================================================================
    
    @classmethod
    def success(cls): return cls.load_icon("success.svg")
    
    @classmethod
    def warning(cls): return cls.load_icon("warning.svg")
    
    @classmethod
    def error(cls): return cls.load_icon("error.svg")
    
    @classmethod
    def info(cls): return cls.load_icon("info.svg")
    
    @classmethod
    def loading(cls): return cls.load_icon("loading.svg")
    
    @classmethod
    def pending(cls): return cls.load_icon("pending.svg")
    
    @classmethod
    def check(cls): return cls.load_icon("check.svg")
    
    @classmethod
    def alert(cls): return cls.load_icon("alert.svg")
    
    # =================================================================
    # NOTIFICATIONS
    # =================================================================
    
    @classmethod
    def notification(cls): return cls.load_icon("notification.svg")
    
    @classmethod
    def bell(cls): return cls.load_icon("bell.svg")