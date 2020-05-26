import json
import requests


class RestClient():

    def __init__(self, uri, chat_api_token):
        self.uri = uri
        self.chat_api_token = chat_api_token
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    
    def post(self, data=None):
        return requests.post(self.uri, data)
    
    def get_response_from_api(self, user_message):
        d = {'apikey': self.chat_api_token, 'query': user_message}
        raw_response = self.post(data=d)
        if raw_response.status_code != 200:
            return '{}'
        else:
            return json.loads(raw_response.text)
