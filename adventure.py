# Dean Blank
# Section: CS-172-A; Lab 061

import sys
import random
from Monster1 import *
from Monster2 import *
from Monster3 import *
from Monster4 import *
from hero import *

# intro
print('\033[1m' + 'Welcome to the Adventure Battle!'+ '\033[0m')


# main function
def main():

  random.seed(0)
  name = input('What is the name of your hero? \n') # asks for hero name
  hero = Hero(name)

  while True:
    try:  # loop to ask for number of monsters to fight. Checks for invalid inputs
      num = int(input('How many monsters will ' + name + ' battle? \n'))
      if 0<num<=4:
        break
      print('Enter integer between 1 and 4')
    except:
      print('Please enter an integer.')

  one = Monster1()  # instantiating monster classes
  two = Monster2()
  three = Monster3()
  four = Monster4()

  l = [one,two,three,four]    # creating random list of enemies
  random.shuffle(l) # shuffling monster list to make fight random
  x = 0
  for i in range(0,num):  # battling random list of enemies
    winner = battle(hero,l[x])
    x+=1

  # if the battle function returns hero as winner, print
  if winner == hero:
    print('You have defeated all enemies and saved the world. Good job.')



# _____________________Battle Function is Below_________________________

def battle(hero, monster):

  # encountering a montser
  print("You have encountered a " + monster.getName() + "!")

  #Loop until either one is unconscious
  while(hero.getHealth() > 0 and monster.getHealth() > 0):

    # printing health and status of hero
    print('\033[1m' + hero.getName()+ ': ' + str(hero.getHealth()) + '/100 health' + '\033[0m')
    print('Remaining: ' + str(hero.getFireball()) + ' Fireballs, ' + str(hero.getPotion()) + ' Potions')
  
    # used to record the damage done
    before_health = monster.getHealth()
    before_health1 = hero.getHealth()

    # Getting command for hero and using command on monster
    command = input('Enter Command: sword shield fireball potion exit\n')
    while (command != 'sword') and (command != 'shield') and (command != 'fireball') and (command != 'potion') and (command != 'exit'):
      print('invalid command.') # will print invalid input if command doesnt meet requirement in while loop
      command = input('Enter Command: sword shield fireball potion exit\n')

    if command == 'sword':
      hero.basicAttack(monster) # basic attack monster
      if monster.getHealth()>=0:  # if monster is still alive print its current health
        print('\033[1m' + monster.getName()+ ': ' + str(monster.getHealth()) + '/100 health' + '\033[0m') # print health of monster
      else:
        print('\033[1m' + monster.getName()+ ': 0/100 health' + '\033[0m') # print health of monster as 0 health if health falls below zero
      
    elif command == 'shield': 
      hero.defense(monster) # use shield
      if monster.getHealth()>=0:  
        print('\033[1m' + monster.getName()+ ': ' + str(monster.getHealth()) + '/100 health' + '\033[0m') # print health of monster
      else:
        print('\033[1m' + monster.getName()+ ': 0/100 health' + '\033[0m') # print health of monster as 0 health if health falls below zero

    elif command == 'fireball':
      if hero.getFireball()> 0: # if the hero has enough fireballs it will use fireball
        hero.specialAttack(monster) # special attack monster
      else:
        print('Fireball Failed! Ran out of special attack.')
      if monster.getHealth()>=0:  
        print('\033[1m' + monster.getName()+ ': ' + str(monster.getHealth()) + '/100 health' + '\033[0m') # print health of monster
      else:
        print('\033[1m' + monster.getName()+ ': 0/100 health' + '\033[0m') # print health of monster as 0 health if health falls below zero
    elif command == 'potion':
      if hero.getPotion() > 0:  # if the hero has enough potions it will use potion
        hero.potion() # use potion
      else:
        print('Potion Failed! No potions left.')
      if monster.getHealth()>=0:  
        print('\033[1m' + monster.getName()+ ': ' + str(monster.getHealth()) + '/100 health' + '\033[0m') # print health of monster
      else:
        print('\033[1m' + monster.getName()+ ': 0/100 health' + '\033[0m') # print health of monster as 0 health if health falls below zero
      
    else:
      sys.exit()




    #Determine what move the monster makes    # used this attack % probability from lab4
    #Probabilities:
    # 60% chance of standard attack
    # 20% chance of defense move
    # 20% chance of special attack move

    #Pick a number between 1 and 100
    if monster.getHealth() > 0: # if the monster is dead, then it can't attack
      move = random.randint(1,100)

      if(move >=1 and move <= 60):
        #Attack!
        monster.basicAttack(hero)
        
      elif move>=61 and move <= 80:
        #Defend!
        monster.defense(hero)
    
      else:
        #Special Attack!
        monster.specialAttack(hero)


  #Determine Results of the match
  if(hero.getHealth() < 1): # if hero is dead, print dead and exit program
    print('You died!')
    sys.exit()

  if(monster.getHealth() < 1):  # if monster is dead, print enemy is dead and return hero as winner
    monster.setHealth(0)
    print('Enemy is defeated!')
    return hero
 

# run main program
if __name__=="__main__":
  main()

