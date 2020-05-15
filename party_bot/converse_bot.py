#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.

This program is dedicated to the public domain under the CC0 license.

This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
#import game_host

#pip install -r requirements.txt 
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

answers = {"counter":0}

questions = ["Do you want to split the bill equally?"]
equal_split_questions = ["How much is the bill?",
                        "How many people are in the table?"]
unequal_split_questions = ["Food bill?",
                           "Drinks bill?",
                           "No. of people ate?",
                           "No. of people drank?"]


def greet(msg):
    greeting_msg = "Hello I am a partybot, I will help you split the bill, while you are too drunk to do the math."
    human_greetings = ["hello", "hi", "hey"]
    if msg.lower() in human_greetings:
        return greeting_msg
    else:
        return None

def negative(msg):
    if msg.lower() == "exit":
        answers["counter"] = 0
        return "Thank you!"
    else:
        return None

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def bill_equal_split(answers):
    total_bill = int(answers[0])
    no_of_people = int(answers[1])

    per_head = total_bill / no_of_people
    reply = f"Per head bill is {per_head}"
    
    return reply

def method_decider(answers):
    if answers.get(0) == "yes":
        questions.pop()
        questions.extend(equal_split_questions)
        answers["counter"] = 1
    elif answers.get(0) == "no":
        questions.pop()
        questions.extend(unequal_split_questions)
        answers["counter"] = 1
    else:
        pass

def echo(bot, update):
    """Echo the user message."""
    msg = update.message.text
    #output = game_host.identify_msg(msg)
    greeting = greet(msg)
    thank_you = negative(msg)
    method_decider(answers)
    if greeting:
        answer = greeting
    elif thank_you:
        answer = thank_you
    elif answers["counter"] == len(questions):
        question_number = answers["counter"] - 1
        answers[question_number] = msg
        answer = bill_equal_split(answers)
        answers["counter"] = 0
        print(answers)
    else:
        counter = answers["counter"]

        if counter > 0:
            if counter == 2:
                if answers[0] == "no":
                    
            question_number = counter - 1
            answers[question_number] = msg
        else:
            pass
        question = questions[counter]
        answers["counter"] += 1
        answer = question
    update.message.reply_text(answer)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    TOKEN = "884654954:AAHXv-EGFqx_cFgvT3CzHMmUPPZ1LhZlW6c"
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()