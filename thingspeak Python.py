import urllib.request
import requests
import threading
import json

import random


# Define a function that will post on server every 15 Seconds

def thingspeak_post():
    threading.Timer(15,thingspeak_post).start()
    val=random.randint(1,30)
    URl='https://api.thingspeak.com/update?api_key='
    KEY='WRITE KEY XXXXXXXXXXX  '
    HEADER='&field1={}&field2={}'.format(val,val)
    NEW_URL=URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)

def read_data_thingspeak():
    URL='https://api.thingspeak.com/channels/557500/fields/1.json?api_key='
    KEY='READ KEY XXXXX  '
    HEADER='&results=2'
    NEW_URL=URL+KEY+HEADER
    print(NEW_URL)

    get_data=requests.get(NEW_URL).json()
    #print(get_data)
    channel_id=get_data['channel']['id']

    feild_1=get_data['feeds']
    #print(feild_1)

    t=[]
    for x in feild_1:
        #print(x['field1'])
        t.append(x['field1'])

if __name__ == '__main__':
    #thingspeak_post()
    read_data_thingspeak()


