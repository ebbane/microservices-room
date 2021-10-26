
import random
import time
from test_dictionnaire import *

from paho.mqtt import client as mqtt_client

BROKER_ADDRESS ="10.3.141.1"
PORT = 5672
TOPIC = "microservices/room"
CLIENT_NAME = "ROOM"


def connect_mqtt():
    def on_connect(client, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(CLIENT_NAME)
    client.on_connect = on_connect
    client.connect(BROKER_ADDRESS, PORT)
    return client


def publish(client):

    while True:
        time.sleep(1)
        msg = dictionnaire
        result = client.publish(TOPIC, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{TOPIC}`")
        else:
            print(f"Failed to send message to topic {TOPIC}")
       


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
   
        print(f"Received `{msg.payload.decode()}` from `{msg.TOPIC}` topic")

    client.subscribe(TOPIC)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    client.loop_start()
    # subscribe(client)
    publish(client)


if __name__ == '__main__':
    run()