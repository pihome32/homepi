#!/usr/bin/python
#import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


def mqttSend(topic,data):
    publish.single("paho/test/single", "boo", hostname="localhost", port=1883)
    print("psdfassssssssssss")

class MyMQTTClass(mqtt.Client):

    def on_connect(self, mqttc, obj, flags, rc):
        print("rc: "+str(rc))

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        mqttSend("yes",22222222222)

    def on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def run(self):
        self.connect("localhost", 1883, 60)
        self.subscribe("home/sensorPI/ask/#", 0)

        rc = 0
        while rc == 0:
            rc = self.loop()
        return rc

#print("rc: "+str(rc))
def mqttListener():
     mqttc = MyMQTTClass()
     rc = mqttc.run()






