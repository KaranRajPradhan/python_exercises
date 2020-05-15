import paho.mqtt.client as mqtt
import json

hardware_mockup = {"led1": False, "led2": False, "relay1": False}

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + msg.payload.decode("utf-8"))
    json_action_message = msg.payload.decode("utf-8")
    action_message = json.loads(json_action_message)
    device_name = action_message["device_name"]
    device_action = action_message["device_action"]

    if device_name in hardware_mockup.keys():
        if device_action == "on":
            hardware_mockup[device_name] = True
        elif device_action == "off":
            hardware_mockup[device_name] = False
        else:
            print("invalid action")
    else:
        print("invalid device")

    print(hardware_mockup)


mqttc = mqtt.Client()
mqttc.on_message = on_message

mqttc.connect("10.10.20.22", 1883, 60)
mqttc.subscribe("iot_control", 0)

mqttc.loop_forever()