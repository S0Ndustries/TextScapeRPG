# Base game file
# version 1.4

import sys
import time
import os
import random

# Global variables
global playerHP
global enemyHP
global playerBal
global baitCount
global fishCount
global cookedFish
playerBal = 1000
playerHP = 10
enemyHP = 20
baitCount = 0
fishCount = 0
cookedFish = 0
# Global monster stats
global monsterGoblin
global monsterName
global monsterHP
global monsterMaxHit
global monsterXP
global monsterCoins
global monsterItemsDropped

# Functions

def fightMonster():
    monsterSelect = random.randint(0, 0)
    if(monsterSelect==0):
        monsterGoblin =   ["Goblin",   "50", "8",  "25", "3",    "Bones"]
        monsterName = monsterGoblin[0]
        monsterHP = monsterGoblin[1]
        monsterMaxHit = monsterGoblin[2]
        monsterXP = monsterGoblin[3]
        monsterCoins = monsterGoblin[4]
        monsterItemsDropped = monsterGoblin[5]
    if(monsterSelect==1):
        monsterSkeleton = ["Skeleton", "30", "10", "15", "5",    "Bones"]
    if(monsterSelect==2):
        thismonsterRat =  ["Rat",      "10", "1",  "5",  "0",    "Bones"]
    if(monsterSelect==3):
        monsterThief =    ["Thief",    "75", "15", "38", "100",  "Bones"]
        # array([[ 0.,  0.,  0.,  0.,  0.],
        # [ 0.,  0.,  0.,  0.,  0.],
        # [ 0.,  0.,  0.,  0.,  0.],
        # [ 0.,  0.,  0.,  0.,  0.],
        # [ 0.,  0.,  0.,  0.,  0.]])

def actionPrompt():
   print("What would you like to do?")
   print("Enter 'help' for more options.")
   action=input("Action: ")
   if (action in actionList):
       if (action==actionList[0]):
           fightAdv()
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
def attackAdv():
    print("You attacked!")
    global monsterHP
    global playerHP
    global monsterMaxHit
    playerDMG = random.randint(0, 10)
    monsterDMG = random.randint(0, monsterMaxHit)
    print("Enemy has lost %iHP" % playerDMG)
    time.sleep(0.3)
    print("Enemy attacks! You lost %i HP" % monsterDMG)
    enemyHP -= playerDMG
    playerHP -= monsterDMG
    time.sleep(0.3)
def run():
    print("You have run away!")
    time.sleep(0.1)
    actionPrompt()
def heal():
    global cookedFish
    global playerHP
    if(cookedFish > 0):
        print("You have healed 5 HP! You have %i cooked fish left" % cookedFish)
        playerHP += 5
        print("Your health is %i" % playerHP)
        cookedFish -= 1
    else:
        print("Not enough cooked fish!")
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
def fightAdv():
    global monsterGoblin
    global monsterName
    global monsterHP
    global monsterMaxHit
    global monsterXP
    global monsterCoins
    global monsterItemsDropped
    fightMonster()
    while(monsterHP > 0):
        fightActionList = ["a","h","r"]
        print(monsterName + " has appeared! HP:" + str(monsterXP))
        print("Your health: %i" % (playerHP)
        time.sleep(0.2)
        print("Type 'a' to attack, 'h' to heal, or 'r' to run!")
        action=input("Fight action: ")
        if (action in fightActionList):
             if (action==fightActionList[0]):
                attackAdv()
             elif(action==fightActionList[1]):
                heal()
             elif(action==fightActionList[2]):
                run()
             else:
                print("Something's up...")
    else:
        playerBal += monsterCoins

def fish():
    global baitCount
    global fishCount
    global playerBal
    print("What would you like to do?")
    print("Type 'f' to fish, 'b' to buy bait, or 'e' to exit")
    fishAction=input("Fish action:")
    if(fishAction=="f"):
        if(baitCount == 0):
            print("You don't have any bait!")
            fish()
        else:
            print("You cast your line..")
            time.sleep(0.4)
            print("You feel a bite!")
            time.sleep(0.2)
            print("You reel in your fish!")
            print("You have caught: %s!" % "a fish")
            baitCount -= 1
            fishCount += 1
            fish()
    if(fishAction=="b"):
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
        elif (buyBait == "n"):
            print("That's not an option!")
            fish()
        else:
            fish()
    if(fishAction=="e"):
        actionPrompt()
    else:
        print("Invalid action!")
        return

def cook():
    global fishCount
    global cookedFish
    print("You have %i raw fish & %i cooked fish." % (fishCount, cookedFish))
    print("Type the amount you'd like to cook, or 'e' to exit!")
    cookAction=input("Cook action: ")
    if(cookAction=="n"):
        actionPrompt()
    else:
        if(int(cookAction) > fishCount):
            print("You don't have that many fish!")
        elif(int(cookAction) <= fishCount):
            fishCount -= int(cookAction)
            cookedFish += int(cookAction)
            print("You have cooked %i fish!" % int(cookAction))
            print("You now have %i raw fish & %i cooked fish!" % (fishCount, cookedFish))
            actionPrompt()
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
global monsterList
monsterList["monsterGoblin","monsterSkeleton","monsterRat","monsterThief"]

global monsterGoblin
global monsterSkeleton
global monsterRat
global monsterThief
monsterGoblin =   ["Goblin",   "50", "8",  "25", "3",    "Bones"]
monsterSkeleton = ["Skeleton", "30", "10", "15", "5",    "Bones"]
monsterRat =      ["Rat",      "10", "1",  "5",  "0",    "Bones"]
monsterThief =    ["Thief",    "75", "15", "38", "100",  "Bones"]
#

# Run program
actionPrompt()
