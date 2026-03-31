import asyncio
import os
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

alert_message = "🚨 Alert! Suspicious activity detected.\nPlease check the attached video."
video_file_path = r"path_to_your_video.mp4"  


async def send_alert_with_video():
    bot = Bot(token=BOT_TOKEN)
    try:
        await bot.send_message(chat_id=CHAT_ID, text=alert_message)
        print("Alert message sent successfully!")

        with open(video_file_path, "rb") as video_file:
            await bot.send_video(chat_id=CHAT_ID, video=video_file, caption="🔍 Video Footage")
            print("Video clip sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(send_alert_with_video())