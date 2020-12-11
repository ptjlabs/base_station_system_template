
# from flask import Flask
# import paho.mqtt.client as mqtt

# app = Flask(__name__)

# topic = '/cot/openTopic/#'
# topic2 = '/cot/mqttServer'
# port = 5000

# def on_connect(client, userdata, rc):
#     client.subscribe(topic)
#     client.publish(topic2, "STARTING SERVER")
#     client.publish(topic2, "CONNECTED")


# def on_message(client, userdata, msg):
#     client.publish(topic2, "MESSAGE")


# @app.route('/')
# def hello_world():
#     return 'Hello World! I am running on port ' + str(port)

# if __name__ == '__main__':
#     client = mqtt.Client()
#     #client.username_pw_set(username, password)
#     client.on_connect = on_connect
#     client.on_message = on_message
#     client.connect('localhost', port=1883)
#     client.loop_start()

#     app.run(host='0.0.0.0', port=port, debug=True)
import paho.mqtt.client as mqtt
import socket
import requests

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/apt326/bedroom/#")



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    url = 'localhost/api/v2/ingest'
    payload = dict(topic=msg.topic,data=str(msg.payload))
    requests.post(url, data=payload)
    #print(msg.topic+" "+str(msg.payload))
    #print(socket.gethostname())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
instance = [1,2,3,4]
client.connect(socket.gethostname(), 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

