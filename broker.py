import paho.mqtt.client as mqtt
from getch import getch

TOPIC_PUSH = "iot/data/iotmmsp1942978066trial/v1/85732072-22b7-4cd1-ae8f-d363975c0f91"
TOPIC_PULL = "iot/push/iotmmsp1942978066trial/v1/85732072-22b7-4cd1-ae8f-d363975c0f91"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if (rc == 0):
        print("Connected with success")
    else:
        print("Connection aborted")
    #FromDevice
    client.subscribe((TOPIC_PUSH, 1))
    #ToDevice
    client.subscribe((TOPIC_PULL, 1))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

#########################################
#   MAIN LOGIC
#########################################

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("capllkmg", password="TYk-UHLw95TH")

client.connect("m14.cloudmqtt.com", 15839, 60)

client.loop_start()

while True:
    key = getch()
    print("Pressed : " + key)

    if key != "":
        client.publish(TOPIC_PULL, "")

    if key == "q":
        break
