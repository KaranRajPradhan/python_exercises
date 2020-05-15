import paho.mqtt.publish as publish

username = input("Enter your username: ")

while True:
    message = input("Enter your message: ")

    message_to_send = f"{username} : {message}"

    publish.single("iot_control", message_to_send, hostname='10.10.20.22')