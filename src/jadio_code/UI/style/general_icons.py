# UI/style/general_icons.py
"""
General utility and AI icons
"""

from .icon_loader import IconLoader

class GeneralIcons(IconLoader):
    """Icons for general utilities and AI features"""
    
    # =================================================================
    # AI & CHAT
    # =================================================================
    
    @classmethod
    def ai(cls): return cls.load_icon("ai.svg")
    
    @classmethod
    def robot(cls): return cls.load_icon("robot.svg")
    
    @classmethod
    def chat(cls): return cls.load_icon("chat.svg")
    
    @classmethod
    def send(cls): return cls.load_icon("send.svg")
    
    @classmethod
    def mic(cls): return cls.load_icon("mic.svg")
    
    @classmethod
    def mic_off(cls): return cls.load_icon("micoff.svg")
    
    @classmethod
    def brain(cls): return cls.load_icon("brain.svg")
    
    @classmethod
    def sparkles(cls): return cls.load_icon("sparkles.svg")
    
    # =================================================================
    # ESSENTIAL UTILITIES
    # =================================================================
    
    @classmethod
    def home(cls): return cls.load_icon("home.svg")
    
    @classmethod
    def star(cls): return cls.load_icon("star.svg")
    
    @classmethod
    def bookmark(cls): return cls.load_icon("bookmark.svg")
    
    @classmethod
    def pin(cls): return cls.load_icon("pin.svg")
    
    @classmethod
    def lock(cls): return cls.load_icon("lock.svg")
    
    @classmethod
    def unlock(cls): return cls.load_icon("unlock.svg")
    
    @classmethod
    def key(cls): return cls.load_icon("key.svg")
    
    @classmethod
    def shield(cls): return cls.load_icon("shield.svg")
    
    @classmethod
    def user(cls): return cls.load_icon("user.svg")
    
    @classmethod
    def team(cls): return cls.load_icon("team.svg")
    
    @classmethod
    def cloud(cls): return cls.load_icon("cloud.svg")
    
    @classmethod
    def database(cls): return cls.load_icon("database.svg")
    
    @classmethod
    def server(cls): return cls.load_icon("server.svg")
    
    @classmethod
    def network(cls): return cls.load_icon("network.svg")
    
    @classmethod
    def download(cls): return cls.load_icon("download.svg")
    
    @classmethod
    def upload(cls): return cls.load_icon("upload.svg")