import time
import asyncio
from datetime import datetime
from Config import ARENA_SIZE
import logging

class Player :
    def __init__(self, id, name):

        self.id = id
        self.name = name
        self.health = 100
        self.position_x = 310
        self.position_y = 400
        self.attack = False
        self.guard = False
        self.size_x = 120
        self.last_action = 0
        self.ko = False


    def update(self, key):  #function key_pressed

       self.last_action = datetime.now()

       if "q" in key:
            self.position_x -=50

       if "d" in key:
            self.position_x +=25
    
       if "s" in key:
            self.position_x -=25

       if "l" in key:
            self.guard = True
                    
     
       return key

    def hitbox(self):      #set la hitbox

       return self.size_x + self.position_x

    def hit(self, other):
        self.last_action = datetime.now()
        self.attack = True
        if self.hitbox() <= other.hitbox() and not other.guard and not self.guard:
            other.health -=25
            if other.health == 0:
               return self.ko == True
            return self.ko == False
            time.sleep(1)
            self.attack = False

       
