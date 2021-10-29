import time
import asyncio
from datetime import datetime
from Config import ARENA_SIZE
import logging
from blinker import signal

class Player :
     
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.health = 100
        self.position_x = 50
        self.attack = False
        self.guard = False
        self.size_x = 125
        self.last_action = datetime.now
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

    def hit(self, other):
        self.last_action = datetime.now()
        self.attack = True
        logging.info(f'player {self.id} : position : {self.position_x} and other {other.id} position : {other.position_x}')
        if abs(self.position_x - (ARENA_SIZE - other.position_x))<= 2 * self.size_x and not other.guard and not self.guard:
          
          other.health -=25
          if other.health <= 0:
               sig = signal('game_ended')
               sig.send({ 'equality' : 'False', 'idUser_Win' : {self.id} , 'idUser_Los' : {other.id}})
               return True
          time.sleep(1)
          self.attack = False
