import time

from jase import get_last_page, get_products, get_latest_product_name
from telegram_bot import get_bot, get_chat_id
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

bot = get_bot()
chat_id = get_chat_id(bot)


while True:
    last_page = get_last_page()
    products = get_products(last_page)

    latest_product_name = get_latest_product_name(products)

    with open(os.path.join(BASE_DIR, "latest.txt"), "r+") as f_read:
        before_product_name = f_read.readline()
        if before_product_name != latest_product_name:
            print("새로운 제품이 올라왔어요")
            bot.sendMessage(chat_id=chat_id, text="새로운 제품이 올라왔어요")
        f_read.close()

    with open(os.path.join(BASE_DIR, "latest.txt"), "w+") as f_write:
        f_write.write(latest_product_name)
        f_write.close()
