# GitHub Contributions Reminder

GitHub Contributions Reminder is a productivity tool that helps you stay consistent with your daily GitHub contributions. It checks whether you have made any contributions for the day and, if not, sends a notification to your Telegram account as a reminder using telegram bot API.

## Features
- **Daily Contributions Check**: Automatically checks your GitHub account for contributions made on the current day.
- **Telegram Notifications**: Sends a reminder to your Telegram account if no contributions are detected.
- **Automated Workflow**: Runs seamlessly ensuring you never forget to contribute to your GitHub projects.
- **Streak Maintenance**: Helps you maintain your GitHub streak by reminding you to make contributions daily.

## Prerequisites
Before using this tool, ensure you have:
- Python installed.
- A GitHub account.
- A Telegram account and a bot token (you can create a bot using the [BotFather](https://core.telegram.org/bots#botfather)).

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/pritish384/Github-Contributions-Reminder
   cd github-contributions-reminder
   ```

2. Configure your environment variables:
   - **GITHUB_PAT**: Your GitHub personal access token.
   - **GITHUB_USERNAME**: Your GitHub username.
   - **TELEGRAM_BOT_TOKEN**: Your Telegram bot token.
   - **CHAT_ID**: Your Telegram chat ID (the recipient of notifications).

   You can set these variables in a `.env` file:
   ```env
   GITHUB_PAT=your_personal_access_token
   GITHUB_USERNAME=your_github_username
   TELEGRAM_BOT_TOKEN=your_bot_token
   TELEGRAM_CHAT_ID=your_chat_id
   ```

## Usage
1. Run the script:
   ```bash
   python ./src/main.py
   ```
   **Schedule it to run automatically using AWS Lambda, CloudWatch, Linux cron job, or any other scheduling service.**


2. Check your Telegram for notifications if you haven't made a contributions for the day.

## Contributing
Contributions are welcome! If you have ideas for features or improvements, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Telegram Bot API](https://core.telegram.org/bots/api)

---

Stay consistent and keep your GitHub streak alive with GitHub Contributions Reminder!
