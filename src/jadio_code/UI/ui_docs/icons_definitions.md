# IconDefinitions: JADIO CODE Icon Name Variations

## Overview

`IconDefinitions` is a comprehensive collection of icon name variations, organized by category, for use throughout the JADIO CODE project. It extends the `IconsCore` class and provides VS Code-level coverage for file, folder, language, UI, terminal, git, status, sidebar, AI, network, and utility icons. This mapping enables robust icon lookup, fuzzy matching, and consistent iconography across the application.

---

## Purpose

- **Centralizes icon name variations** for all major UI and code concepts.
- **Enables fuzzy and multi-name matching** for icon lookup, improving reliability.
- **Supports extensibility** for new icon categories or names.

---

## Structure

### Class: `IconDefinitions`
- Inherits from: `IconsCore`
- Contains: Class variables (lists of string variations) for each icon concept.
- Organization: Grouped by functional and UI categories, matching professional IDE and VS Code conventions.

---

## Categories & Examples

### 1. File & Folder Icons
- `FOLDER_NAMES = ['folder', 'folder-closed', 'directory', ...]`
- `FILE_GENERIC_NAMES = ['file', 'file-generic', 'document', ...]`
- Specialized folders: `FOLDER_SRC_NAMES`, `FOLDER_DIST_NAMES`, etc.

### 2. Programming Language Files
- `FILE_PYTHON_NAMES = ['python', 'brand-python', 'snake', ...]`
- `FILE_JAVASCRIPT_NAMES = ['javascript', 'brand-javascript', 'js', ...]`
- Covers web, backend, scripting, data, and config languages.

### 3. UI Action Icons
- Navigation: `CHEVRON_RIGHT_NAMES`, `ARROW_LEFT_NAMES`, etc.
- Basic actions: `CLOSE_NAMES`, `MINIMIZE_NAMES`, `PLUS_NAMES`, etc.
- Common UI: `SEARCH_NAMES`, `FILTER_NAMES`, `REFRESH_NAMES`, etc.

### 4. Editor & Code Operations
- File ops: `NEW_FILE_NAMES`, `SAVE_NAMES`, `CLOSE_TAB_NAMES`, etc.
- Edit ops: `CUT_NAMES`, `COPY_NAMES`, `PASTE_NAMES`, etc.
- Code ops: `RUN_NAMES`, `DEBUG_NAMES`, `FORMAT_NAMES`, etc.

### 5. Terminal Icons
- `TERMINAL_NAMES`, `TERMINAL_CMD_NAMES`, `NEW_SHELL_NAMES`, etc.

### 6. Git & Version Control
- `GIT_NAMES`, `GIT_BRANCH_NAMES`, `GIT_COMMIT_NAMES`, etc.
- File status: `GIT_ADDED_NAMES`, `GIT_MODIFIED_NAMES`, etc.

### 7. Status & Notification
- `SUCCESS_NAMES`, `WARNING_NAMES`, `ERROR_NAMES`, `BELL_NAMES`, etc.

### 8. Sidebar & Panel
- `EXPLORER_NAMES`, `SEARCH_PANEL_NAMES`, `EXTENSIONS_NAMES`, etc.

### 9. AI & Chatbot
- `AI_NAMES`, `ROBOT_NAMES`, `CHAT_NAMES`, `SEND_NAMES`, etc.

### 10. Network & Connection
- `NETWORK_NAMES`, `WIFI_NAMES`, `CLOUD_NAMES`, `SERVER_NAMES`, etc.

### 11. Misc Utility
- General: `HOME_NAMES`, `STAR_NAMES`, `LOCK_NAMES`, etc.
- Interface: `MENU_NAMES`, `DOTS_HORIZONTAL_NAMES`, `GRIP_NAMES`, etc.
- Time: `CLOCK_NAMES`, `CALENDAR_NAMES`, etc.
- User: `USER_NAMES`, `TEAM_NAMES`, `ACCOUNT_NAMES`, etc.

---

## Usage Example

```python
from .icons_definitions import IconDefinitions

# Get all name variations for a folder icon
folder_names = IconDefinitions.FOLDER_NAMES

# Use with IconsCore for icon lookup
icon_svg = IconDefinitions.load_icon(IconDefinitions.FOLDER_NAMES)
```

---

## Extending
- Add new categories or name lists as class variables.
- Follow the naming convention: `CATEGORY_NAMES = [...]`.
- Keep lists ordered by most common/likely match first.

---

## File Location
This module should be placed in:
```
src/jadio_code/UI/ui_docs/icons_definitions.md
```

---

## License & Attribution
See the main project `license.md` for details.
