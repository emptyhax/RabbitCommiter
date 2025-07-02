import os
import subprocess
from datetime import datetime, timedelta
import random
import platform
from colorama import Fore, Style, init

init()

RABBIT_COMMITER_ART = f"""
                {Fore.LIGHTBLUE_EX}████        ████{Fore.RESET}    
              {Fore.LIGHTBLUE_EX}██    ██    ██    ██{Fore.RESET}  
              {Fore.LIGHTBLUE_EX}██    ██    ██    ██{Fore.RESET}  
              {Fore.LIGHTBLUE_EX}██  ░░██    ██  ░░██{Fore.RESET}  
              {Fore.LIGHTBLUE_EX}██  ░░██    ██  ░░██{Fore.RESET}  
              {Fore.LIGHTBLUE_EX}██  ░░██    ██  ░░██{Fore.RESET}  
              {Fore.LIGHTBLUE_EX}██  ░░██████████░░██{Fore.RESET}  
              {Fore.LIGHTBLUE_EX}██                ██{Fore.RESET}  
            {Fore.LIGHTBLUE_EX}██                    ██{Fore.RESET}           made by hax & dan
            {Fore.LIGHTBLUE_EX}██                    ██{Fore.RESET}
            {Fore.LIGHTBLUE_EX}██        ██      ██  ██{Fore.RESET}       _____      _     _     _ _    
            {Fore.LIGHTBLUE_EX}██        ██      ██  ██{Fore.RESET}      | ___ \\    | |   | |   (_) |        
        {Fore.LIGHTBLUE_EX}██████        ██      ██  ██{Fore.RESET}      | |_/ /__ _| |__ | |__  _| |_   
      {Fore.LIGHTBLUE_EX}██    ██            ░░      ██{Fore.RESET}      |    // _` | '_ \\| '_ \\| | __|  
  {Fore.LIGHTBLUE_EX}████        ██                ██{Fore.RESET}        | |\\ \\ (_| | |_) | |_) | | |_      
{Fore.LIGHTBLUE_EX}██  ██            ██████████████{Fore.RESET}          \\_| \\_\\__,_|_.__/|_.__/|_|\\__|  
{Fore.LIGHTBLUE_EX}██  ██                    ██{Fore.RESET}      _____                           _ _                
  {Fore.LIGHTBLUE_EX}████                    ██{Fore.RESET}     /  __ \\                         (_) |              
    {Fore.LIGHTBLUE_EX}██              ██    ██{Fore.RESET}     | /  \\/ ___  _ __ ___  _ __ ___  _| |_ ___ _ __      
    {Fore.LIGHTBLUE_EX}██    ████████  ██    ██{Fore.RESET}     | |    / _ \\| '_ ` _ \\| '_ ` _ \\| | __/ _ \\ '__|     
    {Fore.LIGHTBLUE_EX}██  ████  ██    ████  ██{Fore.RESET}     | \\__/\\ (_) | | | | | | | | | | | | ||  __/ |       
      {Fore.LIGHTBLUE_EX}████      ████  ██████{Fore.RESET}      \\____/\\___/|_| |_| |_|_| |_| |_|_|\\__\\___|_|        
"""


def show_banner():
    print(RABBIT_COMMITER_ART)


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
    print(f"\n{Fore.CYAN}⏳ Initializing new Git repository...{Style.RESET_ALL}")
    try:
        subprocess.run(
            ["git", "init"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print(f"{Fore.GREEN}✅ Git repository initialized{Style.RESET_ALL}")

        repo_url = input(
            f"{Fore.WHITE}🌐 Enter the remote repository URL (or press Enter to skip): {Style.RESET_ALL}"
        ).strip()
        if repo_url:
            subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
            print(f"{Fore.GREEN}✅ Remote repository added{Style.RESET_ALL}")

            subprocess.run(
                ["git", "commit", "--allow-empty", "-m", "Initial commit"],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            print(f"{Fore.GREEN}✅ Initial commit created{Style.RESET_ALL}")

            subprocess.run(
                ["git", "branch", "-M", "main"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

        return True
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}❌ Error initializing Git repository: {e}{Style.RESET_ALL}")
        return False


def generate_random_commit_message():
    messages = [
        "🌱 Empty commit for history",
        "📌 Backfill commit",
        "🔄 Sync point",
        "🔧 Maintenance commit",
        "🎨 Code style improvements",
        "📚 Update documentation",
        "♻️ Refactor code",
        "✏️ Fix typo",
        "⚡ Optimize performance",
        "🧹 Clean up code",
        "🛠️ Fix minor bug",
        "📦 Update dependencies",
        "🚀 Prepare for release",
        "🔍 Add debugging",
        "💡 Add comments",
    ]
    return random.choice(messages)


def detect_os():
    detected_os = platform.system().lower()
    os_map = {"linux": "🐧 Linux", "windows": "🪟 Windows", "darwin": "🍎 MacOS"}

    detected = os_map.get(detected_os, "❓ Unknown")

    while True:
        print(f"\n{Fore.WHITE}🔍 Detected OS: {detected}")
        user_input = (
            input(f"{Fore.WHITE}💻 Is this correct? (Y/n): {Style.RESET_ALL}")
            .strip()
            .lower()
        )

        if user_input in ["", "y", "yes"]:
            return detected_os
        elif user_input in ["n", "no"]:
            print(f"\n{Fore.WHITE}Please select your OS:")
            print(f"1. {os_map['windows']}")
            print(f"2. {os_map['linux']}/{os_map['darwin']}")
            choice = input(
                f"{Fore.WHITE}Enter your choice (1-2): {Style.RESET_ALL}"
            ).strip()
            if choice == "1":
                return "windows"
            elif choice == "2":
                return "linux"
            else:
                print(
                    f"{Fore.RED}❌ Invalid choice. Please try again.{Style.RESET_ALL}"
                )
        else:
            print(f"{Fore.RED}❌ Please answer with Y or N.{Style.RESET_ALL}")


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
        print(
            f"{Fore.YELLOW}⚠️ No Git repository found in current directory{Style.RESET_ALL}"
        )
        if input(
            f"{Fore.WHITE}Would you like to initialize one? (Y/n): {Style.RESET_ALL}"
        ).lower() in ["", "y", "yes"]:
            if not initialize_git_repo():
                return
        else:
            print(f"{Fore.RED}❌ Operation cancelled by user{Style.RESET_ALL}")
            return

    current_branch = get_current_branch()
    if current_branch not in ["main", "master"]:
        print(
            f"{Fore.RED}❌ You're on branch '{current_branch}'. Please switch to 'main' or 'master'.{Style.RESET_ALL}"
        )
        return

    if not validate_date(date_start_str) or not validate_date(date_end_str):
        print(
            f"{Fore.RED}❌ Invalid date! Use DD:MM:YYYY format (ex: 02:04:2024).{Style.RESET_ALL}"
        )
        return

    day_s, month_s, year_s = map(int, date_start_str.split(":"))
    day_e, month_e, year_e = map(int, date_end_str.split(":"))
    date_start = datetime(year=year_s, month=month_s, day=day_s)
    date_end = datetime(year=year_e, month=month_e, day=day_e)

    if date_start > date_end:
        print(
            f"{Fore.RED}❌ Start date must be earlier than end date.{Style.RESET_ALL}"
        )
        return

    if commit_count < 0 or commit_count > 1000:
        print(f"{Fore.RED}❌ Commit count must be between 0-1000.{Style.RESET_ALL}")
        return

    print(
        f"\n{Fore.CYAN}⏳ Generating {commit_count} empty commits on branch '{current_branch}' from {date_start_str} to {date_end_str}...{Style.RESET_ALL}"
    )
    try:
        random_commit_dates = random_dates_between(date_start, date_end, commit_count)
    except ValueError as e:
        print(f"{Fore.RED}❌ {e}{Style.RESET_ALL}")
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
                    f"{Fore.WHITE}✅ Created commit {i+1}/{commit_count} - {message}{Style.RESET_ALL}"
                )

        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}❌ Error creating commit {i+1}: {e}{Style.RESET_ALL}")
            continue

    print(
        f"\n{Fore.GREEN}🎉 Successfully created {commit_count} empty commits on branch '{current_branch}'!{Style.RESET_ALL}"
    )

    push_confirm = (
        input(
            f"\n{Fore.WHITE}🚀 Do you want to push to remote repository? (Y/n): {Style.RESET_ALL}"
        )
        .strip()
        .lower()
    )
    if push_confirm in ["", "y", "yes"]:
        try:
            print(f"{Fore.CYAN}⏳ Pushing to remote repository...{Style.RESET_ALL}")
            subprocess.run(["git", "push", "-u", "origin", current_branch], check=True)
            print(f"{Fore.GREEN}✅ Successfully pushed to remote!{Style.RESET_ALL}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}❌ Error pushing to remote: {e}{Style.RESET_ALL}")
            print(
                f"{Fore.YELLOW}⚠️ You may need to push manually with: git push -u origin {current_branch}{Style.RESET_ALL}"
            )
    else:
        print(
            f"{Fore.YELLOW}⚠️ Remember to push your changes when ready!{Style.RESET_ALL}"
        )


def main():
    show_banner()

    os_type = detect_os()
    print(f"\n{Fore.WHITE}🖥️  Using {os_type.capitalize()} mode{Style.RESET_ALL}")

    while True:
        date_start_input = input(
            f"\n{Fore.WHITE}📅 Start date (DD:MM:YYYY): {Style.RESET_ALL}"
        ).strip()
        if not validate_date(date_start_input):
            print(
                f"{Fore.RED}❌ Invalid format! Use DD:MM:YYYY (ex: 02:04:2024).{Style.RESET_ALL}"
            )
            continue

        date_end_input = input(
            f"{Fore.WHITE}📅 End date (DD:MM:YYYY): {Style.RESET_ALL}"
        ).strip()
        if not validate_date(date_end_input):
            print(
                f"{Fore.RED}❌ Invalid format! Use DD:MM:YYYY (ex: 02:04:2024).{Style.RESET_ALL}"
            )
            continue

        day_s, month_s, year_s = map(int, date_start_input.split(":"))
        day_e, month_e, year_e = map(int, date_end_input.split(":"))
        date_start = datetime(year=year_s, month=month_s, day=day_s)
        date_end = datetime(year=year_e, month=month_e, day=day_e)

        if date_start > date_end:
            print(
                f"{Fore.RED}❌ Start date must be earlier than end date.{Style.RESET_ALL}"
            )
            continue

        days_between = (date_end - date_start).days
        print(f"{Fore.WHITE}📆 Time period: {days_between} days{Style.RESET_ALL}")

        while True:
            try:
                commit_count = (
                    input(
                        f"{Fore.WHITE}🔢 Number of commits (1-1000, or 'd' for daily average): {Style.RESET_ALL}"
                    )
                    .strip()
                    .lower()
                )

                if commit_count == "d":
                    suggested = max(1, min(1000, days_between * 2))
                    print(
                        f"{Fore.WHITE}✨ Suggested: {suggested} commits ({suggested/days_between:.1f} per day){Style.RESET_ALL}"
                    )
                    commit_count = input(
                        f"{Fore.WHITE}🔢 Enter number of commits (1-1000): {Style.RESET_ALL}"
                    ).strip()

                commit_count = int(commit_count)
                if commit_count < 1 or commit_count > 1000:
                    print(
                        f"{Fore.RED}❌ Number must be between 1-1000.{Style.RESET_ALL}"
                    )
                    continue

                avg_per_day = commit_count / max(1, days_between)
                if avg_per_day > 10:
                    print(
                        f"{Fore.YELLOW}⚠️ Warning: High commit density ({avg_per_day:.1f} commits/day){Style.RESET_ALL}"
                    )
                    confirm = input(
                        f"{Fore.WHITE}Are you sure? (Y/n): {Style.RESET_ALL}"
                    ).lower()
                    if confirm not in ["", "y", "yes"]:
                        continue
                break
            except ValueError:
                print(f"{Fore.RED}❌ Please enter a valid number.{Style.RESET_ALL}")

        break

    make_empty_commits(date_start_input, date_end_input, commit_count, os_type)

    print(f"\n{Fore.MAGENTA}✨ All done! Happy coding! 🚀{Style.RESET_ALL}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}❌ Operation cancelled by user.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}❌ An unexpected error occurred: {e}{Style.RESET_ALL}")
