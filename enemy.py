# Dean Blank
# Section: CS-172-A; Lab 061

import abc

class Enemy(metaclass=abc.ABCMeta):

  def __init__(self,n,h): # health and name attribute
    self.__health = h
    self.__name = n

  # string method
  def __str__(self):
    return "I am a monster named " + self.__name+"."

  # get name
  def getName(self):
    return self.__name

  # get health
  def getHealth(self):
    return self.__health

  # set health of monster
  def setHealth(self, health):
    self.__health = health

  # This function is used by the enemy
  # either do damage (positive int) or heal (negative int)
  @abc.abstractmethod
  def Damage(self,damage):
    pass


  # basic attack
  @abc.abstractmethod
  def basicAttack(self,enemy):
    pass

  # special attack
  @abc.abstractmethod
  def specialAttack(self,enemy):
    pass

  # defense
  @abc.abstractmethod
  def defense(self,enemy):
    pass

  # get name of defense
  @abc.abstractmethod
  def defenseName(self):
   pass

  # get name of basic attack
  @abc.abstractmethod
  def basicName(self):
    pass

  # get name of special attack
  @abc.abstractmethod
  def specialName(self):
    pass
