from flask import Flask, request

import fields, utility

app = Flask(__name__)

import sched
import datetime, time


class PeriodicScheduler(object):
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def setup(self, interval, action, actionargs=()):
        action(*actionargs)
        self.scheduler.enter(interval, 1, self.setup,
                             (interval, action, actionargs))

    def run(self):
        self.scheduler.run()

at, rt = utility.get_token()

# This is the event to execute every time
def refresh_token():
    at, rt = utility.get_token()

@app.route('/api/doctors')
def doctor_name_guess():
    task = request.args.get('task')
    user_id = request.args.get('user_id')
    if task == 'get_doctors_by_name':
        name = request.args.get('doc_name')
        fields.get_doctors_by_name(at, name)



if __name__ == "__main__":
    shed = PeriodicScheduler()
    shed.setup(3000, refresh_token)
    shed.run()
    app.run(port=5008)