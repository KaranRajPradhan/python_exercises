import RPi.GPIO as GPIO
import dht11
import time
from flask import Flask, request, redirect, url_for
from flask import render_template
import random
import json
 
 
app  = Flask(__name__)
 
 
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(15, GPIO.OUT)
 
# read data using pin 14
instance = dht11.DHT11(pin = 14)
 
class Entry:
    def __init__(self, max_temp, max_humidity):
        self.max_temp = max_temp
        self.max_humidity = max_humidity
 
 
stored_temp, stored_humidity = [0,0]
def get_temperature():
    global stored_temp, stored_humidity
    result = instance.read()
 
 
    if result.is_valid():
        Temperature = result.temperature
        Humidity = result.humidity
        stored_temp = Temperature
        stored_humidity = Humidity
        return Temperature, Humidity
    else:
        return None

def compare_conditions(temperature, humidity):
    json_data = open('weather.json').read()
    conditions_dict = json.loads(json_data)
    max_temp = conditions_dict["max_temp"]
    max_humidity = conditions_dict["max_humidity"]
    if temperature > max_temp or humidity > max_humidity:
        return 1
    else:
        return 0
   
 
@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        # entry = Entry(max_temp = request.form["max_temp"], max_humidity = request.form["max_humidity"])
        conditions_dict = {
        "max_temp" : int(request.form["max_temp"]),
        "max_humidity" : int(request.form["max_humidity"])}

        with open('weather.json', 'w') as file_object:
            json_data = json.dumps(conditions_dict)
            file_object.write(json_data)
        

        # if stored_temp > int(entry.max_temp) or stored_humidity > int(entry.max_humidity):
        #     # GPIO.output(15, GPIO.HIGH)
        #     print("RELAY ON")
        # else:
        #     # GPIO.output(15, GPIO.LOW)
        #     print("RELAY OFF")
        return redirect(url_for("home"))
       
    else:
        value = get_temperature()
        # value = random.randint(20,30), random.randint(20,30)
        if value == None:
            Temperature, Humidity = stored_temp, stored_humidity
        else:
            Temperature, Humidity = value
        
        if compare_conditions(Temperature, Humidity) is 1:
            print("RELAY ON")
        else:
            print("RELAY OFF")
 
        return render_template("iot_page.html", temperature = Temperature, humidity = Humidity)
 
 
   
app.run(host='0.0.0.0')