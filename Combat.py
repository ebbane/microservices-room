import time
from Config import ARENA_SIZE
from Player import Player
from datetime import datetime
import asyncio
import logging
from blinker import signal

logging.getLogger().setLevel(logging.INFO)

class Combat :
        def __init__(self):

            self.players = []
            # self.id_combat = id_combat
            self.start_time = 0
            self.timer = 0
            self.afk_limit = 40
            self.time_limit = 90

    
            
        def increment_timer(self):
             time.sleep(1)
             new_time = datetime.now()
             self.timer = new_time - self.start_time
                
             # Send timer update
             sig = signal('timer')
             sig.send(self.timer)

             self.check_afk()
                
             # Check game ended
             if self.timer.seconds >= self.time_limit:
                 sig = signal('game_ended')
                 sig.send('timeout')
                 self.restart()
                 return

             self.increment_timer()

        def restart(self):
            logging.info("Combat is restarting")
            for player in self.players:
                player.health = 100
            self.launch_timer()




        def launch_timer(self):
                self.timer = 0
                self.start_time = datetime.now()
                self.increment_timer()


        def check_afk(self):
             for player in self.players:
                  current_time = datetime.now()
                  if (current_time - player.last_action).seconds > self.afk_limit:
                         self.players.remove(player)
                         logging.info(f'Player id:{player.id} was removed for inactivity')

        def add_player(self, id, name):
             logging.info(f'Player added with id: {id}')
             if len(self.players) < 2:
                 self.players.append(Player(id, name))
                 return True      
             return False


        def get_player(self, id):

            for player in self.players:
                if id == player.id:
                    return player
            return None


        def update_player(self, id, key):
            player = self.get_player(id)
            if "k" in key:
                    other = None
                    for iplayer in self.players:
                        other = iplayer
                        break
                    player.hit(other)
                    logging.info(f'Other {other}')
                    return{'id': other.id, 'data': {'hp' : other.health}}
            self.collider()
            logging.info(f'Player {player}')
            player.update(key)
            return {'id' : id, 'position_x' : player.position_x, 'guard ' : player.guard, 'attack' : player.attack}
            


        def collider(self):
            def is_colliding(player1, player2):
                p2_mirrored = ARENA_SIZE - player2.position_x
                if abs(p2_mirrored - player1.position_x) < 2 * player1.size_x:
                    return True
                return False
    
            for player in self.players:
                 # handle arena_size boundaries
                if player.position_x + player.size_x > ARENA_SIZE:
                       player.position_x = ARENA_SIZE - player.size_x
                if player.position_x < 0:
                    player.position_x = 0

                 # handle player collision
                for other in self.players:
                    if other.id != player.id and is_colliding(player, other):
                        player.position_x = ARENA_SIZE - other.position_x + 2 * player.size_x