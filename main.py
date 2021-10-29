import logging
import time
from Combat import * 
import Player
logging.getLogger().setLevel(logging.INFO)

# Main class to test the game 
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
    
    # hit other
    data = {'id': 3, 'key': 'k'}
    game.update_player(data['id'], 'k')

    game.update_player(3, 'q')
    for i in range(0, 29):
        game.update_player(4, 'd')

    # Colliding with player and player hit and other guard 
    for i in range(0, 3):
        game.update_player(4, 'l')
        data = {'id': 3, 'key': 'k'}
        game.update_player(data['id'], 'k')
        



if __name__ == "__main__":
    main()