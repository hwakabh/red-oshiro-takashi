import os
import sys
from random import randint

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

from .restclient import RestClient

print('>>> Starting chatbot programs ...')

# Pre-checking
API_ENDPOINT = 'https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk'
CHAT_API_TOKEN = os.environ.get('CHAT_API_TOKEN')
if not CHAT_API_TOKEN:
    print('>>> Failed to get API Token for TalkAPI endpoints.')
    print('>>> Run `export CHAT_API_TOKEN=\'YOUR_TALK_API_TOKEN\' before running script.')
    print('>>> See details of how to get CHAT_API_TOKEN in API documents: https://a3rt.recruit-tech.co.jp/')
    sys.exit(1)


talk_api = RestClient(uri=API_ENDPOINT, chat_api_token=CHAT_API_TOKEN)


@listen_to(r'^.*こんにちは.*')
def make_response(message):
    msg = message.body['text']
    print('>>> Respongind to message: {}'.format(msg))

    # If message contains some keyword, post whole message to A3RT API
    print('>>> Calling RestClient.get_response_from_api() with user message : {}'.format(message))
    rsp = talk_api.get_response_from_api(user_message=msg)

    message.reply(rsp['results'][0]['reply'], in_thread=True)
