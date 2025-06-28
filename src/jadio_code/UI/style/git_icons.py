# UI/style/git_icons.py
"""
Git and version control icons
"""

from .icon_loader import IconLoader

class GitIcons(IconLoader):
    """Icons for Git and version control operations"""
    
    # =================================================================
    # GIT OPERATIONS
    # =================================================================
    
    @classmethod
    def git(cls): return cls.load_icon("git.svg")
    
    @classmethod
    def branch(cls): return cls.load_icon("branch.svg")
    
    @classmethod
    def commit(cls): return cls.load_icon("commit.svg")
    
    @classmethod
    def merge(cls): return cls.load_icon("merge.svg")
    
    @classmethod
    def pull(cls): return cls.load_icon("pull.svg")
    
    @classmethod
    def push(cls): return cls.load_icon("push.svg")
    
    @classmethod
    def clone(cls): return cls.load_icon("clone.svg")
    
    @classmethod
    def diff(cls): return cls.load_icon("diff.svg")
    
    @classmethod
    def stash(cls): return cls.load_icon("stash.svg")
    
    # =================================================================
    # FILE STATUS
    # =================================================================
    
    @classmethod
    def git_added(cls): return cls.load_icon("gitadded.svg")
    
    @classmethod
    def git_modified(cls): return cls.load_icon("gitmodified.svg")
    
    @classmethod
    def git_deleted(cls): return cls.load_icon("gitdeleted.svg")
    
    @classmethod
    def git_untracked(cls): return cls.load_icon("gituntracked.svg")
    
    @classmethod
    def git_conflict(cls): return cls.load_icon("gitconflict.svg")