# Dean Blank
# Section: CS-172-A; Lab 061

from enemy import *

class Monster4(Enemy):
  
  def __init__(self):
    super().__init__('Bowser',100) # health and name attributes from enemy class
    self.__defense_mode = False

  # basic attack
  def basicAttack(self,enemy):
    self.__defense_mode = False # Can't Defend and attack
    enemy.Damage(30)
    print(super().getName() + ' flying slams you!')

  # special attack
  def specialAttack(self,enemy):
    self.__defense_mode = False # Can't Defend and attack
    enemy.Damage(40)
    print(super().getName() + ' used fire breath on you!')

  # defense
  def defense(self,enemy):
    self.__defense_mode = True # if defense is True then attack will do half damage
    print(super().getName() + ' uses whirling fortress block!')

  # get name of defense
  def defenseName(self):
    return "Whirling Fortress Block"

  # get name of basic attack
  def basicName(self):
    return "Flying Slam"

  # get name of special attack
  def specialName(self):
    return "Fire Breath"

# Damage function used to take damage
  def Damage(self,damage):
    if(self.__defense_mode):
      #Half Damage
      super().setHealth(super().getHealth()-(damage//2))
    else:
      super().setHealth(super().getHealth()-damage)