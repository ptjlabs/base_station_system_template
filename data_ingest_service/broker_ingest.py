
#import context
import paho.mqtt.publish as publish
import json
import time
import random





def main():
    while True:
        m = subscribe.simple("/apt326/#", hostname="mqtt-broker",retained=False)
        print('Message from: {} '.format(m.topic))
        print('Data: {} '.format(m.payload))



if __name__=='__main__':
    main()