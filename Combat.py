import time
from Config import ARENA_SIZE
from Player import Player
from datetime import datetime
import asyncio
import logging
logging.getLogger().setLevel(logging.INFO)

class Combat :
        def __init__(self, id_combat, seconds):

            self.players = []
            self.id_combat = id_combat
            self.seconds = seconds
            self.start_time = 0
            self.timer = 0
            self.afk_limit = 10
             

    
            
        def increment_timer(self):

                time.sleep(1)
                new_time = datetime.now()
                self.timer = new_time - self.start_time
                self.check_afk()
                self.increment_timer()


        def launch_timer(self):
                self.timer = 0
                self.start_time = datetime.now()
                self.increment_timer()



        def initCombat(self, p1x, p1y,p2x, p2y, timer):

                timer(seconds)



        def closeCombat(self,pscore, phealth, timer):
                if phealth == 0 and timer > 0 :
                        pscore += 0
                        pscore += 1

                if timer == 0 :
                        pscore += 0


        def check_afk(self):
             logging.info(f'AFK DETECTED : {id}')
             for player in self.players:
                  current_time = datetime.now()
                  if (current_time - player.last_action).seconds > self.afk_limit:
                         self.players.remove(player)

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
                    return{'id': other.id, 'data': {'hp' : other.health}}
            player.update(key)
            return {'id' : id, 'position_x' : player.position_x, 'guard ' : player.guard, 'attack' : player.attack}
            


        def collider(self):
            logging.info(f'check position1 : {position1} and position2 : {position2} and ARENA_SIZE : {ARENA_SIZE}')
            def is_colliding(player1, player2):
                if abs(player2.position_x - player2.position_x) < 2 * player1.size_x:
                    return True
                return False

            for player in self.player:
                 # handle arena_size boundaries
                if player.position_x + player.size_x > ARENA_SIZE:
                       player.position_x = ARENA_SIZE - player.size_x
                if player.position_x < 0:
                    player.position_x = 0

                 # handle player collision
                for other in self.player:
                    if other.id != player.id and is_colliding(player, other):
                        player.position_x = ARENA_SIZE + other.position_x
