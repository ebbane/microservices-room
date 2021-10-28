import logging
import time
from mqttClient import * 

class Room():
    def __init__(self):
        pass
    
    def on_player_connexion(self, msg):
        print (msg)
        
        # print(f'Received message : {msg}')
            
            # msg.get('joueur1').get('nom')
            # msg.get('joueur1').get('id')
            # Création des joueur a partir des id
        
    def on_player1_action(self, msg):
        # Apelle fonction déplacement 
        # set player = player1
        print (msg)
        control = msg.get('control')
        
    def on_player2_action(self, msg):
        print(msg)        
        # player = player2
        control = msg.get('control')
        # Apelle fonction déplacement 
       
            
    
    # Sending a MQTT Message through blinker signals
    def send_topic(self, topic, payload):
        sig = signal('message')
        sig.send({'topic': topic, 'body': payload})
        
    # def position(self):
    #     position2= {'player1_x': 15, 'player1_y': 200, 'player2_x': 100, 'player2_y': 150}
    #     self.send_topic('game/match', position2)
                
    
            

# --------------------------------------------------


def main():

    # ---------------------------------
    # Initializing MQTT
    mqtt_client = MQTTClient(['prediction/infos', 'room/player1', 'room/player2' ])
    mqtt_client.setup()
    mqtt_client.run()

    # ---------------------------------
    # TODO: Start my application
    app = Room()
    
    
    def listen_topic():
        # print('coucou')
        
        def on_message_room_connexion(msg):
            app.on_player_connexion(msg)        
    
        sig = signal('prediction/infos')
        sig.connect(on_message_room_connexion)
        
        def on_message_player1(msg):
            app.on_player1_action(msg)        
    
        sig = signal('room/player1')
        sig.connect(on_message_player1)
        
        def on_message_player2(msg):
            app.on_player2_action(msg)        
    
        sig = signal('room/player2')
        sig.connect(on_message_player2)
        
    listen_topic()
    while True :
        pass
    # mqtt_client.wait() 



    # ---------------------------------
    # Closing connection
    # mqtt_client.stop()

if __name__ == "__main__":
    main()