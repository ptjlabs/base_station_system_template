
#import context
import paho.mqtt.subscribe as subscribe
import json
import time
import random





def main():
    while True:
        try:
            m = subscribe.simple("/apt326/#", hostname="mqtt-broker",retained=False)
            print('Message from: {} '.format(m.topic))
            print('Data: {} '.format(m.payload))
        except:
            print(f"Not able to connect to broker at this time...")




if __name__=='__main__':
    main()