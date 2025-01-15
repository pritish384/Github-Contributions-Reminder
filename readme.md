# GitHub Contributions Reminder

GitHub Contributions Reminder is a productivity tool that helps you stay consistent with your daily GitHub contributions. It checks whether you have made any contributions for the day and, if not, sends a notification to your Telegram account as a reminder using telegram bot API.

## Features
- **Daily Contributions Check**: Automatically checks your GitHub account for contributions made on the current day.
- **Telegram Notifications**: Sends a reminder to your Telegram account if no contributions are detected.
- **Automated Workflow**: Runs seamlessly ensuring you never forget to contribute to your GitHub projects.
- **Streak Maintenance**: Helps you maintain your GitHub streak by reminding you to make contributions daily.

## Prerequisites
Before using this tool, ensure you have:
- A GitHub account.
- A Telegram account and a bot token (you can create a bot using the [BotFather](https://core.telegram.org/bots#botfather)).

## Usage
1. Fork this repository: Click the Fork button in the top right corner of the repository.

2. Configure your environment variables in repository secrets:
   - **GH_PERSONAL_ACCESS_TOKEN**: Your GitHub personal access token.
   - **GH_USERNAME**: Your GitHub username.
   - **TELEGRAM_BOT_TOKEN**: Your Telegram bot token.
   - **CHAT_ID**: Your Telegram chat ID (the recipient of notifications).

   You can set these variables in a `.env` file:
   ```env
   GH_PERSONAL_ACCESS_TOKEN=your_personal_access_token
   GH_USERNAME=your_github_username
   TELEGRAM_BOT_TOKEN=your_bot_token
   CHAT_ID=your_chat_id
   ```

3. Setup cron job as per your choice to run the script daily in workflow file:
   ```yaml
   on:
     schedule:
       - cron: '0 0 * * *'
   ```

4. Check your Telegram for notifications if you haven't made a contributions for the day.

## Contributing
Contributions are welcome! If you have ideas for features or improvements, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Telegram Bot API](https://core.telegram.org/bots/api)

---

Stay consistent and keep your GitHub streak alive with GitHub Contributions Reminder!
