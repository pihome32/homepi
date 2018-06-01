import paho.mqtt.client as mqtt
import time
import json
from sendmsg import earthquake
from paper import build_image


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("home/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, message):
    print("message received  ", str(message.payload.decode("utf-8")), \
          "topic", message.topic, "retained ", message.retain)
    if (message.topic == "home/paper/create"):
        print("test")
        build_image(message.payload)
    if (message.topic == "home/message/ask/earthquake"):
        for msg in earthquake():
            print(msg)
            client.publish("home/message/new", json.dumps(msg))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()

