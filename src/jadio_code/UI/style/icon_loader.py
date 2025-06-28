# UI/style/icon_loader.py
"""
Base icon loading functionality with JSON registry and color support
"""

import os
import json
import re
from pathlib import Path
import urllib.parse
from .color_loader import ColorLoader

class IconLoader:
    """Base class for loading SVG icons from single directory with JSON registry and color support"""
    
    # Directories
    STYLE_DIR = Path(r"C:\JDOLabs\jadio-code\src\jadio_code\UI\style")
    ICON_DIR = STYLE_DIR / "icons"
    ICONS_JSON_PATH = STYLE_DIR / "icons.json"
    
    # Cache for loaded icon registry
    _icon_registry = None
    
    @classmethod
    def load_icon_registry(cls):
        """Load the icons.json registry file"""
        if cls._icon_registry is None:
            try:
                if cls.ICONS_JSON_PATH.exists():
                    with open(cls.ICONS_JSON_PATH, 'r', encoding='utf-8') as f:
                        cls._icon_registry = json.load(f)
                else:
                    # Default registry if file doesn't exist
                    cls._icon_registry = {
                        "icon_modules": [
                            "language_icons",
                            "editor_icons", 
                            "file_icons",
                            "ui_icons",
                            "panel_icons",
                            "git_icons",
                            "status_icons",
                            "general_icons"
                        ],
                        "icon_directory": "icons",
                        "description": "JADIO Code Icon Registry"
                    }
            except Exception:
                cls._icon_registry = {"icon_modules": [], "description": "Failed to load registry"}
        
        return cls._icon_registry
    
    @classmethod
    def get_available_modules(cls):
        """Get list of available icon module names"""
        registry = cls.load_icon_registry()
        return registry.get("icon_modules", [])
    
    @classmethod
    def load_icon(cls, svg_filename, color=None, fallback_color=None):
        """Load SVG content from file with optional color override"""
        icon_path = cls.ICON_DIR / svg_filename
        
        # Try to load the SVG file
        if icon_path.exists():
            try:
                with open(icon_path, 'r', encoding='utf-8') as f:
                    svg_content = f.read()
                    
                    # Apply color if specified
                    if color:
                        svg_content = cls._apply_color_to_svg(svg_content, color)
                    
                    return svg_content
            except Exception:
                pass
        
        # Generate fallback SVG if file doesn't exist
        name = svg_filename.replace('.svg', '').replace('-', ' ').replace('_', ' ')
        initials = ''.join([c for c in name.title() if c.isupper()])[:2] or name[:2].upper()
        
        # Use fallback color or default JADIO colors
        bg_color = fallback_color or ColorLoader.get_color_safe('jadio_graphite', '#404040')
        border_color = ColorLoader.get_color_safe('jadio_border', '#666666')
        text_color = ColorLoader.get_color_safe('jadio_pearl', '#ffffff')
        
        return f'''<svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
            <rect width="16" height="16" rx="2" fill="{bg_color}" stroke="{border_color}" stroke-width="0.5"/>
            <text x="8" y="11" text-anchor="middle" font-family="Arial, sans-serif" font-size="6" fill="{text_color}">{initials}</text>
        </svg>'''
    
    @classmethod
    def _apply_color_to_svg(cls, svg_content, color):
        """Apply color to SVG content by replacing fill and stroke attributes"""
        # Resolve color name to hex if it's a JADIO color
        if isinstance(color, str) and not color.startswith('#'):
            color = ColorLoader.get_color_safe(color, color)
        
        # Replace currentColor with the specified color
        svg_content = svg_content.replace('currentColor', color)
        
        # Replace common fill attributes
        svg_content = re.sub(r'fill="[^"]*"', f'fill="{color}"', svg_content)
        
        # For stroke-based icons, also update stroke
        if 'stroke=' in svg_content and 'fill="none"' in svg_content:
            svg_content = re.sub(r'stroke="[^"]*"', f'stroke="{color}"', svg_content)
        
        return svg_content
    
    @classmethod
    def get_icon_data_url(cls, svg_filename, color=None):
        """Get icon as data URL for CSS usage with optional color"""
        content = cls.load_icon(svg_filename, color=color)
        encoded = urllib.parse.quote(content)
        return f"data:image/svg+xml,{encoded}"
    
    @classmethod
    def get_colored_icon(cls, svg_filename, color_name):
        """Get icon with JADIO color applied"""
        color = ColorLoader.get_color_safe(color_name)
        return cls.load_icon(svg_filename, color=color)
    
    @classmethod
    def get_themed_icon(cls, svg_filename, theme='dark'):
        """Get icon with theme-appropriate colors"""
        if theme == 'dark':
            color = ColorLoader.get_color_safe('jadio_pearl', '#F8F9FA')
        elif theme == 'light':
            color = ColorLoader.get_color_safe('jadio_charcoal', '#252529')
        else:
            color = ColorLoader.get_color_safe('jadio_silver', '#D4D5DA')
        
        return cls.load_icon(svg_filename, color=color)
    
    @classmethod
    def get_status_icon(cls, svg_filename, status='normal'):
        """Get icon with status-appropriate colors"""
        status_colors = {
            'success': ColorLoader.get_color_safe('jadio_success', '#22C55E'),
            'warning': ColorLoader.get_color_safe('jadio_warning', '#EAB308'),
            'error': ColorLoader.get_color_safe('jadio_error', '#EF4444'),
            'info': ColorLoader.get_color_safe('jadio_info', '#3B82F6'),
            'disabled': ColorLoader.get_color_safe('jadio_disabled', '#6B7280'),
            'normal': ColorLoader.get_color_safe('jadio_pearl', '#F8F9FA'),
            'active': ColorLoader.get_color_safe('jadio_crimson', '#E63946'),
            'hover': ColorLoader.get_color_safe('jadio_electric', '#3B82F6')
        }
        
        color = status_colors.get(status, status_colors['normal'])
        return cls.load_icon(svg_filename, color=color)
    
    @classmethod
    def get_semantic_icon(cls, svg_filename, semantic_type):
        """Get icon with semantic coloring (git, editor, etc.)"""
        semantic_colors = {
            # Git colors
            'git_added': ColorLoader.get_color_safe('jadio_git_added', '#22C55E'),
            'git_modified': ColorLoader.get_color_safe('jadio_git_modified', '#F59E0B'),
            'git_deleted': ColorLoader.get_color_safe('jadio_git_deleted', '#EF4444'),
            'git_untracked': ColorLoader.get_color_safe('jadio_git_untracked', '#8B5CF6'),
            'git_conflict': ColorLoader.get_color_safe('jadio_git_conflict', '#DC2626'),
            
            # Editor colors
            'editor_primary': ColorLoader.get_color_safe('jadio_electric', '#3B82F6'),
            'editor_secondary': ColorLoader.get_color_safe('jadio_gold', '#F59E0B'),
            'editor_accent': ColorLoader.get_color_safe('jadio_crimson', '#E63946'),
            
            # UI element colors
            'ui_primary': ColorLoader.get_color_safe('jadio_pearl', '#F8F9FA'),
            'ui_secondary': ColorLoader.get_color_safe('jadio_silver', '#D4D5DA'),
            'ui_accent': ColorLoader.get_color_safe('jadio_crimson', '#E63946')
        }
        
        color = semantic_colors.get(semantic_type, ColorLoader.get_color_safe('jadio_pearl'))
        return cls.load_icon(svg_filename, color=color)
    
    @classmethod
    def create_icon_css_class(cls, class_name, svg_filename, color=None, size='16px'):
        """Create CSS class for an icon with proper coloring"""
        data_url = cls.get_icon_data_url(svg_filename, color=color)
        
        return f"""
        .{class_name} {{
            background-image: url('{data_url}');
            background-repeat: no-repeat;
            background-position: center;
            background-size: {size};
            width: {size};
            height: {size};
            display: inline-block;
        }}
        """
    
    @classmethod
    def generate_icon_variants(cls, svg_filename):
        """Generate multiple color variants of an icon"""
        variants = {}
        
        # Standard variants
        variants['default'] = cls.load_icon(svg_filename)
        variants['light'] = cls.get_themed_icon(svg_filename, 'light')
        variants['dark'] = cls.get_themed_icon(svg_filename, 'dark')
        
        # Status variants
        for status in ['success', 'warning', 'error', 'info', 'disabled']:
            variants[status] = cls.get_status_icon(svg_filename, status)
        
        # Brand variants
        variants['primary'] = cls.get_colored_icon(svg_filename, 'jadio_crimson')
        variants['secondary'] = cls.get_colored_icon(svg_filename, 'jadio_electric')
        variants['accent'] = cls.get_colored_icon(svg_filename, 'jadio_gold')
        
        return variants