# UI/style/color_loader.py
"""
JADIO Code Color Loader - Loads colors from colors.json with enhanced features
"""

import json
import os
from pathlib import Path
import re

class Colors:
    """Loads and manages JADIO signature colors from JSON with validation and utilities"""
    
    # Path to colors.json
    STYLE_DIR = Path(r"C:\JDOLabs\jadio-code\src\jadio_code\UI\style")
    COLORS_JSON_PATH = STYLE_DIR / "colors.json"
    
    # Cache for loaded colors
    _colors = None
    _color_schemes = None
    _metadata = None
    _is_loaded = False
    
    @classmethod
    def load_colors(cls, force_reload=False):
        """Load colors from colors.json file with optional force reload"""
        if cls._colors is None or force_reload:
            try:
                if cls.COLORS_JSON_PATH.exists():
                    with open(cls.COLORS_JSON_PATH, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        cls._colors = data.get('colors', {})
                        cls._color_schemes = data.get('color_schemes', {})
                        cls._metadata = {
                            'description': data.get('description', ''),
                            'version': data.get('version', '1.0.0'),
                            'brand': data.get('brand', 'JADIO Labs'),
                            'theme_philosophy': data.get('theme_philosophy', ''),
                            'usage_guidelines': data.get('usage_guidelines', {})
                        }
                        cls._is_loaded = True
                        print(f"✓ Loaded JADIO colors v{cls._metadata['version']}")
                else:
                    # Fallback colors if JSON doesn't exist
                    print("⚠ colors.json not found, using fallback colors")
                    cls._colors = cls._get_fallback_colors()
                    cls._color_schemes = cls._get_fallback_schemes()
                    cls._metadata = cls._get_fallback_metadata()
                    cls._is_loaded = True
            except Exception as e:
                print(f"❌ Error loading colors.json: {e}")
                cls._colors = cls._get_fallback_colors()
                cls._color_schemes = cls._get_fallback_schemes()
                cls._metadata = cls._get_fallback_metadata()
                cls._is_loaded = True
        
        return cls._colors
    
    @classmethod
    def get_color_schemes(cls):
        """Get predefined color schemes"""
        if cls._color_schemes is None:
            cls.load_colors()
        return cls._color_schemes
    
    @classmethod
    def get_metadata(cls):
        """Get color palette metadata"""
        if cls._metadata is None:
            cls.load_colors()
        return cls._metadata
    
    @classmethod
    def is_valid_hex_color(cls, color_value):
        """Validate if a string is a valid hex color"""
        if not isinstance(color_value, str):
            return False
        # Match #RGB, #RRGGBB, or #RRGGBBAA formats
        pattern = r'^#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6}|[A-Fa-f0-9]{8})$'
        return bool(re.match(pattern, color_value))
    
    @classmethod
    def get_color(cls, color_name, validate=True):
        """Get a specific color by name (supports nested access) with validation"""
        colors = cls.load_colors()
        result_color = None
        
        # Support nested access like "blacks.jadio_void"
        if '.' in color_name:
            category, name = color_name.split('.', 1)
            result_color = colors.get(category, {}).get(name)
        else:
            # Direct access - search all categories
            for category in colors.values():
                if isinstance(category, dict) and color_name in category:
                    result_color = category[color_name]
                    break
        
        # Handle not found
        if result_color is None:
            print(f"⚠ Warning: Color '{color_name}' not found, using fallback")
            return '#FF00FF'  # Magenta fallback
        
        # Validate hex color if requested
        if validate and not cls.is_valid_hex_color(result_color):
            print(f"⚠ Warning: Invalid hex color '{result_color}' for '{color_name}', using fallback")
            return '#FF00FF'
        
        return result_color
    
    @classmethod
    def get_color_safe(cls, color_name, fallback='#FF00FF'):
        """Get color with custom fallback (no console warnings)"""
        colors = cls.load_colors()
        
        if '.' in color_name:
            category, name = color_name.split('.', 1)
            result = colors.get(category, {}).get(name)
        else:
            result = None
            for category in colors.values():
                if isinstance(category, dict) and color_name in category:
                    result = category[color_name]
                    break
        
        return result if result and cls.is_valid_hex_color(result) else fallback
    
    @classmethod
    def search_colors(cls, search_term):
        """Search for colors by name pattern"""
        colors = cls.load_colors()
        results = {}
        search_lower = search_term.lower()
        
        for category_name, category_colors in colors.items():
            if isinstance(category_colors, dict):
                for color_name, color_value in category_colors.items():
                    if search_lower in color_name.lower() or search_lower in category_name.lower():
                        results[f"{category_name}.{color_name}"] = color_value
        
        return results
    
    @classmethod
    def get_category_colors(cls, category_name):
        """Get all colors from a specific category"""
        colors = cls.load_colors()
        return colors.get(category_name, {})
    
    @classmethod
    def get_categories(cls):
        """Get list of all color categories"""
        colors = cls.load_colors()
        return list(colors.keys())
    
    @classmethod
    def list_all_colors(cls, include_category_prefix=True):
        """Get a flat list of all available color names"""
        colors = cls.load_colors()
        all_colors = []
        
        for category_name, category_colors in colors.items():
            if isinstance(category_colors, dict):
                for color_name in category_colors.keys():
                    if include_category_prefix:
                        all_colors.append(f"{category_name}.{color_name}")
                    all_colors.append(color_name)  # Also add direct name
        
        return sorted(set(all_colors))  # Remove duplicates and sort
    
    @classmethod
    def validate_all_colors(cls):
        """Validate all colors in the palette"""
        colors = cls.load_colors()
        invalid_colors = []
        
        for category_name, category_colors in colors.items():
            if isinstance(category_colors, dict):
                for color_name, color_value in category_colors.items():
                    if not cls.is_valid_hex_color(color_value):
                        invalid_colors.append(f"{category_name}.{color_name}: {color_value}")
        
        if invalid_colors:
            print(f"⚠ Found {len(invalid_colors)} invalid colors:")
            for invalid in invalid_colors:
                print(f"  • {invalid}")
        else:
            print("✓ All colors are valid hex values")
        
        return len(invalid_colors) == 0
    
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
    
    @classmethod
    def _get_fallback_metadata(cls):
        """Fallback metadata"""
        return {
            "description": "JADIO Code Fallback Colors",
            "version": "1.0.0-fallback",
            "brand": "JADIO Labs",
            "theme_philosophy": "Modern, high-contrast, developer-focused",
            "usage_guidelines": {}
        }