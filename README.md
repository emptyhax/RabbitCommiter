# RabbitCommiter

RabbitCommiter is a command-line tool that allows you to generate multiple empty Git commits on a specific date. This can be useful for backfilling commit history, testing, or maintaining contribution streaks. The tool is interactive and supports both Windows and Unix-like systems.

## Features
- Generate up to 100 empty commits for a specified date
- Cross-platform support (Windows, Linux, MacOS)
- Randomized commit messages for each commit
- Interactive prompts for user-friendly operation
- Option to push commits to the remote repository after creation

## Requirements
- Python 3.6+
- Git must be installed and available in your system's PATH
- An existing Git repository (run inside a Git project directory)

## Usage
1. **Clone or download this repository.**
2. **Navigate to the project directory in your terminal.**
3. **Run the script:**
   ```bash
   python main.py
   ```
4. **Follow the interactive prompts:**
   - Confirm your operating system
   - Enter the commit date in `DD:MM:YYYY` format (e.g., 02:04:2024)
   - Enter the number of empty commits to generate (0-100)
   - Optionally, push the commits to your remote repository

## Example
```
$ python main.py

📅 Commit date (DD:MM:YYYY): 15:05:2024
🔢 Number of commits (0-100): 10
🚀 Do you want to push to remote repository? (Y/n): y
```

## Notes
- The script must be run from the root of a Git repository.
- Only works on the `main` or `master` branch.
- Commits are created with incremented timestamps (by minutes).
- If you encounter permission or environment issues, ensure Git is properly installed and accessible.

made by [hax](https://github.com/emptyhax) & [dan](https://github.com/Dansvn)