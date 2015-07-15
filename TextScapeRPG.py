# Base game file
# version 1.3

import sys
import time
import os

# Global Variables
global playerHP
global enemyHP
playerHP = 10
enemyHP = 20

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
       elif(action==actionList[4]):
           help_func()
       else:
           print("Something's up...")

def help_func():
    print("Fight: Begins a fight")
    print("Fish: Try to fish for food")
    print("Cook: Cook the fish, or other food")
    print("Help: Gives general information about commands")
    actionPrompt()
def attack():
    global enemyHP
    global playerHP
    print("Enemy has lost 5 HP")
    time.sleep(0.3)
    print("Enemy attacks! You lost 1 HP")
    enemyHP -= 5
    playerHP -= 1
def run():
    print("You have run away!")
    time.sleep(0.1)
    actionPrompt()
def heal():
    global playerHP
    print("You have healed 2 HP!")
    playerHP += 2
    print("Your health is %i" % playerHP)
def fight():
    while(enemyHP > 1):
        fightActionList = ["a","h","r"]
        print("Your health: %i, enemy health: %i " % (playerHP, enemyHP))
        print("Type 'a' to attack, 'h' to heal, or 'r' to run!")
        action=input("Fight action: ")
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
actionList = ["fight", "fish", "cook", "heal", "help"]
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
