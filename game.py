import Combat
import Player
import Mqtt

Player1 = Player(id, name, position_x, position_y)
Player2 = Player(id, name, position_x, position_y)
Player.id = MQTT.add_id(player, id)
initCombat(Player1.position_x, Player1.position_y, Player2.position_x, Player2.position_y)
loop_afk()
closeCombat(health, timer)
destroy(Combat)