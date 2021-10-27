Player1 = Player(id, name, pos_x, pos_y, health)
Player2 = Player(id, name, pos_x, pos_y, health)
Player.id = MQTT.add_id(player, id)
initCombat(Player1, Player2)
closeCombat(health, timer)

#choisir les variables en tant voulues