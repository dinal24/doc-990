from random import choice, randint
import _thread, time
import apiai
from pymongo import MongoClient
import json
import logging
import requests
import copy
# translator functions
import logging
import requests
import json


CLIENT_ACCESS_TOKEN = "dc72770405c44a6abdcb5dea5001bdaa"

client = MongoClient('localhost', 27017)
db = client['doc-990']

BF_ACCESS_TOKEN = {
    "": ""
}
BOT_ID = "420"
BF_HOOK = "https://botfactoryai.com/send_messages"

def call_webhook(params):
    time.sleep(3)
    requests.get(BF_HOOK, params=params, timeout=30)

KEY = "AIzaSyA4JjjlNVc1NOWd_H8VX2XFil0QEpz8wrI"
GAPI_URL = "https://translation.googleapis.com/language/translate/v2?key={0}"

def translate_api_call(query, target='en'):
    URL = GAPI_URL.format(KEY)
    data = {
        'q': query,
        'target': target
    }
    response = json.loads(requests.post(URL, data=data).text)
    result = response.get('data').get('translations')[0].get('translatedText')

    logging.warning("incoming: {} || translated: {}".format(query, result))
    return result

emoji = {
    ":D" : u"😀",
    ":)" : u"🙂",
    ";)" : u"😉",
    "^_^": u"😊",
    "-_-": u"😑",
    ":/" : u"😕",
    ":|" : u"😐",
    "B)" : u"😎"
}

def replace_ae(text, emoji=emoji):
    for em in emoji.keys():
        text = text.replace(em, emoji[em])

    return text


def translate_to_en(lang, query):
    if lang == 'si':
        query = translate_api_call(query, 'en')

    return query


def translate_from_en(lang, query):
    if lang == 'si':
        query = replace_ae(query)
        query = translate_api_call(query, 'si')

    return query

class UserSession:
    def __init__(self, user_id, target='en'):
        self.ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
        self.user_id = user_id
        self.target = target

    def __call_hook(self, node, bot_id):
        params = {
            "access_token": BF_ACCESS_TOKEN[bot_id],
            "bot_id": bot_id,
            "node_id": node,
            "user_id": self.user_id
        }
        _params = copy.deepcopy(params)
        _thread.start_new_thread(call_webhook, (_params,))

    def __make_action(self, action, bot_id):
        node = None
        state_flow = "flow"
        if action == "call_button":
            pass

        # Disabled prompting stuff
        # if not node and self.data['small_talk_count'] > 3 + randint(50, 60) and self.data['required']:
        #     node = node_map[choice(self.data['required'])]http://image.com/files/8813/5551/7470/cruise-ship.png

        return state_flow

    def __resolve_intent(self, query):
        ai_request = self.ai.text_request()
        ai_request.lang = 'en'
        ai_request.session_id = self.user_id
        ai_request.query = query
        response_json = ai_request.getresponse()
        interpret = json.loads(response_json.read().decode())
        action = interpret.get('result', {}).get('action', 'flow')
        response = interpret.get('result', {}).get('fulfillment', {}).get('speech', '')

        return action, response

    def get_response(self, query, bot_id, extras=None):
        query = translate_to_en(self.target, query)

        action, response = self.__resolve_intent(query)
        state_flow = self.__make_action(action, bot_id)

        if not response:
            # Connect agent
            pass
        else:
            response = translate_from_en(self.target, query=response)

        logging.warning("Action: {} | Speech: {}".format(action, response))
        return response, action
