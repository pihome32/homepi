import paho.mqtt.client as mqtt
import time
from tentacle_pi.AM2315 import AM2315
import json

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	am = AM2315(0x5c,"/dev/i2c-1")
	temperature, humidity, crc_check = am.sense()
	message=str(temperature) + ' ' + str(humidity)
	client.publish("home/pi/sensor/am2315", message)
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	#client.subscribe("home/sensor/ask_am2315")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	am = AM2315(0x5c,"/dev/i2c-1")
	temperature, humidity, crc_check = am.sense()
	message=str(temperature) + ' ' + str(humidity)
	client.publish("home/sensor/am2315", message)
	

client = mqtt.Client()
client.on_connect = on_connect
#client.on_message = on_message

client.connect("localhost", 1883, 60)

am = AM2315(0x5c,"/dev/i2c-1")
temperature, humidity, crc_check = am.sense()
message = {"temperature":temperature, "humidity":humidity}
message= json.dumps(message)
#message=str(temperature) + ' ' + str(humidity)
client.publish("home/pi/sensor/am2315", message)


