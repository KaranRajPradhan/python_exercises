import paho.mqtt.publish as publish
import json


while True:
    device_name = input("Enter device name: ")
    device_action = input("Enter device action ( on/off ): ")

    message = {"device_name": device_name, "device_action": device_action}
    json_message = json.dumps(message)

    publish.single("iot_control", json_message, hostname = "10.10.20.22")