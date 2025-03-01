import telegram
from dotenv import load_dotenv
import os


load_dotenv()
TG_API = os.getenv('TG_API')
bot = telegram.Bot(token=TG_API)
bot.send_message(chat_id=-1002251218602, text="Привет пользователь!")
bot.get_me()