import paho.mqtt.client as mqtt
class mqttClient:

    def on_connect(self, master, obj, flags, rc):
        self.master.subscribe('home/sensorPI/ask')
        self.master.publish('sdfsdf/',23)


    def on_message(self, master, obj, msg):
        print(str(msg.payload))

    def __init__(self,master):
        self.master=master
        self.master.on_connect=self.on_connect
        self.master.on_message=self.on_message
        self.master.connect("localhost", 1883, 60)

    def publish(self,master):
        self.master.publish('sdfsdf')



client=mqtt.Client()
ob1=mqttClient(client)
client.loop_forever()

