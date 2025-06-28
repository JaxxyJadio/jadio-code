"""
JADIO CODE - Icon Routing
Single import point for all icons
"""

from .general_icons import GeneralIcons
from .panel_icons import PanelIcons
from .editor_icons import EditorIcons
from .git_icons import GitIcons
from .status_icons import StatusIcons
from .ui_icons import UIIcons
from .file_icons import FileIcons

class Icons:
    # General purpose
    General = GeneralIcons
    # Side panel / sidebar
    Panel = PanelIcons
    # Editor toolbar
    Editor = EditorIcons
    # Git controls
    Git = GitIcons
    # Status / Notifications
    Status = StatusIcons
    # UI buttons / general controls
    UI = UIIcons
    # File / Folder tree
    File = FileIcons
