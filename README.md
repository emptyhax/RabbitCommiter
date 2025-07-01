# RabbitCommiter

RabbitCommiter is a command-line tool to generate multiple empty commits in a Git repository, distributed randomly between two dates. Useful for backfilling history, testing CI/CD flows, or maintaining contribution streaks. The script is fully interactive and supports Windows, Linux, and MacOS.

## Features
- Generate up to **1000** empty commits between two chosen dates
- Cross-platform support (Windows, Linux, MacOS)
- Random commit messages for each commit
- Fully interactive operation (dates, amount, OS, push)
- Option to automatically push to the remote repository
- Only works on `main` or `master` branches

## Requirements
- Python 3.6+
- Git installed and available in your system's PATH
- An initialized Git repository (run from the project root)

## How to use
1. **Clone or download this repository.**
2. **Open the terminal in the project folder.**
3. **Run the script:**
   ```bash
   python main.py
   ```
4. **Follow the interactive prompts:**
   - Confirm your operating system
   - Enter the start and end dates in `DD:MM:YYYY` format (e.g., 02:04:2024)
   - Enter the number of empty commits to generate (0-1000)
   - Choose whether to push to the remote repository

## Example
```
$ python main.py

🔍 Detected OS: Windows
💻 Is this correct? (Y/n): y
📅 Start date (DD:MM:YYYY): 01:05:2024
📅 End date (DD:MM:YYYY): 10:05:2024
🔢 Number of commits (0-1000): 20
🚀 Do you want to push to remote repository? (Y/n): y
```

## Notes
- The script must be run from the root of a Git repository.
- Only works on the `main` or `master` branch.
- Commit dates are distributed randomly within the informed interval.
- If you encounter permission or environment errors, make sure Git is installed and accessible.

Made by [hax](https://github.com/emptyhax) & [dan](https://github.com/Dansvn)
