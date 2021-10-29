import logging
import time
from Combat import * 
import Player
from mqttClient import * 

logging.getLogger().setLevel(logging.INFO)

class Room():
    def __init__(self):
        pass
    
    def on_player_connexion(self, msg):      
        print(msg)
        player1_id = msg.get('id') # Extract data from key
        player1_name = msg.get('username')
         
        self.add_player(player1_id, player1_name) # set player 1 in player array    
         
    def on_player_action(self, msg):
        playerId = msg.get('id')   # Extract data from key
        control = msg.get('control') 
        
        new_data = self.update_player(playerId,control)   # get new position with player id
        topic='client/players'     # set topic 
        self.send_topic(topic, new_data) # use function to send topic      
            
    # Sending a MQTT Message through blinker signals
    def send_topic(self, topic, payload): 
        sig = signal('message')
        sig.send({'topic': topic, 'body': payload})
              
    # Get timer signal ans set timer topic
    def on_message_timer(self, msg):
        topic='client/timer'     # set topic 
        self.send_topic(topic, msg)     
    
    sig = signal('timer')
    sig.connect(on_message_timer)
    
    # Get result and finish modality : timer or KO and set game/result topic
    def on_message_game_finsih(self, msg):
        topic='game/result'     # set topic
        if msg == 'timeout' :  
            payload = { 'equality' : 'True', 'idUser_Win' : Player[0] , 'idUser_Los' : Player[1] }        
            self.send_topic(topic, payload)
        else :
            self.send_topic(topic, msg)  
    
    sig = signal('game_ended')
    sig.connect(on_message_game_finsih)      

# --------------------------------------------------

def main():

    # ---------------------------------
    # Initializing MQTT
    mqtt_client = MQTTClient(['client/newplayer', 'room/player' ])
    mqtt_client.setup()
    mqtt_client.run()

    # ---------------------------------
    # Initialize Room class
    app = Room()
    
    # define topic list to listen with signal
    def listen_topic():
        
        def on_message_room_connexion(msg):
            app.on_player_connexion(msg)        
    
        sig = signal('client/newplayer')
        sig.connect(on_message_room_connexion)
        
        def on_message_player(msg):
            app.on_player_action(msg)        
    
        sig = signal('room/player')
        sig.connect(on_message_player)
        
       
    # Call topic function
    listen_topic()
    
    # Initialize Combat class and start timer
    game = Combat()
    game.launch_timer() 
    
 
    # ---------------------------------
    # Closing connection
    # mqtt_client.stop()

if __name__ == "__main__":
    main()