#!/home/YOURUSERNAME/code/Python/venvs/env1/bin/python

import requests
import sys

def send_to_telegram(message):

    apiToken = 'YOURAPITOKEN'
    chatID = 'YOURCHATID'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)
