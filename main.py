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
        branch = (
            subprocess.check_output(
                "git branch --show-current", shell=True, stderr=subprocess.DEVNULL
            )
            .decode()
            .strip()
        )
        return branch
    except subprocess.CalledProcessError:
        return None


def initialize_git_repo():
    print("\033[96m⏳ Initializing new Git repository...\033[0m")
    try:
        subprocess.run(
            ["git", "init"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print("\033[92m✅ Git repository initialized\033[0m")

        repo_url = input("\033[97m🔗 Enter the remote repository URL: \033[0m").strip()
        if repo_url:
            subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
            print("\033[92m✅ Remote repository added\033[0m")

            subprocess.run(
                ["git", "commit", "--allow-empty", "-m", "Initial commit"],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            print("\033[92m✅ Initial commit created\033[0m")

            subprocess.run(
                ["git", "branch", "-M", "main"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

        return True
    except subprocess.CalledProcessError as e:
        print(f"\033[91m❌ Error initializing Git repository: {e}\033[0m")
        return False


def generate_random_commit_message():
    messages = [
        "Empty commit for history",
        "Backfill commit",
        "Placeholder commit",
        "Sync point",
        "Maintenance commit",
        "Code style improvements",
        "Update documentation",
        "Refactor code",
        "Fix typo",
        "Optimize performance",
    ]
    return random.choice(messages)


def detect_os():
    detected_os = platform.system().lower()
    os_map = {"linux": "Linux", "windows": "Windows", "darwin": "MacOS"}

    detected = os_map.get(detected_os, "Unknown")

    while True:
        print(f"\n\033[97m🔍 Detected OS: {detected}")
        user_input = input("\033[97m💻 Is this correct? (Y/n): \033[0m").strip().lower()

        if user_input in ["", "y", "yes"]:
            return detected_os
        elif user_input in ["n", "no"]:
            print("\n\033[97mPlease select your OS:")
            print("1. Windows")
            print("2. Linux/MacOS")
            choice = input("\033[97mEnter your choice (1-2): \033[0m").strip()
            if choice == "1":
                return "windows"
            elif choice == "2":
                return "linux"
            else:
                print("\033[91m❌ Invalid choice. Please try again.\033[0m")
        else:
            print("\033[91m❌ Please answer with Y or N.\033[0m")


def random_dates_between(start, end, count):
    total_seconds = int((end - start).total_seconds())
    if total_seconds < count:
        raise ValueError(
            f"Interval of {total_seconds} seconds is insufficient to generate {count} unique dates."
        )
    random_seconds = sorted(random.sample(range(total_seconds), count))
    return [start + timedelta(seconds=sec) for sec in random_seconds]


def make_empty_commits(date_start_str, date_end_str, commit_count, os_type):
    if not os.path.exists(".git"):
        print("\033[93m⚠️ No Git repository found in current directory\033[0m")
        if input(
            "\033[97mWould you like to initialize one? (Y/n): \033[0m"
        ).lower() in ["", "y", "yes"]:
            if not initialize_git_repo():
                return
        else:
            print("\033[91m❌ Operation cancelled by user\033[0m")
            return

    current_branch = get_current_branch()
    if current_branch not in ["main", "master"]:
        print(
            f"\033[91m❌ You're on branch '{current_branch}'. Please switch to 'main' or 'master'.\033[0m"
        )
        return

    if not validate_date(date_start_str) or not validate_date(date_end_str):
        print(
            f"\033[91m❌ Invalid date! Use DD:MM:YYYY format (ex: 02:04:2024).\033[0m"
        )
        return

    day_s, month_s, year_s = map(int, date_start_str.split(":"))
    day_e, month_e, year_e = map(int, date_end_str.split(":"))
    date_start = datetime(year=year_s, month=month_s, day=day_s)
    date_end = datetime(year=year_e, month=month_e, day=day_e)

    if date_start > date_end:
        print(f"\033[91m❌ Start date must be earlier than end date.\033[0m")
        return

    if commit_count < 0 or commit_count > 1000:
        print(f"\033[91m❌ Commit count must be between 0-1000.\033[0m")
        return

    print(
        f"\n\033[96m⏳ Generating {commit_count} empty commits on branch '{current_branch}' from {date_start_str} to {date_end_str}...\033[0m"
    )
    try:
        random_commit_dates = random_dates_between(date_start, date_end, commit_count)
    except ValueError as e:
        print(f"\033[91m❌ {e}\033[0m")
        return

    for i in range(commit_count):
        adjusted_date = random_commit_dates[i]
        date_git_format = adjusted_date.strftime("%Y-%m-%d %H:%M:%S")
        message = generate_random_commit_message()

        try:
            if os_type == "windows":
                subprocess.run(
                    f'set "GIT_AUTHOR_DATE={date_git_format}" && '
                    f'set "GIT_COMMITTER_DATE={date_git_format}" && '
                    f'git commit --allow-empty -m "{message}"',
                    shell=True,
                    check=True,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
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
                    stderr=subprocess.DEVNULL,
                )

            if (i + 1) % 10 == 0 or (i + 1) == commit_count:
                print(
                    f"\033[97m✅ Created commit {i+1}/{commit_count} - {message}\033[0m"
                )

        except subprocess.CalledProcessError as e:
            print(f"\033[91m❌ Error creating commit {i+1}: {e}\033[0m")
            continue

    print(
        f"\n\033[92m🎉 Successfully created {commit_count} empty commits on branch '{current_branch}'!\033[0m"
    )

    push_confirm = (
        input("\n\033[97m🚀 Do you want to push to remote repository? (Y/n): \033[0m")
        .strip()
        .lower()
    )
    if push_confirm in ["", "y", "yes"]:
        try:
            print("\033[96m⏳ Pushing to remote repository...\033[0m")
            subprocess.run(["git", "push", "-u", "origin", current_branch], check=True)
            print("\033[92m✅ Successfully pushed to remote!\033[0m")
        except subprocess.CalledProcessError as e:
            print(f"\033[91m❌ Error pushing to remote: {e}\033[0m")
            print(
                f"\033[93m⚠️ You may need to push manually with: git push -u origin {current_branch}\033[0m"
            )
    else:
        print("\033[93m⚠️ Remember to push your changes when ready!\033[0m")


def main():
    show_banner()

    os_type = detect_os()
    print(f"\n\033[97m🖥️  Using {os_type.capitalize()} mode\033[0m")

    while True:
        date_start_input = input(
            "\n\033[97m📅 Start date (DD:MM:YYYY): \033[0m"
        ).strip()
        if not validate_date(date_start_input):
            print("\033[91m❌ Invalid format! Use DD:MM:YYYY (ex: 02:04:2024).\033[0m")
            continue

        date_end_input = input("\033[97m📅 End date (DD:MM:YYYY): \033[0m").strip()
        if not validate_date(date_end_input):
            print("\033[91m❌ Invalid format! Use DD:MM:YYYY (ex: 02:04:2024).\033[0m")
            continue

        try:
            commit_count = int(
                input("\033[97m🔢 Number of commits (0-1000): \033[0m").strip()
            )
            if commit_count < 0 or commit_count > 1000:
                print("\033[91m❌ Number must be between 0-1000.\033[0m")
                continue
            break
        except ValueError:
            print("\033[91m❌ Please enter a valid number.\033[0m")

    make_empty_commits(date_start_input, date_end_input, commit_count, os_type)


if __name__ == "__main__":
    main()
