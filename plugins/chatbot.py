import os
import sys
from random import randint

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

from .restclient import RestClient

print('Starting chatbot programs ...')

API_ENDPOINT = 'https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk'
CHAT_API_TOKEN = os.environ.get('CHAT_API_TOKEN')
if not CHAT_API_TOKEN:
    print('>>> Failed to get API Token for TalkAPI endpoints.')
    print('>>> Run `export CHAT_API_TOKEN=\'YOUR_TALK_API_TOKEN\' before running script.')
    print('>>> See details of how to get CHAT_API_TOKEN in API documents: https://a3rt.recruit-tech.co.jp/')
    sys.exit(1)


talk_api = RestClient(uri=API_ENDPOINT, chat_api_token=CHAT_API_TOKEN)
bot_message = talk_api.get_response_from_api(user_message='初めましてこんばんは')
print(bot_message)