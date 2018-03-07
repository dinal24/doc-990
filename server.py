from flask import Flask, request

import actions, utility, faq

app = Flask(__name__)

import sched
import datetime, time, json


class PeriodicScheduler(object):
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def setup(self, interval, action, actionargs=()):
        action(*actionargs)
        self.scheduler.enter(interval, 1, self.setup,
                             (interval, action, actionargs))

    def run(self):
        self.scheduler.run()

# at, rt = utility.get_token()

# This is the event to execute every time
def refresh_token():
    at, rt = utility.get_token()

@app.route('/api/doc990')
def doctor_name_guess():
    task = request.args.get('task')
    user_id = request.args.get('user_id')
    if task == 'get_doctors_by_name':
        name = request.args.get('doc_name')
        response = actions.find_doctor_by_name(name)
        return json.dumps(response)
    elif task == 'faq':
        q = request.args.get('last_nli')
        bot_id = request.args.get('bot_id')
        session = faq.UserSession(user_id)
        response, action = session.get_response(q, bot_id)

        response_dict = {
            "option": "default",
            "values": {
                "bot_say": response,
                "action": action
            }
        }
        return json.dumps(response_dict)



if __name__ == "__main__":
    app.run(port=5010)