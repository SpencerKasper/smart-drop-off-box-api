from flask import Flask, render_template, request, redirect, url_for, make_response
import RPi.GPIO as GPIO

from command_sns_listener import CommandListener

relay = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)
GPIO.output(relay, 0)
app = Flask(__name__)


listener = CommandListener('smart_drop_off_box_queue.fifo', region_name='us-east-1')
listener.listen()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<changepin>', methods=['POST'])
def reroute(change_pin):
    lock_on_off_pin_value = int(change_pin)
    if lock_on_off_pin_value == 1:
        print("ON")
        GPIO.output( relay , 1)                
    elif lock_on_off_pin_value == 2:
        print("OFF")
        GPIO.output(relay, 0)
    return make_response(redirect(url_for('index')))


app.run(debug=True, host='0.0.0.0', port=8000)