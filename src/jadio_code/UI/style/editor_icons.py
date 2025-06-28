# UI/style/editor_icons.py
"""
Editor operations and IDE functionality icons
"""

from .icon_loader import IconLoader

class EditorIcons(IconLoader):
    """Icons for editor operations and IDE functionality"""
    
    # =================================================================
    # FILE OPERATIONS
    # =================================================================
    
    @classmethod
    def new_file(cls): return cls.load_icon("newfile.svg")
    
    @classmethod
    def new_folder(cls): return cls.load_icon("newfolder.svg")
    
    @classmethod
    def open(cls): return cls.load_icon("open.svg")
    
    @classmethod
    def save(cls): return cls.load_icon("save.svg")
    
    @classmethod
    def save_as(cls): return cls.load_icon("saveas.svg")
    
    @classmethod
    def save_all(cls): return cls.load_icon("saveall.svg")
    
    @classmethod
    def close(cls): return cls.load_icon("close.svg")
    
    # =================================================================
    # EDIT OPERATIONS
    # =================================================================
    
    @classmethod
    def cut(cls): return cls.load_icon("cut.svg")
    
    @classmethod
    def copy(cls): return cls.load_icon("copy.svg")
    
    @classmethod
    def paste(cls): return cls.load_icon("paste.svg")
    
    @classmethod
    def undo(cls): return cls.load_icon("undo.svg")
    
    @classmethod
    def redo(cls): return cls.load_icon("redo.svg")
    
    @classmethod
    def find(cls): return cls.load_icon("find.svg")
    
    @classmethod
    def replace(cls): return cls.load_icon("replace.svg")
    
    @classmethod
    def select_all(cls): return cls.load_icon("selectall.svg")
    
    # =================================================================
    # CODE OPERATIONS
    # =================================================================
    
    @classmethod
    def run(cls): return cls.load_icon("run.svg")
    
    @classmethod
    def debug(cls): return cls.load_icon("debug.svg")
    
    @classmethod
    def stop(cls): return cls.load_icon("stop.svg")
    
    @classmethod
    def restart(cls): return cls.load_icon("restart.svg")
    
    @classmethod
    def build(cls): return cls.load_icon("build.svg")
    
    @classmethod
    def deploy(cls): return cls.load_icon("deploy.svg")
    
    @classmethod
    def format(cls): return cls.load_icon("format.svg")
    
    @classmethod
    def lint(cls): return cls.load_icon("lint.svg")
    
    # =================================================================
    # NAVIGATION
    # =================================================================
    
    @classmethod
    def go_to_definition(cls): return cls.load_icon("gotodefinition.svg")
    
    @classmethod
    def find_references(cls): return cls.load_icon("findreferences.svg")
    
    @classmethod
    def peek_definition(cls): return cls.load_icon("peekdefinition.svg")
    
    @classmethod
    def go_back(cls): return cls.load_icon("goback.svg")
    
    @classmethod
    def go_forward(cls): return cls.load_icon("goforward.svg")