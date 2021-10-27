class Player :
    def__init__(self, id, name, pos_x, pos_y, score_)

    self.id = 0
    self.name = string
    self.health = 100
    self.position_x = pos_x
    self.position_y = pos_y
    self.attack = bool
    self.guard = bool
    self.score = score_



    def initmovement(self, key):  #function key_pressed
     if "q" in key:
            self.position_x -=50

     if "d" in key:
            self.position_x +=25
    
     if "s" in key:
            self.position_x -=25

     if "k" in key:
            self.attack == true

     if "l" in key:
            self.guard == true
     
     return key

    def hitbox (self, player):      #set la hitbox

     pos_x += 20
     pos_y += 50

    def hit(self, other): 

     if self.attack == True and self.hitbox.pos_x <= other.hitbox.pos_x and other.guard == False:
         other.health -=25
         time.sleep(1);  #frame d'invulnerabilité



    def guard(self):
         for i in range(1):
             self.guard == True
             time.sleep(3) #permet de monter la garde toutes les 3s