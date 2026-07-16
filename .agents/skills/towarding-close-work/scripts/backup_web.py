import os
import shutil
from datetime import datetime

def perform_backup():
    # 1. Get current date in YYYYMMDD format
    today_str = datetime.now().strftime("%Y%m%d")
    
    # 2. Get working directory (repo root)
    workspace_root = r"d:\AntiGravity WorkSpace\TowardingWeb_AntGrv"
    
    # 3. Create target backup directory
    backup_dir = os.path.join(workspace_root, today_str)
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print(f"Created backup directory: {backup_dir}")
    else:
        print(f"Backup directory already exists: {backup_dir}")
        
    # 4. List of files and folders to copy
    files_to_copy = [
        "index.html",
        "style.css",
        "script.js",
        "hero_bg.png",
        "logo_header_transparent.png",
        "logo_footer_transparent.png",
        "qrcode.png",
        "towarding_intro.pdf",
        "favicon.ico",
        "favicon.png"
    ]
    
    dirs_to_copy = [
        "images"
    ]
    
    # 5. Copy files
    for file_name in files_to_copy:
        src_path = os.path.join(workspace_root, file_name)
        dest_path = os.path.join(backup_dir, file_name)
        if os.path.exists(src_path):
            shutil.copy2(src_path, dest_path)
            print(f"Copied file: {file_name} -> {dest_path}")
        else:
            print(f"Warning: Source file not found: {file_name}")
            
    # 6. Copy directories
    for dir_name in dirs_to_copy:
        src_dir = os.path.join(workspace_root, dir_name)
        dest_dir = os.path.join(backup_dir, dir_name)
        if os.path.exists(src_dir):
            if os.path.exists(dest_dir):
                shutil.rmtree(dest_dir) # Clear existing target dir to avoid nesting
            shutil.copytree(src_dir, dest_dir)
            print(f"Copied directory: {dir_name} -> {dest_dir}")
        else:
            print(f"Warning: Source directory not found: {dir_name}")
            
    print(f"\nBackup completed successfully at: {backup_dir}")

if __name__ == "__main__":
    perform_backup()
