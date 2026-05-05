# File Organizer Bot
Automatically organizes files in a folder based on file extensions using configurable rules.

Built to practice file handling, automation, and basic system design in Python.


## Features
- Organizes files by type (images, videos, etc.)
- Config-driven rules using JSON
- Handles duplicate filenames automatically
- Supports unknown file types
- Supports 100+ extension

## Tech Stack
- Python
- os, shutil
- JSON

## How It Works
1. Loads rules from config.json
2. Scans target directory
3. Matches file extensions to categorize
4. Moves files to respective folders
5. Renames files if duplicates exist

## Setup

1. Clone the repository
2. Update the folder path in main.py OR enter via input
3. Run the script:

```bash
python main.py
```
---

## 8. **Example Config**
```markdown
## Example Config (config.json)
{
    "png": "Images",
    "jpg": "Images",
    "jpeg": "Images",
    "gif": "Images",
    "bmp": "Images",
    "tiff": "Images",
    "svg": "Vector Graphics",
    "webp": "Images",
    "ico": "Icons"
}
```
## Limitations
- Uses file extensions only (not content-based detection)
- No GUI support

## Future Improvements
- Add command-line arguments
- Add scheduling/automation
- Improve file type detection

## What I Learned
- File handling using os and shutil
- Handling edge cases like duplicate files
- Separating logic from configuration
- Designing simple automation systems
