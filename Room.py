import logging
import time
from Combat import * 
import Player
from mqttClient import * 

class Room():
    def __init__(self):
        pass
    
    def on_player_connexion(self, msg):      
        
        player1_id = msg.get('joueur1').get('id') # Extract data from key
        player1_name = msg.get('joueur1').get('nom')       
        
           
        self.add_player(player1_id, player1_name) # set player 1 in player array    
        
        
    def on_player_action(self, msg):
        playerId = msg.get('id')   
        control = msg.get('control') 
        new_data = self.iniinitmovement(playerId,control)
        topic='client/players'
        
        self.send_topic(topic, new_data)
               
            
    # Sending a MQTT Message through blinker signals
    def send_topic(self, topic, payload):
        sig = signal('message')
        sig.send({'topic': topic, 'body': payload})
        
            

# --------------------------------------------------


def main():

    # ---------------------------------
    # Initializing MQTT
    mqtt_client = MQTTClient(['client/newplayer', 'room/player' ])
    mqtt_client.setup()
    mqtt_client.run()

    # ---------------------------------
    # TODO: Start my application
    app = Room()
    
    
    def listen_topic():
        
        def on_message_room_connexion(msg):
            app.on_player_connexion(msg)        
    
        sig = signal('client/newplayer')
        sig.connect(on_message_room_connexion)
        
        def on_message_player(msg):
            app.on_player_action(msg)        
    
        sig = signal('room/player')
        sig.connect(on_message_player)
        
       
        
    listen_topic()
    game = Combat()
    game.launch_timer() 
    
    # mqtt_client.wait() 



    # ---------------------------------
    # Closing connection
    # mqtt_client.stop()

if __name__ == "__main__":
    main()