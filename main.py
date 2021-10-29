import logging
import time
from Combat import * 
import Player
# from mqttClient import * 
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
        
            
    # # Mettre écoute signaux qui vienne de game 
    # sig = signal('game_?')
    # sig.connect(send_topic('game/result', msg))
            

# --------------------------------------------------

def main():
    logging.warning(f'coucou')
    game = Combat()

    id = 3
    data = { 'name': 'Thor'}
    game.add_player(3, data)

    id = 4
    data = { 'name': 'Odin'}
    game.add_player(id, data)

    id = 5
    data = { 'name': 'NotAdded'}
    game.add_player(id, data)

    game.update_player(3, 'q')
    for i in range(0, 29):
        game.update_player(4, 'd')

    # Colliding with player
    game.update_player(4, 'd')

    # game.update_player(3)
    # for pos in range(0, 10):
    #     data = { 'id': 3, 'pos_x': pos}
    #     game.update_player(data['id'], data)
    #     data = {'id': 4, 'key': 'k'}
    #     game.update_player(data['id'], 'k')
    #     data = {'id': 3, 'key': 'l'}
    #     game.update_player(data['id'], 'l')

    # game.launch_timer()

if __name__ == "__main__":
    main()