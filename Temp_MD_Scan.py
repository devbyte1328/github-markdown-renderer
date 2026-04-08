import os
import re
import shutil
from pathlib import Path

def scan_and_copy(md_file_path, destination_root):
    """
    Scans a Markdown file for images and copies them to destination_root,
    preserving the internal folder structure.
    """
    md_path = Path(md_file_path).resolve()
    dest_root = Path(destination_root).resolve()
    base_dir = md_path.parent

    if not md_path.exists():
        print(f"Error: {md_file_path} does not exist.")
        return

    # Regex: Finds ![alt](path) and captures the path
    # Ignores external URLs (http/https)
    img_pattern = re.compile(r'!\[.*?\]\(((?!http|https|www).*?)\)')

    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Failed to read file: {e}")
        return

    # Find all matches
    matches = img_pattern.findall(content)
    
    if not matches:
        print("No local images found to copy.")
        return

    print(f"Found {len(matches)} image(s). Processing...")

    for img_rel_path in matches:
        # 1. Clean path (remove potential URL-encoded spaces like %20)
        clean_rel_path = img_rel_path.replace('%20', ' ')
        
        # 2. Locate source file (relative to MD file)
        source_file = (base_dir / clean_rel_path).resolve()
        
        # 3. Define target path
        target_file = (dest_root / clean_rel_path).resolve()

        if source_file.exists() and source_file.is_file():
            # Create sub-directories if they don't exist
            target_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy the file (shutil.copy2 preserves metadata)
            shutil.copy2(source_file, target_file)
            print(f"Copied: {clean_rel_path}")
        else:
            print(f"Skipped (Not Found): {source_file}")

