from pyrogram import Client
from pyrogram import Message
from pyrogram import InputPhoneContact
from pyrogram import Filters
import redis
from redis import StrictRedis
import telebot
import os
import sys
import requests
import re
####################
api_id = 739690
api_hash = "427ff8e03bccfd1182961765d9c1bc6b"
gplog = -1001378817892
logger = '937699704:AAF8YsUQvOcPnvkni0_DNCiE3qjmSrIZ9kk'
bot = telebot.TeleBot(logger)
app = Client("9",api_id, api_hash)
database = redis.StrictRedis(host='localhost', port=6379, db=1,charset='UTF-8', decode_responses=True)
redis = database
#####################
@app.on_message()
def cmd(c,message):
    if message.chat.type == "private":
        if redis.sismember('self:markreadall',"mall"):
            if message:
                app.read_history(message.chat.id)

        if database.sismember('self:monshi',message.from_user.id):
            my = app.get_me()
            if my.status == "offline":
                if message:
                    app.send_message(message.chat.id,"{}".format(database.smembers('self:mtext')))
                
app.run()