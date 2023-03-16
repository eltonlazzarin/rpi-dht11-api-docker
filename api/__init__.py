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

  retries = 0
  while (result.is_valid() is not True and retries <= 3):
    result = instance.read()
    retries += 1 

  if result.is_valid():
    templateData = {
      'temperature' : result.temperature,
      'humidity' : result.humidity
  }
    # show to user temperature and humidity values from device
    return Response(json.dumps(templateData), mimetype='application/json')
  else:
    # show bad readings response from sensors
    return Response("No response from sensors", status=404, mimetype='text/plain')

@app.route('/temperature')
def temperature():
  result = instance.read()

  retries = 0
  while (result.is_valid() is not True and retries <= 3):
    result = instance.read()
    retries += 1 

  if result.is_valid():
    templateData = {
      'temperature': result.temperature
  }
    return Response(json.dumps(templateData), mimetype='application/json')
  else:
    return Response("No response from sensor", status=404, mimetype='text/plain')

@app.route('/humidity')
def humidity():
  result = instance.read()

  retries = 0
  while (result.is_valid() is not True and retries <= 3):
    result = instance.read()
    retries += 1

  if result.is_valid():
    templateData = {
      'humidity': result.humidity
  }
    return Response(json.dumps(templateData), mimetype='application/json')
  else:
    return Response("No response from sensor", status=404, mimetype='text/plain')

app.run(debug=True, host='0.0.0.0', port=5000)
