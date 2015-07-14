# Base game file
# version 1.3

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

playerHP = 10
enemyHP = 20
def attack():
    print("Enemy has lost 5 HP")
    enemyHP = enemyHP - 5
    print("Enemy attacks! You lost 1 HP")
    playerHP = playerHP - 1
def run():
    print("You have run away!")
    time.sleep(0.1)
    actionPrompt()
def heal():
    print("You have healed 2HP!")
    playerHP = playerHP + 2
def fight():
    while(enemyHP > 1):
        fightActionList = ["a","h","r"]
        print("Your health: %i, enemy health: %i " % (playerHP, enemyHP))
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
