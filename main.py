import sys
import time
import telepot
import requests
import os

TOKEN = "224522900:AAHAA_XwT7dOFigxwBFl2h78q3WK0PFAm4c"

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    input_text = msg['text']
    flavor = telepot.flavor(msg)
    summary = telepot.glance(msg, flavor=flavor)
    print(flavor, summary)

    if input_text.startswith("https://"):
        cmd = 'youtube-dl --extract-audio --audio-format mp3 \
            --output "audio.%%(ext)s" %summary'%(input_text)
        os.system(cmd)
        sendAudio(chat_id,'audio.mp3')
    else:
        bot.sendMessage(chat_id,input_text)

def sendImage(chat_id):
    url = "https://api.telegram.org/bot%s/sendPhoto"%(TOKEN)
    files = {'photo': open('4.png', 'rb')}
    data = {'chat_id' : chat_id}
    r= requests.post(url, files=files, data=data)
    print(r.status_code, r.reason, r.content)

def sendVideo(chat_id,file_name):
    url = "https://api.telegram.org/bot%s/sendVideo"%(TOKEN)
    files = {'video': open(file_name, 'rb')}
    data = {'chat_id' : chat_id}
    r= requests.post(url, files=files, data=data)
    print(r.status_code, r.reason, r.content)

def sendAudio(chat_id,file_name):
    url = "https://api.telegram.org/bot%s/sendAudio"%(TOKEN)
    files = {'audio': open(file_name, 'rb')}
    data = {'chat_id' : chat_id}
    r= requests.post(url, files=files, data=data)
    print(r.status_code, r.reason, r.content)

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print('Listening ...')

while 1:
    time.sleep(10)