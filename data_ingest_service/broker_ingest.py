
#import context
import paho.mqtt.client as mqtt
import json
import time
import random
import uuid

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)


def main():
    client_name  = f"starfox:{uuid.uuid4()}"
    client = mqtt.Client(client_name)
    while True:

        client.on_message = on_message
        client.connect(host="base_station_mqtt-broker_1",port=1883,keepalive=60)
        client.loop_start()

        client.subscribe("cot/research")
        time.sleep(2)



            
if __name__ == '__main__':
        main()