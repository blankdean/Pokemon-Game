# Dean Blank
# Section: CS-172-A; Lab 061

from enemy import *

class Monster3(Enemy):

  def __init__(self):
    super().__init__('Pikachu',100) # health and name attributes from enemy class
    self.__defense_mode = False

  # basic attack
  def basicAttack(self,enemy):
    self.__defense_mode = False # Can't Defend and attack
    enemy.Damage(10)
    print(super().getName() + ' volt tackles you!')

  # special attack
  def specialAttack(self,enemy):
    self.__defense_mode = False # Can't Defend and attack
    enemy.Damage(55)
    print(super().getName() + ' used thunder shock on you!')

  # defense
  def defense(self,enemy):
    self.__defense_mode = True # if defense is True then attack will do half damage
    print(super().getName() + ' uses dash defense!')

  # get name of defense
  def defenseName(self):
    return "Dash"

  # get name of basic attack
  def basicName(self):
    return "Volt Tackles"

  # get name of special attack
  def specialName(self):
    return "Thunder Shock"

# Damage function used to take damage
  def Damage(self,damage):
    if(self.__defense_mode):
      #third Damage for Pikachu
      super().setHealth(super().getHealth()-(damage//3))
    else:
      super().setHealth(super().getHealth()-damage)
