from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
from bs4 import BeautifulSoup as bs
import random
import json

TOKEN = "884654954:AAHXv-EGFqx_cFgvT3CzHMmUPPZ1LhZlW6c"

def get_url_bop():
    contents = requests.get("https://random.dog/woof.json").json()
    url = contents["url"]
    return url

def get_url_joke():
    joke_num = random.randint(1,101)
    link = f"https://xkcd.com/{joke_num}/"
    html_data = requests.get(link).content
    soup = bs(html_data)

    image_div = soup.find("div", {"id":"comic"})
    image_url = image_div.find("img").get("src")
    final_link = "https:" + image_url

    return final_link

def get_url_weather():
    website_url = "https://www.metaweather.com/api/location/2295420/"
    website_data = requests.get(website_url).json()
    print(website_data)
    current_weather = str(website_data['consolidated_weather'][0]['the_temp'])
    final_text = f"Temperature today is {current_weather} degrees"

    return(final_text)



def bop(bot, update):
    url = get_url_bop()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def joke(bot, update):
    url = get_url_joke()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def weather(bot, update):
    url = get_url_weather()
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=url)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('joke',joke))
    dp.add_handler(CommandHandler('weather',weather))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()