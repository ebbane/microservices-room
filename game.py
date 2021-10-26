from tkinter import * 
import time
import keyboard


## Gravity ##

class point:
    def __init__(self, name):
        self.name = name
        self.x = 25
        self.y = 775
        self.vx = 5
        self.vy = 0
        self.newVy = 15
        self.ax = 0
        self.ay = 0.5
        self.etat = 1
        self.nb = 0
        self.timer = 0
        self.score = 0
        self.hit = 0
        self.life = 3

player1 = point(0)
player1.x = 50

player2 = point(1)
player2.x = 1850




player1.timer = time.time()



movement_speed = 0

# Valeurs
def init_vitesse_players(val):
    pass

        
def init_movement(val, player):
    global movement_speed
    player.vx += val
    if(player.vx <= 1):
        player.vx = 1
    # if (player == player1):
    #     jump_speed = canvas.create_text(1300, 500, font="Times, 50", text=player1.vx, fill = "White")
    # else :
    #     jump_speed = canvas.create_text(1300, 900, font="Times, 50", text=player2.vx, fill = "White")



def control():
    if(player1.etat == 1):
        if (keyboard.is_pressed("z")):
            player1.vy = -player1.newVy
            player1.etat = 0
    if keyboard.is_pressed("d"):
        player1.x += player1.vx
    if keyboard.is_pressed("q"):
        player1.x -= player1.vx
    if keyboard.is_pressed("s"):
        player1.y += 25
    if (keyboard.is_pressed("space")) and (time.time()-player1.timer >= 0.35):
        player1.bullet[player1.nb].y = player1.y
        player1.bullet[player1.nb].x = player1.x
        player1.nb += 1
        player1.timer = time.time()
        if(player1.nb == 5):
            player1.nb = 0


    if(player2.etat == 1):
        if keyboard.is_pressed("up"):
            player2.vy = -player2.newVy
            player2.etat = 0
    if keyboard.is_pressed("right"):
        player2.x += player2.vx
    if keyboard.is_pressed("left"):
        player2.x -= player2.vx
    if keyboard.is_pressed("down"):
        player2.y += 25
    if (keyboard.is_pressed("enter")) and (time.time()-player2.timer >= 0.35):
        player2.bullet[player2.nb].y = player2.y
        player2.bullet[player2.nb].x = player2.x
        player2.nb += 1
        player2.timer = time.time()
        if(player2.nb == 5):
            player2.nb = 0