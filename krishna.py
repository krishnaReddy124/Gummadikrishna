!pip install adafruit-io
x = "krishnareddy"
y = "aio_qdqe14zU0bg30PE5Rs3Ta5jk0ts4"
from Adafruit_IO import Client, Feed
aio = Client(x,y)
# Create a feed
new = Feed(name='bot312')  # Feed name is given
result = aio.create_feed(new)
result
from Adafruit_IO import Data
# Sending a value to a feed
value = Data(value=0)
value_send = aio.create_data('bot312',value)
!pip install python-telegram-bot
from telegram.ext import Updater,CommandHandler
import requests  # Getting the data from the cloud


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def on(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'ligth is turning on'
    pic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Green_sphere.svg/1024px-Green_sphere.svg.png'
    bot.send_message(chat_id, txt)
    bot.send_photo(chat_id, pic)
    from Adafruit_IO import Data
    value = Data(value=1)
    value_send = aio.create_data('bot312',value)

def off(bot,update):
    url = get_url()
    chat_id = update.message.chat_id
    txt = 'ligth is turning off'
    pic = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTuueKIndqjMG0rlzPZrO0UUFP6ts8b_CrUIQ&usqp=CAU'
    bot.send_message(chat_id, txt)
    bot.send_photo(chat_id, pic)
    from Adafruit_IO import Data
    value = Data(value=0)
    value_send = aio.create_data('bot312',value)


u = Updater('1284733152:AAFiPcuXLwv1BSzr5J5C6GCWYjJBjJNQ4N8')
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
u.start_polling()
u.idle()
