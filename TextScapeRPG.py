# Base game file
# version 1.2

import sys
import time
import os

# Functions
def actionPrompt():
   print("What would you like to do?")
   print("Enter 'help' for more options.")
   action=input("Action: ")
   if (action in actionList):
       if (action==actionList[0]):
           fight()
       elif(action==actionList[1]):
           fish()
       elif(action==actionList[2]):
           #Jesse, we need to-
           cook()
       elif(action==actionList[3]):
           heal()
       else:
           print("Something's up...")

def fight():
   playerHP = 10
   enemyHP = 20
   fightActionList = ["a","h","r"]
   print("You are now fighting!")
   print("Your health: %i, enemy health: %i ", % 10, 20)
   print("Type 'a' to attack, 'h' to heal, or 'r' to run!")
   action=input("Action: ")
   if (action in fightActionList):
        if (action==fightActionList[0]):
            attack()
        elif(action==fightActionList[1]):
            heal()
        elif(action==fightActionList[2]):
            run()
        else:
            print("Something's up...")
   def attack()
      print("Enemy has lost %i HP", %, 5)
      enemyHP -= 5
      print("Enemy attacks! You lost %i HP", % 1)
      playerHP -= 1
      fight()
#

# Actions
actionList = ["fight", "fish", "cook", "heal"]
#

#    Variables
# User skills
attack = 1
strength = 1
defence = 1
health = 1
fishing = 1
cooking = 1
#

# Monsters
monsterGoblin = ["Goblin", "50", "8", "25", "Bones"]
#

# Run program
actionPrompt()
