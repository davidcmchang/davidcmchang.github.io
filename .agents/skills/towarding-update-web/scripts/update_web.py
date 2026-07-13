import os
import subprocess
import json

project_dir = r"d:\AntiGravity WorkSpace\TowardingWeb_AntGrv"

def run_cmd(cmd, cwd=project_dir):
    # Run with empty GITHUB_TOKEN to ensure gh CLI credential helper works on Windows
    env = os.environ.copy()
    env["GITHUB_TOKEN"] = ""
    result = subprocess.run(cmd, shell=True, cwd=cwd, text=True, capture_output=True, env=env, encoding="utf-8", errors="replace")
    return result

def main():
    print("=== [Towarding Web Update Skill] ===")
    
    # 1. Check and create CNAME file
    cname_path = os.path.join(project_dir, "CNAME")
    cname_content = "towarding.org"
    
    try:
        write_cname = True
        if os.path.exists(cname_path):
            with open(cname_path, "r", encoding="utf-8") as f:
                current = f.read().strip()
            if current == cname_content:
                write_cname = False
                print("[1/4] CNAME file already exists and is correct.")
        
        if write_cname:
            with open(cname_path, "w", encoding="utf-8", newline="\n") as f:
                f.write(cname_content)
            print("[1/4] Created CNAME file pointing to towarding.org.")
    except Exception as e:
        print(f"Error creating CNAME: {e}")
        return

    # 2. Copy webpage files to Backup folder
    print("[2/5] Backing up webpage files to Backup folder...")
    backup_dir = os.path.join(project_dir, "Backup")
    try:
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            print("Created Backup directory.")
            
        files_to_backup = [
            "index.html",
            "style.css",
            "script.js",
            "hero_bg.png",
            "logo_header_transparent.png",
            "logo_footer_transparent.png",
            "qrcode.png",
            "towarding_intro.pdf"
        ]
        
        import shutil
        for f in files_to_backup:
            src = os.path.join(project_dir, f)
            dst = os.path.join(backup_dir, f)
            if os.path.exists(src):
                shutil.copy2(src, dst)
                print(f"Backed up file: {f}")
                
        # Copy images folder recursively
        src_images = os.path.join(project_dir, "images")
        dst_images = os.path.join(backup_dir, "images")
        if os.path.exists(src_images):
            if os.path.exists(dst_images):
                shutil.rmtree(dst_images)
            shutil.copytree(src_images, dst_images)
            print("Backed up images directory.")
    except Exception as e:
        print(f"Error performing backup: {e}")
        return

    # 3. Git Status and Staging
    print("[3/5] Staging files for git...")
    run_cmd("git add CNAME index.html style.css script.js qrcode.png towarding_intro.pdf README.md ANTIGRAVITY.md logo_header_transparent.png logo_footer_transparent.png hero_bg.png images Backup .gitignore .agents/skills/towarding-update-web/scripts/update_web.py .agents/skills/towarding-close-work/SKILL.md .agents/skills/towarding-close-work/scripts/backup_web.py")
    
    # Dynamically find and stage local logo source files to avoid encoding issues
    for f in os.listdir(project_dir):
        if "Logo淡" in f or "Logo深" in f:
            run_cmd(f'git add "{f}"')
    
    # 4. Git Commit
    status = run_cmd("git status --porcelain")
    if not status.stdout.strip():
        print("[4/5] No changes to commit.")
    else:
        print("[4/5] Committing changes...")
        # Use a generic update commit message
        commit_res = run_cmd('git commit -m "site: update web content and verify domain with backup"')
        print(commit_res.stdout.strip())
        
    # 5. Force Push to Remote main branch
    print("[5/5] Force pushing changes to davidcmchang.github.io...")
    push_res = run_cmd("git push -f origin HEAD:main")
    print(push_res.stdout.strip())
    if push_res.stderr:
        print(push_res.stderr.strip())
        
    print("\nUpdate process finished successfully! Website deployed to https://towarding.org/")

if __name__ == "__main__":
    main()
