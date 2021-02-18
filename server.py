import paho.mqtt.client as mqtt
import sensor as sensor
import get_result as parse
import time

#broker = "iot.eclipse.org"
#broker = "test.mosquitto.org"
broker = "echontrol" #local



def create_msg(change_type, change_amount):
    #we gonna do everything to cut the message (not actually everything, but THIS will cut it considerably)
    if change_type == "increase":
        parsed_type = 1
    elif change_type == "decrease":
        parsed_type = 2
    else:
        parsed_type = 1
        print("msg parsing error: unexpected type:", change_type)
    
    parsed_amount = change_amount
    
    msg = str(parsed_type) + " " + str(parsed_amount)
    print("parse msg result:", msg)
    return msg
def get_sensor():
    try:
        return sensor.main()
    except:
        get_sensor()

def on_subscribe(client, userdata, mid, granted_qos):
    print("subbed to:", mid, granted_qos)
def on_connect(subscriber, userdata, flags, rc):
    print("Connected with result code " + str(rc))
def on_message_get_ip(subscriber,userdata, msg):
    global connected_flag, server, client_ip
    received_message = str(msg.payload)
    client_ip = received_message
    
    print("1. Was connected:", client_ip)
    if connected_flag == False:
        client.loop_stop()
    connected_flag = True
def on_message_main(subscriber,userdata, msg):
    received_message = str(msg.payload)
    print("On_message:", received_message)
def on_publish(client, userdata, mid):
    print("Published:", client, userdata, mid)
def on_disconnect(client, userdata, rc):
    if rc == 1:
        print("Sudden disconnect!")
        exit(1)
    print("Disconnected", client)


print("start_connection")
connected_flag = False
#client ip isn't really ip - in fact it's just a welcoming message by client
client_ip = None
client = mqtt.Client()
client.on_subscribe = on_subscribe
client.on_connect = on_connect
client.on_message = on_message_get_ip
client.on_publish = on_publish
client.on_disconnect = on_disconnect
client.connect(broker, 1883, 60)
client.subscribe("echontrol_main", qos=1)
client.loop_start()
while client_ip == None:
    time.sleep(.5)
    print("Waiting for ip cast", client_ip)
client.disconnect()
client = 0
client = mqtt.Client()


client.on_message = on_message_main
client.on_publish = on_publish
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_disconnect = on_disconnect
client.connect(broker, 1883, 60)
client.subscribe("echontrol_main", qos=1)

last2 = get_sensor()
last1 = get_sensor()
new = get_sensor()
print(last2, last1, new)
print("Initialization complete. Start main module...")
client.loop_start()
while 1:
    if True: #don't ask me why
        parse_result = parse.main(last2, last1, new) # [0] = success(True/False/etc); [1] = "increase"/"decrease"(str); [2] = amount(int)
        print(parse_result) #debug data
        try:
            if parse_result[0] == True:
                #print(parse_result[2])
                client.publish("echontrol_main", create_msg(parse_result[1], parse_result[2]), qos=1)
        except:
           print("error in hardware...")
        last2 = last1
        last1 = new
        new = get_sensor()
            


