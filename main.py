import time
import random

class Character:
  def __init__(self, name, level, health, attack, speed, xp):
    self.name = name
    self.level = level
    self.health = health + level
    self.attack = attack + level
    self.speed = speed + level
    self.xp = xp

  def level_up(self):
    self.level = self.level + 1
    self.xp = self.xp % 100
    self.health = self.health + 1
    self.attack = self.attack + 1
    self.speed = self.speed + 1


class Creature:
  def __init__(self, name, level, health, attack, speed, xp_value):
    self.name = name
    self.level = level
    self.health = health + level
    self.attack = attack + level
    self.speed = speed + level
    self.xp_value = xp_value + level * 10


human = Character("Human", 1, 1000, 3, 2, 0)

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


class Start:

  def first(x,y):
    fighters = [x, y]
    fighters.sort(key=lambda x: x.speed, reverse=False) # Sorts list from highest to lowest based on speed attribute
    turncount = 0
    while x.health >= 1 and y.health >= 1:
      turncount += 1
      attacker = fighters[turncount % 2]
      defender = fighters[abs((turncount % 2) - 1)]
      Fight.att(attacker, defender)
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


class SceneManager:
  
  def builder(random_level):
    place = levels[random_level.name]
    enemy = land_creatures[random_level.enemy]
    
    # random_level.difficulty = random_level.difficulty + 1


    # for i in land_creatures:
    #   if i.name == enemy:
    text = f"You have entered the {place} and encountered a level {enemy.level} {enemy.name}"
    health_val = enemy.health
    print(text)
    print(f"This enemy is worth {enemy.xp_value}!")
    Fight.stats(enemy, human)
    Start.first(enemy, human)
    human.xp = human.xp + enemy.xp_value
    if human.xp >= 100:
      Character.level_up(human)

    print(f"You are now level {human.level} with {human.xp} xp!")
    enemy.health = health_val
    random_level.name = random.randrange(0, 3)
    random_level.enemy = random.randrange(0, 3)
    random_level.difficulty = random_level.difficulty + 1
 


class Menu:


  def start():
    while True:
      print("""
      1 = Explore
      2 = Camp
      3 = Use Item
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
          print(human.health)
          human.health = human.health + 10
          print(human.health)

      elif response == '3':
          print("Which item would you like to use?")

      elif response == '4':
          Fight.human_stats()

      elif response == '5':
          break

      else:
          print("Not an accepted input")



Menu.start()
