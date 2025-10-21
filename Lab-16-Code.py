from flask import Flask, render_template
from gpiozero import LED

app = Flask(__name__)
led1 = LED(18) # Change to match your LED!
led2 = LED(23)
led3 = LED(24)

@app.route('/')
def index():
    return render_template('HTML Code.html')

@app.route('/LED1/<action>')
def LED1Control(action):
    if action == 'on':
        led1.on()
        return 'LED Turned On'
    elif action == 'off':
        led1.off()
        return 'LED Turned Off'
    else:
        return 'Invalid Action'

@app.route('/LED2/<action>')
def LED2Control(action):
    if action == 'on':
        led2.on()
        return 'LED Turned On'
    elif action == 'off':
        led2.off()
        return 'LED Turned Off'
    else:
        return 'Invalid Action'

@app.route('/LED3/<action>')
def LED3Control(action):
    if action == 'on':
        led3.on()
        return 'LED Turned On'
    elif action == 'off':
        led3.off()
        return 'LED Turned Off'
    else:
        return 'Invalid Action'

if __name__ == '__main__':
    app.run(host='10.1.0.68', port=80)