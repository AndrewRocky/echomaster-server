import paho.mqtt.client as mqtt

def on_connect(subscriber, userdata, flags, rc):
    subscriber.subscribe("echontrol_main", qos=1)
    print("Connected with result code " + str(rc))
def on_message(subscriber,userdata, msg):
    global connected_flag, server, client_ip
    received_message = str(msg.payload)
    if recieved_message != None:
        client_ip = received_message
    connected_flag = True
    #server.connect(client_ip, 1883, 60)
    print("1. Connected to", client_ip)

def init():
    print("start_connection")
    connected_flag = False
    client_ip = None
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("echontrol", 1883, 60)
    #server = mqtt.Client()
    print("Waiting for server...")
    while client_ip == None:
        client.loop(.2)
        print("zaloop", client_ip)
    print("2. Connected to", client_ip)
