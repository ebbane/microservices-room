import time
import asyncio
from datetime import datetime

class Player :
    def __init__(self, id, name, pos_x, pos_y, size_x, last_action):

        self.id = -1
        self.name = ""
        self.health = 100
        self.position_x = 310
        self.position_y = 400
        self.attack = False
        self.guard = False
        self.size_x = 120
        self.last_action = 0


        def update_player(self, key):  #function key_pressed
             player.last_action = datetime.now()
             if "q" in key:
                    self.position_x -=50

             if "d" in key:
                    self.position_x +=25
    
             if "s" in key:
                    self.position_x -=25

             if "k" in key:
                    self.attack = True

             if "l" in key:
                    self.guard = True

             if self.position_x > self.arena_size:
                    self.position_x = self.arena_size

             if self.position_x <= other.position_x :
                 self.position_x -= 20

     
             return { 'id' : self.id, 'health': self.health, 'position_x': self.position_x}

        def hitbox(self, player):      #set la hitbox

            return self.size_x + self.position_x

        async def hit(self, other):
            
             self.last_action = datetime.now()
             self.attack = True
             if self.hitbox.pos_x <= other.hitbox.pos_x and not other.guard and not self.guard:
                  other.health -=25
                  await asyncio.sleep(1)
                  self.attack = False
