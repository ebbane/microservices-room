import logging
import time
from MQTT import * 



class Room():
    def __init__(self):
        pass
    
    def player_connexion(self, msg):
        logging.info(f'Received message : {msg}')
        # msg.payload = 
            # msg.get('key')
            # Création des joueur a partir des id
        
    def player1_action(self, msg):
        logging.info(f'Received message : {msg}')
        # Apelle fonction déplacement 
        # set player = player1
        
    def player2_action(self, msg):
        logging.info(f'Received message : {msg}')
        # Apelle fonction déplacement 
        # set player = player2
       
            
    
    # Sending a MQTT Message through blinker signals
    def send_topic(self, topic, payload):
        sig = signal('message')
        sig.send({'topic': topic, 'body': payload})
        
    def position(self):
        position2= {'player1_x': 150, 'player1_y': 200, 'player2_x': 100, 'player2_y': 150}
        self.send_topic('game/match', position2)
                
    
            

# --------------------------------------------------


def main():

    # ---------------------------------
    # Initializing MQTT
    mqtt_client = MQTTClient(['room/connexion', 'room/joueur1', 'room/joueur2' ])
    mqtt_client.setup()
    mqtt_client.run()

    # ---------------------------------
    # TODO: Start my application
    app = Room()
    app.position()
    
    def listen_topic(self):
        
        def on_message_room_connexion(msg):
            app.player_connexion(msg)        
    
        sig = signal('room/connexion')
        sig.connect(on_message_room_connexion)
        
        def on_message_player1(msg):
            app.player1_action(msg)        
    
        sig = signal('room/joueur1')
        sig.connect(on_message_player1)
        
        def on_message_player2(msg):
            app.player2_action(msg)        
    
        sig = signal('room/joueur2')
        sig.connect(on_message_player2)
        


    # ---------------------------------
    # Closing connection
    # mqtt_client.stop()

if __name__ == "__main__":
    main()