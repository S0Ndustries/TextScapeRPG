# Base game file
# version 1.4

import sys
import time
import os
import random

# Global Variables, Sort of
global playerHP
global enemyHP
global playerBal
global baitCount
global fishCount
playerBal = 1000
playerHP = 10
enemyHP = 20
baitCount = 0
fishCount = 0

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
def attackOpt():
    print("You attacked!")
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
                attackOpt()
             elif(action==fightActionList[1]):
                heal()
             elif(action==fightActionList[2]):
                run()
             else:
                print("Something's up...")

def fish():
    global baitCount
    global fishCount
    global playerBal
    if(baitCount == 0):
        print("You don't have any bait!")
        print("Would you like to purchase some bait for 3gp?")
        print("Your balance: %i" % playerBal)
        print("Type 'y' to buy, or 'n' to cancel.")
        buyBait=input("Buy?: ")
        if (buyBait == "y"):
            if (playerBal>=3):
                print("You have bought some bait!")
                playerBal -= 3
                baitCount += 1
                fish()
            else:
                print("You don't have enough gp!")
        else:
            fish()
    else:
        fishCatch=["null", "Catfish", "Carp", "Salmon", "Whale, somehow"]
        fishChoose=random.randint(1, 4)
        print("You cast your line..")
        time.sleep(1)
        print("You feel a bite!")
        time.sleep(0.2)
        print("You reel in your fish!")
        print("You have caught: %a" % fishCatch[fishChoose])
        baitCount -= 1
        fishCount += 1

#

# Actions
actionList = ["fight", "fish", "cook", "heal", "help"]
#

#    Variables
# User skills
global attack
global strength
global defence
global health
global fishing
global cooking

attack = 1
strength = 1
defence = 1
health = 1
fishing = 1
cooking = 1
#

# Monsters
# Name, IDK, IDK, IDK, IDK, Drops
monsterGoblin = ["Goblin", "50", "8", "25", "3", "Bones"]
monsterTheif = ["Theif", "", "", "", "", "Amulet"]
#

# Run program
actionPrompt()
