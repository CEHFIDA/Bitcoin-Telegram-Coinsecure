import urllib2
import re
import time
import subprocess
import telepot
import datetime
import requests
import json


def handle(msg):
        chat_id = msg['chat']['id']
        command = msg['text']

        print "Got Command : %s " %command
	if command=="btc":
			url= "https://www.google.com.pk/search?q=bitcoin+to+pkr"
			req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
			con = urllib2.urlopen( req )
			Text=con.read()
			position=re.search("1 Bitcoin =",Text)
			res = float(Text[position.end():position.end()+9])
			axx = '1 BTC : '+str(res)+' PKR'
			bot.sendMessage(chat_id,str(axx))
	elif command == "urdubit":
			res = requests.get('https://api.blinktrade.com/api/v1/PKR/ticker?crypto_currency=BTC')
			#print(res.text)
			j = json.loads(res.text)
			sell = j['message']['bid']
			stringsell = str(sell)
			buy = j['message']['lastPrice']
			timestamp = int(j['message']['timestamp'])
			date_time = datetime.datetime.now()
			datex = date_time.date()  # gives date
			timex = date_time.time()  # gives time
			xxx = "Time:"+str(timex.hour)+":"+str(timex.minute)+", BTC PRICE: "+str(sell)[0:6]+" PKR "
			print stringsell
			bot.sendMessage(chat_id,str(xxx))
	elif command.startswith('notify'):
		notes = command[6:]
		print notes
		while True:
			url= "https://www.google.com.pk/search?q=bitcoin+to+pkr"
			req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
			con = urllib2.urlopen( req )
			Text=con.read()
			position=re.search("1 Bitcoin =",Text)
			res = float(Text[position.end():position.end()+9])
			axx = '1 BTC : '+str(res)+' PKR'
			sleep(60) # Every Minute Update # Please Note Need to edit this part FUXING BUG
			if str(res) >= notes: 
				bot.sendMessage("Notification Alert: ",str(axx))
				bot.sendMessage(chat_id,str(axx))



	else:
		aa=subprocess.check_output(command,shell=True)
		bot.sendMessage(chat_id,aa)

bot = telepot.Bot('PUT API KEY HERE')
bot.message_loop(handle)
print 'i am listening .....'

while 1:
        time.sleep(10)

