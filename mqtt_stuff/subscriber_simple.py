import paho.mqtt.client as mqtt

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + msg.payload.decode("utf-8"))

mqttc = mqtt.Client()
mqttc.on_message = on_message

mqttc.connect("10.10.20.22", 1883, 60)
mqttc.subscribe("python_chatbox", 0)

mqttc.loop_forever()