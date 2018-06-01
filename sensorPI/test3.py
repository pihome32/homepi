import paho.mqtt.subscribe as subscribe
import threading
def print_msg(client, userdata, message):
    print("%s : %s" % (message.topic, message.payload))

def testt():
    subscribe.callback(print_msg, "#", hostname="localhost")


t = threading.Thread(target=testt, args=())
print("dfadfasfasdfdsf")