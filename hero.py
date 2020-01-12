# Dean Blank
# Section: CS-172-A; Lab 061

from enemy import Enemy

class Hero(Enemy):

  def __init__(self,n):
    super().__init__(n,100) # health and name attribute from enemy class
    self.__defense_mode = False
    self.__potion = 6
    self.__fireball = 10

  # string method
  def __str__(self):
    return "I am a mighty hero named " + super().getName()+"."


  def getPotion(self):      # get amount of potions left
    return self.__potion

  def getFireball(self):      # need to add potion effect
    return self.__fireball


  # sword attack
  def basicAttack(self,enemy):
    self.__defense_mode = False # Can't Defend and attack
    enemy.Damage(20)
    print('Sword Slash Attack!')

  # fireball attack
  def specialAttack(self,enemy):
    self.__defense_mode = False # Can't Defend and attack
    enemy.Damage(50)
    self.__fireball-=1
    print('Fireball Attack Sucessful!')

  # potion
  def potion(self):
    super().setHealth(super().getHealth()+50)
    if super().getHealth() >=100:
      super().setHealth(100)
    self.__potion-=1
    print('You drank a potion.')

  # shield
  def defense(self,enemy):
    self.__defense_mode = True
    print('Hide behind the Shield!')

  def defenseName(self):
    return "Shield"

  def basicName(self):
    return "Sword"

  def specialName(self):
    return "Fireball"

  def potionName(self):
    return "potion"

# Damage function used to take damage
  def Damage(self,damage):
    if(self.__defense_mode):
      #Half Damage
      super().setHealth(super().getHealth()-(damage//2))
    else:
      super().setHealth(super().getHealth()-damage)
