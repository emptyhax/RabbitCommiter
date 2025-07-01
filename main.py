import os
import subprocess
from datetime import datetime, timedelta
import random
import platform 

RABBIT_COMMITER_ART = r"""
                ████        ████    
              ██    ██    ██    ██  
              ██    ██    ██    ██  
              ██  ░░██    ██  ░░██  
              ██  ░░██    ██  ░░██  
              ██  ░░██    ██  ░░██  
              ██  ░░██████████░░██  
              ██                ██  
            ██                    ██           made by hax & dan
            ██                    ██
            ██        ██      ██  ██       _____      _     _     _ _    
            ██        ██      ██  ██      | ___ \    | |   | |   (_) |        
        ██████        ██      ██  ██      | |_/ /__ _| |__ | |__  _| |_   
      ██    ██            ░░      ██      |    // _` | '_ \| '_ \| | __|  
  ████        ██                ██        | |\ \ (_| | |_) | |_) | | |_      
██  ██            ██████████████          \_| \_\__,_|_.__/|_.__/|_|\__|  
██  ██                    ██      _____                           _ _                
  ████                    ██     /  __ \                         (_) |              
    ██              ██    ██     | /  \/ ___  _ __ ___  _ __ ___  _| |_ ___ _ __      
    ██    ████████  ██    ██     | |    / _ \| '_ ` _ \| '_ ` _ \| | __/ _ \ '__|     
    ██  ████  ██    ████  ██     | \__/\ (_) | | | | | | | | | | | | ||  __/ |       
      ████      ████  ██████      \____/\___/|_| |_| |_|_| |_| |_|_|\__\___|_|        
"""

def show_banner():
    print(f"\n\033[97m{RABBIT_COMMITER_ART}\033[0m")

def validate_date(date_str):
    try:
        day, month, year = map(int, date_str.split(":"))
        datetime(year=year, month=month, day=day)
        return True
    except ValueError:
        return False

def get_current_branch():
    try:
        branch = subprocess.check_output(
            "git branch --show-current", 
            shell=True, 
            stderr=subprocess.DEVNULL
        ).decode().strip()
        return branch
    except subprocess.CalledProcessError:
        return None

def generate_random_commit_message():
    messages = [
        "Empty commit for history",
        "Backfill commit",
        "Placeholder commit",
        "Sync point",
        "Maintenance commit",
    ]
    return random.choice(messages)

def detect_os():
    detected_os = platform.system().lower()
    os_map = {
        'linux': 'Linux',
        'windows': 'Windows',
        'darwin': 'MacOS'
    }
    
    detected = os_map.get(detected_os, 'Unknown')
    
    while True:
        print(f"\n\033[97m🔍 Detected OS: {detected}")
        user_input = input("\033[97m💻 Is this correct? (Y/n): \033[0m").strip().lower()
        
        if user_input in ['', 'y', 'yes']:
            return detected_os
        elif user_input in ['n', 'no']:
            print("\n\033[97mPlease select your OS:")
            print("1. Windows")
            print("2. Linux/MacOS")
            choice = input("\033[97mEnter your choice (1-2): \033[0m").strip()
            if choice == '1':
                return 'windows'
            elif choice == '2':
                return 'linux'
            else:
                print("\033[91m❌ Invalid choice. Please try again.\033[0m")
        else:
            print("\033[91m❌ Please answer with Y or N.\033[0m")

def make_empty_commits(date_str, commit_count, os_type):
    current_branch = get_current_branch()
    if current_branch not in ["main", "master"]:
        print(f"\033[91m❌ You're on branch '{current_branch}'. Please switch to 'main' or 'master'.\033[0m")
        return

    if not validate_date(date_str):
        print(f"\033[91m❌ Invalid date! Use DD:MM:YYYY format (ex: 02:04:2024).\033[0m")
        return

    day, month, year = map(int, date_str.split(":"))
    commit_date = datetime(year=year, month=month, day=day)

    if commit_count < 0 or commit_count > 100:
        print(f"\033[91m❌ Commit count must be between 0-100.\033[0m")
        return

    if not os.path.exists(".git"):
        print(f"\033[91m❌ This directory is not a Git repository.\033[0m")
        return

    print(f"\n\033[96m⏳ Generating {commit_count} empty commits on branch '{current_branch}' (date: {date_str})...\033[0m")

    for i in range(commit_count):
        adjusted_date = commit_date + timedelta(minutes=i)
        date_git_format = adjusted_date.strftime("%Y-%m-%d %H:%M:%S")
        message = generate_random_commit_message()
        
        try:
            if os_type == 'windows':
                subprocess.run(
                    f'set "GIT_AUTHOR_DATE={date_git_format}" && '
                    f'set "GIT_COMMITTER_DATE={date_git_format}" && '
                    f'git commit --allow-empty -m "{message}"',
                    shell=True,
                    check=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
            else:
                env = os.environ.copy()
                env["GIT_AUTHOR_DATE"] = date_git_format
                env["GIT_COMMITTER_DATE"] = date_git_format
                
                subprocess.run(
                    ["git", "commit", "--allow-empty", "-m", message],
                    env=env,
                    check=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
        except subprocess.CalledProcessError as e:
            print(f"\033[91m❌ Error creating commit {i+1}: {e}\033[0m")
            continue

    print(f"\033[92m✅ {commit_count} empty commits created on branch '{current_branch}'!\033[0m")
    
    push_confirm = input("\n\033[97m🚀 Do you want to push to remote repository? (Y/n): \033[0m").strip().lower()
    if push_confirm in ['', 'y', 'yes']:
        try:
            print("\033[96m⏳ Pushing to remote repository...\033[0m")
            subprocess.run(["git", "push", "origin", current_branch], check=True)
            print("\033[92m✅ Successfully pushed to remote!\033[0m")
        except subprocess.CalledProcessError as e:
            print(f"\033[91m❌ Error pushing to remote: {e}\033[0m")
            print("\033[93m⚠️ You may need to push manually with: git push origin {current_branch}\033[0m")

def main():
    show_banner()
    
    os_type = detect_os()
    print(f"\n\033[97m🖥️  Using {os_type.capitalize()} mode\033[0m")

    while True:
        date_input = input("\n\033[97m📅 Commit date (DD:MM:YYYY): \033[0m").strip()
        if not validate_date(date_input):
            print("\033[91m❌ Invalid format! Use DD:MM:YYYY (ex: 02:04:2024).\033[0m")
            continue

        try:
            commit_count = int(input("\033[97m🔢 Number of commits (0-100): \033[0m").strip())
            if commit_count < 0 or commit_count > 100:
                print("\033[91m❌ Number must be between 0-100.\033[0m")
                continue
            break
        except ValueError:
            print("\033[91m❌ Please enter a valid number.\033[0m")

    make_empty_commits(date_input, commit_count, os_type)

if __name__ == "__main__":
    main()
