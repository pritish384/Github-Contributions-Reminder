import requests
import datetime
import os
import dotenv
import pytz

# Load environment variables once
dotenv.load_dotenv()

# Timezone for India
india_timezone = pytz.timezone('Asia/Kolkata')
today = datetime.datetime.now(india_timezone)

# Fetch GitHub contributions data
def get_contributions_data():
    token = os.getenv("GH_PERSONAL_ACCESS_TOKEN")
    username = os.getenv("GH_USERNAME")
    query = f"""
    {{
        user(login: "{username}") {{
            contributionsCollection(from: "{today.year}-01-01T00:00:00Z", to: "{today.year}-12-31T00:00:00Z") {{
                contributionCalendar {{
                    weeks {{
                        contributionDays {{
                            date
                            contributionCount
                        }}
                    }}
                }}
            }}
        }}
    }}
    """
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post("https://api.github.com/graphql", json={"query": query}, headers=headers)

    if response.status_code == 200:
        data = response.json()
        contribution_dates = {
            day["date"]
            for week in data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
            for day in week["contributionDays"]
            if day["contributionCount"] > 0
        }
        return contribution_dates
    else:
        print(f"Error fetching contributions: {response.status_code}")
        return set()

# Send a Telegram message
def send_telegram_message(message):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error sending Telegram message: {e}")
        return None

# Calculate the streak starting from today
def calculate_streak(contribution_dates):
    streak = 0
    current_day = today.date()

    # Start from today and go backwards
    while str(current_day) in contribution_dates:
        streak += 1
        current_day -= datetime.timedelta(days=1)

    return streak

# Main function
def main():
    # Get contributions data
    contribution_dates = get_contributions_data()
    contribution_today = str(today.date()) in contribution_dates
    contribution_dates.add(today.strftime("%Y-%m-%d"))
    
    # Calculate streak starting from today
    streak = calculate_streak(contribution_dates)

    # Prepare the message
    message = (
        f"🌟 Today's Date: {today.strftime('%d %B, %Y')}\n\n"
        f"🧑‍💻 GitHub Username: {os.getenv('GH_USERNAME')}\n\n"
        f"🔥 Current Streak: {streak} consecutive day(s)\n\n"
    )

    if not contribution_today:
        message += "🚨 You haven't made any contributions today!\n\n📢 Remember to commit your code today to keep your streak alive."
    else:
        message += "🎉 You have made contributions today! 🚀"

    # Send reminder via Telegram
    send_telegram_message(message)
    print("Message sent via Telegram!")

if __name__ == "__main__":
    main()
