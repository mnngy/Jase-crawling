import telegram

TOKEN = "2105426432:AAGYj4RN8P-se94IbzxKV3qHRAxqcwI9UT0"


def get_bot():
    return telegram.Bot(token=TOKEN)


def get_chat_id(bot):
    return bot.getUpdates()[-1].message.chat.id
