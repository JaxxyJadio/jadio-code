# IconsCore: JADIO CODE Core Icon Loading System

## Overview

`IconsCore` is a robust icon management utility for the JADIO CODE project. It provides a comprehensive system for loading, searching, and serving icons with multiple fallback strategies, supporting a variety of image formats and usage scenarios. This system is designed to ensure that icons are always available, even if the exact file is missing, by searching multiple directories, supporting fuzzy matching, and generating fallback SVGs.

---

## Key Features

- **Multiple Search Directories:** Searches for icons in several possible locations to maximize the chance of finding the requested icon.
- **Format Support:** Handles SVG, PNG, JPG, JPEG, GIF, WEBP, and ICO formats.
- **Fallback Strategies:**
  - Tries exact matches first.
  - Performs fuzzy/partial matches if exact match fails.
  - Generates a default SVG icon with initials as a last resort.
- **Data URL Support:** Returns non-SVG icons as data URLs for easy embedding in CSS or HTML.
- **Color Customization:** Allows color overrides for SVG icons when generating data URLs.

---

## Class Structure

### `IconsCore`

#### Class Variables
- `POSSIBLE_ICON_DIRS`: List of `Path` objects representing directories to search for icon files.
- `SUPPORTED_FORMATS`: List of supported file extensions.

#### Methods

##### `load_icon(name_variations, fallback_name="")`
- **Purpose:** Loads icon content by searching for the given name(s) in all possible directories and formats.
- **Parameters:**
  - `name_variations`: A string or list of possible icon names (without extension).
  - `fallback_name`: Optional name to use for fallback SVG generation.
- **Returns:**
  - SVG content as a string (if SVG found or generated), or
  - Data URL string (for non-SVG formats).
- **Search Order:**
  1. Exact name match in all directories and formats.
  2. Fuzzy/partial match in all directories and formats.
  3. Generates a fallback SVG with initials if no file is found.

##### `get_icon_data_url(name_variations, color=None, fallback_name="")`
- **Purpose:** Returns the icon as a data URL, suitable for CSS or HTML embedding.
- **Parameters:**
  - `name_variations`: Icon name(s) to search for.
  - `color`: Optional color override for SVG icons.
  - `fallback_name`: Optional fallback name for SVG generation.
- **Returns:**
  - Data URL string for the icon.
- **Behavior:**
  - If the icon is already a data URL, returns it directly.
  - If SVG, encodes and returns as a data URL, applying color if specified.

---

## Fallback Logic

1. **Exact Match:**
   - Searches all directories for files named exactly as any of the `name_variations` with any supported extension.
2. **Fuzzy Match:**
   - If no exact match, searches for files whose names partially match any of the `name_variations`.
3. **SVG Generation:**
   - If no file is found, generates a simple SVG icon with a colored background and the initials of the fallback name or first name variation.

---

## Example Usage

```python
# Load SVG content or data URL for an icon named 'folder'
icon_content = IconsCore.load_icon('folder')

# Get a data URL for an icon, with a custom color for SVGs
icon_url = IconsCore.get_icon_data_url(['file', 'document'], color="#FF8800")
```

---

## Customization & Extension
- **Add More Directories:** Modify `POSSIBLE_ICON_DIRS` to include additional search paths.
- **Support More Formats:** Add new extensions to `SUPPORTED_FORMATS` and update MIME type handling.
- **SVG Template:** Customize the fallback SVG in the `load_icon` method for a different look.

---

## File Location
This module is typically located at:
```
UI/styles/icons_core.py
```

---

## License & Attribution
See the main project `license.md` for details.
