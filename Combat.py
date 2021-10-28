import time
import Player
import asyncio

class Combat :
        def __init__(self, id_combat, seconds):

            self.player = []
            self.arena_size = 0
            self.id_combat = int
            self.init_player = int
            self.seconds = 90
            self.score = int
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
                else :
                        pscore += 1

                if timer == 0 :
                        pscore += 0


        def check_afk(self):
       
             for player in self.players:
                  current_time = datetime.now()
                  if (current_time - player.last_action).seconds > self.afk_limit:
                         self.players.remove(player)

        def add_player(self, id, data):
             if len(self.players) < 2:
                 self.players.append(Player(id, data))
                 return True      
             return False
