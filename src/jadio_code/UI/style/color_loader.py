# UI/style/color_loader.py
"""
JADIO Code Color Loader - Loads colors from colors.json
"""

import json
from pathlib import Path

class ColorLoader:
    """Loads and manages JADIO signature colors from JSON"""
    
    # Path to colors.json
    STYLE_DIR = Path(r"C:\JDOLabs\jadio-code\src\jadio_code\UI\style")
    COLORS_JSON_PATH = STYLE_DIR / "colors.json"
    
    # Cache for loaded colors
    _colors = None
    _color_schemes = None
    
    @classmethod
    def load_colors(cls):
        """Load colors from colors.json file"""
        if cls._colors is None:
            try:
                if cls.COLORS_JSON_PATH.exists():
                    with open(cls.COLORS_JSON_PATH, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        cls._colors = data.get('colors', {})
                        cls._color_schemes = data.get('color_schemes', {})
                else:
                    # Fallback colors if JSON doesn't exist
                    cls._colors = cls._get_fallback_colors()
                    cls._color_schemes = cls._get_fallback_schemes()
            except Exception as e:
                print(f"Error loading colors.json: {e}")
                cls._colors = cls._get_fallback_colors()
                cls._color_schemes = cls._get_fallback_schemes()
        
        return cls._colors
    
    @classmethod
    def get_color_schemes(cls):
        """Get predefined color schemes"""
        if cls._color_schemes is None:
            cls.load_colors()
        return cls._color_schemes
    
    @classmethod
    def get_color(cls, color_name):
        """Get a specific color by name (supports nested access)"""
        colors = cls.load_colors()
        
        # Support nested access like "blacks.jadio_void"
        if '.' in color_name:
            category, name = color_name.split('.', 1)
            return colors.get(category, {}).get(name, '#FF00FF')  # Magenta fallback
        
        # Direct access - search all categories
        for category in colors.values():
            if isinstance(category, dict) and color_name in category:
                return category[color_name]
        
        # Not found - return magenta as warning
        print(f"Warning: Color '{color_name}' not found, using fallback")
        return '#FF00FF'
    
    @classmethod
    def get_category_colors(cls, category_name):
        """Get all colors from a specific category"""
        colors = cls.load_colors()
        return colors.get(category_name, {})
    
    @classmethod
    def list_all_colors(cls):
        """Get a flat list of all available color names"""
        colors = cls.load_colors()
        all_colors = []
        
        for category_name, category_colors in colors.items():
            if isinstance(category_colors, dict):
                for color_name in category_colors.keys():
                    all_colors.append(f"{category_name}.{color_name}")
                    all_colors.append(color_name)  # Also add direct name
        
        return sorted(set(all_colors))  # Remove duplicates and sort
    
    @classmethod
    def _get_fallback_colors(cls):
        """Fallback colors if JSON file is not available"""
        return {
            "blacks": {
                "jadio_void": "#0A0A0A",
                "jadio_midnight": "#121215",
                "jadio_obsidian": "#1A1A1E",
                "jadio_charcoal": "#252529",
                "jadio_carbon": "#2F2F35",
                "jadio_graphite": "#3A3A42"
            },
            "whites": {
                "jadio_pure": "#FEFEFE",
                "jadio_pearl": "#F8F9FA",
                "jadio_ivory": "#F5F6F8",
                "jadio_cream": "#F2F3F5"
            },
            "greys": {
                "jadio_silver": "#D4D5DA",
                "jadio_steel": "#C2C3C9",
                "jadio_slate": "#A8A9B1",
                "jadio_smoke": "#5D5E6B",
                "jadio_shadow": "#373843"
            },
            "reds": {
                "jadio_crimson": "#E63946",
                "jadio_ruby": "#DC2626",
                "jadio_cherry": "#B91C1C"
            },
            "accent_blues": {
                "jadio_electric": "#3B82F6",
                "jadio_azure": "#2563EB"
            },
            "semantic_colors": {
                "jadio_success": "#22C55E",
                "jadio_warning": "#EAB308",
                "jadio_error": "#EF4444",
                "jadio_info": "#3B82F6"
            },
            "ui_elements": {
                "jadio_border": "#374151",
                "jadio_hover": "#4B5563",
                "jadio_active": "#6B7280",
                "jadio_disabled": "#6B7280"
            }
        }
    
    @classmethod
    def _get_fallback_schemes(cls):
        """Fallback color schemes"""
        return {
            "dark_theme": {
                "background": "#0A0A0A",
                "surface": "#121215",
                "primary": "#3B82F6",
                "secondary": "#E63946"
            }
        }