import time
import asensio
from Mqtt import MQTT

class Combat :
        def__init__(self, id_combat, seconds)


        self.id_combat = int
        self.init_player = int
        self.seconds = 90
        self.score = int

        def timer(seconds):
                 print("Chrono : %ds" % seconde)
                 for i in range(seconds): time.sleep(1)
                 print("Fin")




        def initCombat(self, p1x, p1y,p2x, p2y, timer):

                timer(seconds)



        def closeCombat(self,pscore, phealth, timer):
                if phealth == 0 and timer > 0 :
                        pscore += 0
                else :
                        pscore += 1

                if timer == 0 :
                        pscore += 0

        
        async def loop_afk():
                await asyncio.sleep(1)
                if not player.initmovement(key) :
                        time.sleep(10)
                        destroy(Combat)
                await loop_afk
        asyncio.run(loop_afk())