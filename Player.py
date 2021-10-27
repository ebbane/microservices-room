class Player :
    def__init__(self, id, name, pos_x, pos_y, health)

    self.id = 0
    self.name = string
    self.health = 100
    self.pos_x = int
    self.pos_y = 50
    self.backdash = int
    self.attack = bool
    self.guard = bool



    def initmovement(self, key):  #function key_pressed
     if "q" in key:
            self.pos_x -=25

     if "d" in key:
            self.pos_x +=25
    
     if "s" in key:
            self.back +=50

     if "k" in key:
            self.attack == true

     if "l" in key:
            self.guard == true
     
     return key

    def hitbox (self, player):      #set la hitbox

     pos_x += 20
     pos_y += 50

    
    def hit(self): 

     if self.attack == True and hitbox.pos_x1 <= hitbox.pos_x2 and self.guard == False:
         health -=25
         time.sleep(1);  #frame d'invulnerabilité

    def guard(self):
         for i in range(1):
             self.guard == True
             time.sleep(3) #permet de monter la garde toutes les 3s