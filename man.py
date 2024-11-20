import datetime
import random


quotes = [
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "Do what you can with all you have, wherever you are. - Theodore Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"
]


quote = random.choice(quotes)

\
today = datetime.date.today()

print(f"📅 Today's Date: {today}")
print(f"💡 Quote of the Day: {quote}")
