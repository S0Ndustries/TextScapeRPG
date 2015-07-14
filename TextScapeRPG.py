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
   print("You are now fighting.")
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
