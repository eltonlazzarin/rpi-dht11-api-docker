import RPi.GPIO as GPIO
import dht11
import json
from flask import Flask, Response

app = Flask(__name__)

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 17
instance = dht11.DHT11(pin=17)

@app.route('/')
def main():

  result = instance.read()

  if result.is_valid():
    templateData = {
        'temperature' : result.temperature,
        'humidity' : result.humidity
    }
  else:
    templateData = { 'empty' }

  # show to user temperature and humidity values from device
  return Response(json.dumps(templateData), mimetype='application/json')

@app.route('/<action>')
def action(action):

  result = instance.read()
  action_result = 'empty'

  if result.is_valid():
    if action == "temperature":
      action_result = result.temperature
    if action == "humidity":
      action_result = result.humidity

  templateData = {
    action : action_result
  }

  return Response(json.dumps(templateData), mimetype='application/json')

app.run(debug=True, host='0.0.0.0', port=5000)