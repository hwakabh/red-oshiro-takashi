import os
import sys


API_TOKEN = os.environ.get('SLACK_API_TOKEN')
if not API_TOKEN:
    print('>>> Failed to retrive API_TOKEN for slackbot.')
    print('>>> Run `export SLACK_API_TOKEN=\'YOUR_TOKEN_PUBLISH_BY_SLACK_ADMIN\' before running this script.')
    sys.exit(1)

print('>>> Initializing programs ...')
PLUGINS = ['plugins']
