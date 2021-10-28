import time
import Player
import asyncio
from datetime import datetime

class Combat :
        def __init__(self):

            self.player = []
            self.arena_size = 0
            self.seconds = 90
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



        def closeCombat(self, health, timer, player_rang):
                if health == 0 and timer > 0 :
                        # player.pscore = False
                        # other.pscore += 1
                        game_result = {'finish': True, 'equality': False, 'winner': player[player_rang], 'looser': player}
                        self.send_topic('game/result' , game_result)

                if timer == 0 :
                        game_result = {'finish': True, 'equality': True, 'player1': player[player_rang], 'player2': player}
                        self.send_topic('game/result' , game_result)


        def check_afk(self):
       
             for player in self.players:
                  current_time = datetime.now()
                  if (current_time - player.last_action).seconds > self.afk_limit:
                         self.players.remove(player)

        def add_player(self, id, name):
             if len(self.players) < 2:
                 self.players.append(Player(id, name))
                 return True
             return False


        def get_player(self, id):
            for player in self.players:
                if id == player.id:
                    return player
            return None
