import RPi.GPIO as GPIO
import dht11
import json
from flask import Flask, Response

app = Flask(_name_)

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 17
instance = dht11.DHT11(pin=17)

@app.route('/')
def main():
  result = instance.read()

  while (result.is_valid() != True):
    result = instance.read()

  if result.is_valid():
    templateData = {
      'temperature' : result.temperature,
      'humidity' : result.humidity
  }
  else:
    templateData = {}

  # show to user temperature and humidity values from device
  return Response(json.dumps(templateData), mimetype='application/json')

@app.route('/temperature')
def temperature():
  result = instance.read()
  
  while (result.is_valid() != True):
    result = instance.read()

  if result.is_valid():
    templateData = {
      'temperature': result.temperature
    }
  else:
    templateData = {}

  return Response(json.dumps(templateData), mimetype='application/json')

@app.route('/humidity')
def humidity():
  result = instance.read()

  while (result.is_valid() != True):
    result = instance.read()
  
  if result.is_valid():
    templateData = {
      'humidity': result.humidity
    }
  else:
    templateData = {}

  return Response(json.dumps(templateData), mimetype='application/json')

app.run(debug=True, host='0.0.0.0', port=5000)