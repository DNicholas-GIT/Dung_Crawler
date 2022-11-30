Menu.start()

class World_Generator:

  """  
  Creates incrementing named Class objects EX: "Zone_1" that are created by turning a string into an object 
  whose named is "Zone_" and concatinated with an incrementing number "1, 2, 3" etc

  Then appends object to list of said zones
  Ex: lst = (zone_1, zone_2, zone_3)
  zone_# = class object with attributes name, zone_difficulty, etc
  """


  pass





"""
{
    "zones" : {
        "Plains" : {"difficulty": 1, "enemies" : ["orc", "goblin"]}, 
        "Mountains" : {"difficulty": 3, "enemies" : ["orcs", "snakes"]}, 
        "Ocean" : {"difficulty": 2, "enemies" : ["barbarian", "corsair"]}, 
    } 
} 
"""


"""
class Zone:
    def __init__(self, name):
        self.name = name

names = ["Grandpa's home", "Wisp Forest", "Sunnydew Village"] 

zones = {f"Zone {i+1}": Zone(name) for i, name in enumerate(names)} 

print(zones["Zone 2"].name)
"""






{'Armor': chain_mail}




# class TravelManager:

#   def build_zones():
#     p_place = levels[travel_list[0].name]
#     c_place = levels[travel_list[1].name]
#     n_place = levels[travel_list[2].name]

#     p_enemy = land_creatures[travel_list[0].enemy]
#     c_enemy = land_creatures[travel_list[1].enemy]
#     n_enemy = land_creatures[travel_list[2].enemy]

#     p_enemy_hp = p_enemy.health
#     c_enemy_hp = c_enemy.health
#     n_enemy_hp = n_enemy.health

#     p_text = f"You have entered the {p_place} and encountered a level {p_enemy.level} {p_enemy.name}"
#     c_text = f"You have entered the {c_place} and encountered a level {c_enemy.level} {c_enemy.name}"
#     n_text = f"You have entered the {n_place} and encountered a level {n_enemy.level} {n_enemy.name}"

#   def next_zone():
#     pass

#   def repeat_zone():
#     pass

#   def past_zone():
#     pass
