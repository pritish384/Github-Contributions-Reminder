import requests
import datetime
import os
import dotenv
import pytz

dotenv.load_dotenv()

# Timezone for India
india_timezone = pytz.timezone("Asia/Kolkata")
today = datetime.datetime.now(india_timezone)


# Function to fetch public events data for the given GitHub username
def get_contributions_data():
    token = os.getenv("GH_PERSONAL_ACCESS_TOKEN")
    query = f"""
    {{
        user(login: "{os.getenv("GH_USERNAME")}") {{
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
    response = requests.post(
        "https://api.github.com/graphql", json={"query": query}, headers=headers
    )

    if response.status_code == 200:
        data = response.json()
        contribution_dates = []
        for week in data["data"]["user"]["contributionsCollection"][
            "contributionCalendar"
        ]["weeks"]:
            for day in week["contributionDays"]:
                if day["contributionCount"] > 0:
                    contribution_dates.append(day["date"])

        return contribution_dates


# Function to send a reminder message via Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage"
    params = {"chat_id": os.getenv("CHAT_ID"), "text": message}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error sending Telegram message: {e}")
        return None


# Main function
def main():
    contribution_dates = get_contributions_data()
    contribution_dates.append(today.strftime("%Y-%m-%d"))
    contribution_dates = sorted(set(contribution_dates))
    dates = [
        datetime.datetime.strptime(date, "%Y-%m-%d") for date in contribution_dates
    ]
    streak = 0
    for i in range(len(dates) - 1, 0, -1):
        if (dates[i] - dates[i - 1]).days == 1:
            streak += 1
        else:
            break

    message = (
        f"🌟 Today's Date: {today.strftime("%d %B, %Y")}\n\n"
        f"🧑‍💻 GitHub Username: {os.getenv('GH_USERNAME')}\n\n"
        f"🔥 Current Streak: {streak} day(s)\n\n"
    )
    if not str(today.date()) in contribution_dates:
        message += (
            "🚨 You haven't made any contributions today!\n\n"
            "📢 Remember to commit your code today to keep your streak alive."
        )
    else:
        message += "🎉 You have made contributions today! 🚀"

    try:
        send_telegram_message(message)
        print("Message sent via Telegram!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
