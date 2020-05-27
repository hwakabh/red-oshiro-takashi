from slackbot.bot import Bot


if __name__ == '__main__':
    print('>>> main.py called from slackbot_settings.py')
    bt = Bot()
    print('>>> Starting slackbot ...')
    bt.run()
