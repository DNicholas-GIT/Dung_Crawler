import random


class Item:
  def __init__(self, name, level, health, attack, speed, equipable):
    self.name = name
    self.level = level
    self.health = health + level
    self.attack = attack + level
    self.speed = speed + level
    self.equipable = equipable


class Equipable(Item):
  def __init__(self, name, level, health, attack, speed, equipable, slot):
    self.name = name
    self.level = level
    self.health = health + level
    self.attack = attack + level
    self.speed = speed + level
    self.equipable = equipable
    self.slot = slot


class Character:
  def __init__(self, name, level, health, attack, speed, xp, inventory, equipped_gear):
    self.name = name
    self.level = level
    self.health = health + level
    self.attack = attack + level
    self.speed = speed + level
    self.xp = xp
    self.inventory = inventory
    self.equipped_gear = equipped_gear

  def level_up(self):
    self.level = self.level + 1
    self.health = self.health + 3
    self.attack = self.attack + 1
    self.speed = self.speed + 1

  def heal(self, hp_heal):
    self.health = self.health + hp_heal
    max_health = 20 + (self.level * 3)
    if self.health >= max_health:
      self.health = max_health
      print("You are fully rested!")

  def unequip(self):
    while True:
      for x in equipped:
        if x != None:
          print(f"{x.name} equipped in slot {equipped.index(x) + 1}")
      print("""
      1 = Unequip Slot 1
      2 = Unequip Slot 2
      3 = Exit
          """)
      choice = input('Please select a slot to Unequip: ')    
      int_choice = int(choice) - 1
      if choice == "1" or choice == "2":
        print(choice)
        equipped[int_choice] = None
      
      elif choice == "3":
        print(choice)
        break

      else:
          print("Not an accepted input")

          
  def replace(self, new_gear):

    print(f"Prior Human Stats Attack: {human.attack} Speed: {human.speed} Health: {human.health}")

    gear_slot = inventory[new_gear].slot

    if equipped[gear_slot] == None:
      equipped[gear_slot] = inventory[new_gear]
      human.attack = human.attack + equipped[gear_slot].attack
      human.speed = human.speed + equipped[gear_slot].speed
      human.health = human.health + equipped[gear_slot].health

    else:
      human.attack = human.attack - equipped[gear_slot].attack
      human.speed = human.speed - equipped[gear_slot].speed
      human.health = human.health - equipped[gear_slot].health      
      equipped[gear_slot] = inventory[new_gear]
      human.attack = human.attack + equipped[gear_slot].attack
      human.speed = human.speed + equipped[gear_slot].speed
      human.health = human.health + equipped[gear_slot].health      

    print(f"Current Human Stats Attack: {human.attack} Speed: {human.speed} Health: {human.health}")



class Creature:
  def __init__(self, name, level, health, attack, speed, xp_value):
    self.name = name
    self.level = level
    self.health = health + level
    self.attack = attack + level
    self.speed = speed + level
    self.xp_value = xp_value + level * 10

  def reran(difficulty):
    for i in land_creatures:
      i.health = i.health - i.level
      i.attack = i.attack - i.level
      i.speed = i.speed - i.level
      i.xp_value = i.xp_value - i.level * 10
      i.level = random.randrange(1, 4) + difficulty
      i.health = i.health + i.level
      i.attack = i.attack + i.level
      i.speed = i.speed + i.level
      i.xp_value = i.xp_value + i.level * 10

chain_mail = Equipable('Chainmail', 1, 4, 2, 0, True, 0)
shirt = Equipable('Shirt', 1, 4, 2, 0, True, 0)
woodensword = Equipable('woodensword', 1, 4, 2, 0, True, 1)
hp_potion = Item('hp pot', 1, 4, 2, 0, False)
mana_potion = Item('mana pot', 1, 4, 2, 0, False)
hat = Equipable('hat', 1, 4, 2, 0, True, 0)


inventory = (shirt, hp_potion, woodensword, hat) 
equipped = [None, None]

chain_mail = Equipable('Chainmail', 1, 4, 2, 0, True, 0)
shirt = Equipable('Shirt', 1, 4, 2, 0, True, 0)
woodensword = Equipable('woodensword', 1, 4, 2, 0, True, 1)
hp_potion = Item('hp pot', 1, 4, 2, 0, False)
mana_potion = Item('mana pot', 1, 4, 2, 0, False)
hat = Equipable('hat', 1, 4, 2, 0, True, 0)

human = Character("Human", 1, 30, 3, 2, 0, inventory, equipped)

goblin = Creature("Goblin", random.randrange(1, 5), 10, 1, 2, 0)
giant_snek = Creature("Giant Snake", random.randrange(1, 4), 15, 3, 2, 0)
barbarian = Creature("Barbarian", random.randrange(1, 2), 20, 4, 3, 0)



land_creatures = (goblin, giant_snek, barbarian)

class Fight:
  
  def stats(x, y):
    print(vars(x))
    print(vars(y))

  def human_stats():
    global human
    print(vars(human))

  def att(attacker, defender):
    print(f"{attacker.name} attacks {defender.name} for {attacker.attack} damage!")
    if defender.health > attacker.attack:
      defender.health = defender.health - attacker.attack
    else:
      defender.health = defender.health - attacker.attack
      print(f"{defender.name} is dead!")
    print(f"{defender.name} new health is {defender.health}")

  def real_fight(attacker, defender):
    if attacker.name == 'Human':
      print("""
      1 = Attack
      2 = Use Item
      3 = Run Away
      """)
      fight_response = input("Please select an option: ")

      if fight_response == '1':

        print(f"{attacker.name} attacks {defender.name} for {attacker.attack} damage!")
        if defender.health > attacker.attack:
          defender.health = defender.health - attacker.attack
        else:
          defender.health = defender.health - attacker.attack
          print(f"{defender.name} is dead!")
        print(f"{defender.name} new health is {defender.health}")       

      elif fight_response == '2':
        pass

      elif fight_response == '3':
        pass

    else:
      print(f"{attacker.name} attacks {defender.name} for {attacker.attack} damage!")
      if defender.health > attacker.attack:
        defender.health = defender.health - attacker.attack
      else:
        defender.health = defender.health - attacker.attack
        print(f"{defender.name} is dead!")
      print(f"{defender.name} new health is {defender.health}")     

class Start:

  def first(x,y):
    fighters = [x, y]
    fighters.sort(key=lambda x: x.speed, reverse=False) # Sorts list from highest to lowest based on speed attribute
    turncount = 0
    while x.health >= 1 and y.health >= 1:
      turncount += 1
      attacker = fighters[turncount % 2]
      defender = fighters[abs((turncount % 2) - 1)]
      Fight.real_fight(attacker, defender)
      # time.sleep(1.5)
    print("Fight is finished")


levels = ("Plains", "Mountains", "Ocean")
enemies = ("Goblin", "Giant Snake", "Barbarian")


class Location:

  def __init__(self, name, enemy, difficulty):
    self.name = name
    self.enemy = enemy
    self.difficulty = difficulty


random_level = Location(random.randrange(0, 3), random.randrange(0, 3), 0)

prior_zone = Location(random.randrange(0, 3), random.randrange(0, 3), 0)
current_zone = Location(random.randrange(0, 3), random.randrange(0, 3), 1)
next_zone = Location(random.randrange(0, 3), random.randrange(0, 3), 2)

travel_list = (prior_zone, current_zone, next_zone)



class SceneManager:
  
  def builder(random_level):
    place = levels[random_level.name]
    enemy = land_creatures[random_level.enemy]
    text = f"You have entered the {place} and encountered a level {enemy.level} {enemy.name}"
    health_val = enemy.health
    print(text)
    print(f"This enemy is worth {enemy.xp_value}!")
    Fight.stats(enemy, human)
    Start.first(enemy, human)
    human.xp = human.xp + enemy.xp_value
    if human.xp >= (50 + 50 * human.level):
      print(human.xp)
      Character.level_up(human)
      human.xp = human.xp % (50 + 50 * human.level)
      print(vars(human))


    print(f"You are currently level {human.level} with {human.xp} xp!")
    enemy.health = health_val
    random_level.name = random.randrange(0, 3)
    random_level.enemy = random.randrange(0, 3)
    random_level.difficulty = random_level.difficulty + 1
 
    Creature.reran(random_level.difficulty)

class Menu:

  def start():
    while True:
      print("""
      1 = Explore
      2 = Camp
      3 = Inventory
      4 = Show Stats
      5 = Exit
      """)
      response = input("Please select an option: ")
      if response == '1':
          SceneManager.builder(random_level)
          if human.health <= 0:
            print("Game over")
            break
      elif response == '2':
          print("A nice campfire will comfort the soul")
          print("You regain some health")
          Character.heal(human, 10)
          
      elif response == '3':
        inventory_menu()

      elif response == '4':
          pass 
      elif response == '5':
          pass
      elif response == '6':
          break

      else:
          print("Not an accepted input")



def check_equipable(bool_input):
  for x in inventory:
    if x.equipable == bool_input:
      choice_var = str(inventory.index(x))
      print(f"{choice_var}: {x.name}", vars(x))

def pick_item():
    while True:
      for x in equipped:
        if x != None:
          print(f"Equipped in Gear Slot {x.slot + 1} {x.name} Attack: {x.attack} Speed: {x.speed} Health: {x.health}")

      print("""
      1 = Replace or Equip Gear
      2 = Unequip Gear
      3 = Exit
      """)
      choice = input("Please select an option: ")

      if choice == '1':

        for x in inventory:
          if x.equipable == True:
            choice_var = str(inventory.index(x))
            print(f"{choice_var}: {x.name}", vars(x))

        item_choice = input("Select Item to Equip: ")      
        int_item_choice = int(item_choice)
        
        if int(item_choice) > len(inventory) or inventory[int(item_choice)].equipable == False:
          print("please select a valid option!")
        else:  
          Character.replace(human, int_item_choice)

      elif choice == "2":
        Character.unequip(human)

      elif choice == "3":
        break


def inventory_menu():
  while True:
    print("Which item would you like to use?")
    print("""
    1 = Check Useable Items
    2 = Use Item
    3 = Check Equipable Item
    4 = Manage Equipped Gear
    5 = Exit
          """)
    inventory_response = input("Please select an option: ")

    if inventory_response == '1':
      check_equipable(False)

    elif inventory_response == '2':
      pass    

    elif inventory_response == '3':
      check_equipable(True)
    
    elif inventory_response == '4':
      pick_item()

    elif inventory_response == '5':
      break
          
    else:
      print("Not an accepted input")  

Menu.start()