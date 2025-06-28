# UI/style/file_icons.py
"""
File and folder icons
"""

from .icon_loader import IconLoader

class FileIcons(IconLoader):
    """Icons for files and folders"""
    
    # =================================================================
    # FOLDER ICONS
    # =================================================================
    
    @classmethod
    def folder(cls): return cls.load_icon("folder.svg")
    
    @classmethod
    def folder_open(cls): return cls.load_icon("folderopen.svg")
    
    @classmethod
    def folder_src(cls): return cls.load_icon("foldersrc.svg")
    
    @classmethod
    def folder_dist(cls): return cls.load_icon("folderdist.svg")
    
    @classmethod
    def folder_node_modules(cls): return cls.load_icon("foldernodemodules.svg")
    
    @classmethod
    def folder_config(cls): return cls.load_icon("folderconfig.svg")
    
    @classmethod
    def folder_docs(cls): return cls.load_icon("folderdocs.svg")
    
    @classmethod
    def folder_images(cls): return cls.load_icon("folderimages.svg")
    
    @classmethod
    def folder_tests(cls): return cls.load_icon("foldertests.svg")
    
    @classmethod
    def folder_hidden(cls): return cls.load_icon("folderhidden.svg")
    
    # =================================================================
    # SPECIAL CONFIG FILES
    # =================================================================
    
    @classmethod
    def config(cls): return cls.load_icon("config.svg")
    
    @classmethod
    def env(cls): return cls.load_icon("env.svg")
    
    @classmethod
    def license(cls): return cls.load_icon("license.svg")
    
    @classmethod
    def readme(cls): return cls.load_icon("readme.svg")
    
    @classmethod
    def changelog(cls): return cls.load_icon("changelog.svg")
    
    @classmethod
    def makefile(cls): return cls.load_icon("makefile.svg")
    
    @classmethod
    def package(cls): return cls.load_icon("package.svg")
    
    # =================================================================
    # GENERIC FILE TYPES
    # =================================================================
    
    @classmethod
    def file(cls): return cls.load_icon("file.svg")
    
    @classmethod
    def text(cls): return cls.load_icon("text.svg")
    
    @classmethod
    def binary(cls): return cls.load_icon("binary.svg")
    
    @classmethod
    def archive(cls): return cls.load_icon("archive.svg")
    
    @classmethod
    def image(cls): return cls.load_icon("image.svg")
    
    @classmethod
    def audio(cls): return cls.load_icon("audio.svg")
    
    @classmethod
    def video(cls): return cls.load_icon("video.svg")
    
    @classmethod
    def pdf(cls): return cls.load_icon("pdf.svg")