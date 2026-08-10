File Organizer 🗂️

A simple command-line tool that automatically organizes files in a folder into categorized subfolders (Images, Documents, Videos, Audio, Archives, Code, and Others) based on their file extension.

Why this project?

Manually cleaning up a messy Downloads folder is tedious. This script scans a folder and sorts every file into the right category folder in one command.

Features
Organizes files by extension into clear categories
--dry-run mode to preview changes before actually moving files
No third-party dependencies — pure Python standard library
Easily extendable: add new categories/extensions in one dictionary
Usage
bash
# Preview what will happen (no files are moved)
python file_organizer.py /path/to/folder --dry-run

# Actually organize the folder
python file_organizer.py /path/to/folder
Example

Before:

Downloads/
  photo.jpg
  report.pdf
  song.mp3
  script.py

After:

Downloads/
  Images/photo.jpg
  Documents/report.pdf
  Audio/song.mp3
  Code/script.py
How it works

The script builds a reverse lookup dictionary mapping each file extension to its category, so every file is classified in O(1) time. It then either previews (--dry-run) or moves each file into a matching subfolder, creating the subfolder if it doesn't exist yet.

Possible improvements (future work)
Recursive mode to organize subfolders too
Config file (JSON/YAML) for custom category rules
Undo/rollback feature
GUI version using Tkinter
Tech stack

Python 3 · pathlib · argparse · shutil