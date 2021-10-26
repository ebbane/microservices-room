import arcade
from PIL.ImagePalette import random

class Player: 
    def __init__(self, x, y, speed, limit_l, limit_r, id_player):
       
        self.id = id_player
        self.name = name

        self.center_x = x
        self.center_y = y
        self.move_x = 0
        self.move_y = 0
        self.speed = speed

        self.score = 0
        self.lives = 3
        self.blink_timer = 0

        self.freeze = False
        self.invicibility = False

        self.aimlock = False
        self.aiming_timer = 0
        self.aiming_x = 0
        self.aiming_y = 0
        self.aiming_rand = 0


        self.limit_left = limit_l
        self.limit_right = limit_r


    def set_key(self, up_key, down_key, left_key, right_key, aimlock_key, reload_key, shoot_key):
        self.up_key = up_key
        self.down_key = down_key
        self.left_key = left_key
        self.right_key = right_key
        self.aimlock_key = aimlock_key
        self.reload_key = reload_key
        self.shoot_key = shoot_key

   
    def lose_one_live(self, player):
        if not self.invicibility:
            self.lives -= 1
            if self.lives < 1:
                self.freeze = True
                self.invicibility = True
                self.cur_fall_texture = 1
                player.score += 3
            else:
                self.blink_timer = 1
                player.score += 1


    def key_pressed(self, key):
        self.timer_inactivity = 0.0

        if key == self.aimlock_key and self.cur_throw_texture == 0:
            self.aimlock = True
            self.aiming_rand = random() * pi * 2
        if key == self.shoot_key and self.cur_throw_texture == 0 and not self.freeze and self.snowball_count > 0:
            self.shoot()
            self.aimlock = False
            self.cur_throw_texture = 1
            self.aiming_timer = 0
        if key == self.reload_key:
            self.reload = True

    def key_released(self, key):
        self.timer_inactivity = 0.0

        if key == self.up_key:
            self.move_y -= self.speed
        if key == self.down_key:
            self.move_y += self.speed
        if key == self.left_key:
            self.move_x += self.speed
        if key == self.right_key:
            self.move_x -= self.speed
        if key == self.aimlock_key and self.aimlock:
            self.aimlock = False
            self.aiming_timer = 0
        if key == self.reload_key:
            self.reload = False

    def joystick(self, key):
        self.timer_inactivity = 0.0

        if "C" in key:
            self.move_y = 0
            self.move_x = 0
        if "N" in key:
            self.move_y = self.speed
        if "S" in key:
            self.move_y = -self.speed

        if "E" in key:
            self.move_x = self.speed
        if "W" in key:
            self.move_x = -self.speed

    


