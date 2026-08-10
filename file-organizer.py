"""
File Organizer
---------------
 Scan the folder and push the extension files in to the new sub folder and the extension files 
 move in it to organize in better way.(images,pdf,mp3,screenshot,etc.)

Usage:
    python file_organizer.py /path/to/folder
    python file_organizer.py /path/to/folder --dry-run
"""

import argparse
import shutil
from pathlib import Path

# Dictionary (Data Structures topic!) — extension ko category se map karta hai
EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".md", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".json", ".java", ".cpp"],
}


def build_reverse_map(extension_map: dict) -> dict:
    """
    Its reverse the Extension_map which used to easily fetch the file category for
     the 0(1) lookup.
    e.g. {".jpg": "Images", ".pdf": "Documents", ...}
    """
    reverse_map = {}
    for category, extensions in extension_map.items():
        for ext in extensions:
            reverse_map[ext] = category
    return reverse_map


def organize_folder(folder_path: str, dry_run: bool = False) -> dict:
    """
    Scan all the files in the folder and pushes in to the sub-folder category.
    Returns a summary dict: {category: count}
    """
    folder = Path(folder_path)
    if not folder.is_dir():
        raise NotADirectoryError(f"'{folder_path}' ek valid folder nahi hai.")

    reverse_map = build_reverse_map(EXTENSION_MAP)
    summary = {}

    # Only scan the top level files(subfolders are not touched)
    for item in folder.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            category = reverse_map.get(ext, "Others")

            summary[category] = summary.get(category, 0) + 1

            if not dry_run:
                target_dir = folder / category
                target_dir.mkdir(exist_ok=True)
                shutil.move(str(item), str(target_dir / item.name))

    return summary


def main():
    parser = argparse.ArgumentParser(description="Organize files by type into subfolders.")
    parser.add_argument("folder", help="Path to the folder you want to organize")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Sirf preview dikhaye, actual files move na kare",
    )
    args = parser.parse_args()

    summary = organize_folder(args.folder, dry_run=args.dry_run)

    mode = "DRY RUN (preview only)" if args.dry_run else "DONE"
    print(f"\n{mode} — Summary:")
    if not summary:
        print("  Koi file nahi mili organize karne ke liye.")
    for category, count in summary.items():
        print(f"  {category}: {count} file(s)")


if __name__ == "__main__":
    main()