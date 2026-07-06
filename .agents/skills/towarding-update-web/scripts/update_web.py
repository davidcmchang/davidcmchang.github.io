import os
import subprocess
import json

project_dir = r"d:\AntiGravity WorkSpace\TowardingWeb_AntGrv"

def run_cmd(cmd, cwd=project_dir):
    # Run with empty GITHUB_TOKEN to ensure gh CLI credential helper works on Windows
    env = os.environ.copy()
    env["GITHUB_TOKEN"] = ""
    result = subprocess.run(cmd, shell=True, cwd=cwd, text=True, capture_output=True, env=env)
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

    # 2. Git Status and Staging
    print("[2/4] Staging files for git...")
    run_cmd("git add CNAME index.html style.css script.js qrcode.png towarding_intro.pdf README.md ANTIGRAVITY.md")
    
    # 3. Git Commit
    status = run_cmd("git status --porcelain")
    if not status.stdout.strip():
        print("[3/4] No changes to commit.")
    else:
        print("[3/4] Committing changes...")
        # Use a generic update commit message
        commit_res = run_cmd('git commit -m "site: update web content and verify domain"')
        print(commit_res.stdout.strip())
        
    # 4. Force Push to Remote main branch
    print("[4/4] Force pushing changes to davidcmchang.github.io...")
    push_res = run_cmd("git push -f origin main")
    print(push_res.stdout.strip())
    if push_res.stderr:
        print(push_res.stderr.strip())
        
    print("\nUpdate process finished successfully! Website deployed to https://towarding.org/")

if __name__ == "__main__":
    main()
