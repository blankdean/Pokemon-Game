# Dean Blank
# Section: CS-172-A; Lab 061

from enemy import *

class Monster2(Enemy):

  def __init__(self):
    super().__init__('Drexel Dragon',100) # health and name attributes from enemy class
    self.__defense_mode = False

  # basic attack
  def basicAttack(self,enemy):
    self.__defense_mode = False # Can't Defend and attack
    enemy.Damage(25)
    print(super().getName() + ' scratches you!')

  # special attack
  def specialAttack(self,enemy):
    self.__defense_mode = False # Can't Defend and attack
    enemy.Damage(50)
    print(super().getName() + ' used dragon breath on you!')

  # defense
  def defense(self,enemy):
    self.__defense_mode = True # if defense is True then attack will do half damage
    print(super().getName() + ' uses block!')

  # get name of defense
  def defenseName(self):
    return "block"

  # get name of basic attack
  def basicName(self):
    return "Claw"

  # get name of special attack
  def specialName(self):
    return "Dragon Breath"

# Damage function used to take damage
  def Damage(self,damage):
    if(self.__defense_mode):
      #Half Damage
      super().setHealth(super().getHealth()-(damage//2))
    else:
      super().setHealth(super().getHealth()-damage)