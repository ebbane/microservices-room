from Combat import Combat
from Player import Player
import logging

def main():

     
    game = Combat(1, 90)    
    


    id = 3
    data = { 'name': 'Thor'}
    game.add_player(3, data)

    id = 4
    data = { 'name': 'Odin'}
    game.add_player(id, data)

    id = 5
    data = { 'name': 'NotAdded'}
    game.add_player(id, data)

    for pos in range(0, 500):
        data = { 'id': 3, 'pos_x': pos}
        game.update_player(data['id'], data)
        data = {'id': 4, 'key': 'k'}
        game.update_player(data['id'], 'k')
        data = {'id': 3, 'key': 'l'}
        game.update_player(data['id'], 'l')

    game.launch_timer()

if __name__ == "__main__":
       main()