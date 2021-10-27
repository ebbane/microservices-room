import logging
import time
from MQTT import * 

topic="client/joueur2"
payload2={'position': '54', 'health': '2'}

class Room():
    def __init__(self):
        # Linking messages to my application
        def on_message_room_connexion(msg):
            logging.info(f'Received message {msg}')
            print(msg)
            # msg.payload = 
            msg.get('key')
        
        sig = signal('debug/test')
        sig.connect(on_message_room_connexion)
    
    # Sending a MQTT Message through blinker signals
    def send_topic(self, topic, payload):
        sig = signal('message')
        sig.send({'topic': topic, 'body': payload})
        
    def position(self):
        position2= {'player1_x': 'coucou2', 'player1_y': 25, 'player2_x': 100, 'player2_y': 150}
        self.send_topic('game/match', position2)
        
    def new_subscribe(self, topic):
        self.client.subscribe(topic)

# --------------------------------------------------


def main():

    # ---------------------------------
    # Initializing MQTT
    mqtt_client = MQTTClient(['debug/test'])
    mqtt_client.setup()
    mqtt_client.run()

    # ---------------------------------
    # TODO: Start my application
    app = Room()
    app.position()

    # ---------------------------------
    # Closing connection
    # mqtt_client.stop()

if __name__ == "__main__":
    main()