# Base game file
# v0.47-alpha

import sys
import time
import os
import random
import platform

# Global variables
global playerHP
global monsterHP
global playerBal
global baitCount
global fishCount
global cookedFish
playerBal = 1000
playerHP = 100
baitCount = 0
fishCount = 3
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

def clearScreen():
    if(platform.system()=="Windows"):
        os.system('cls')
    else:
        os.system('clear')

def selectMonster():
    global monsterName
    global monsterHP
    global monsterMaxHit
    global monsterXP
    global monsterCoins
    global monsterItemsDropped
    monsterSelect = random.randint(1, 4)
    monster=monsterList[monsterSelect]
    monsterName=monster[0]
    monsterHP=int(monster[1])
    monsterMaxHit=int(monster[2])
    monsterXP=int(monster[3])
    monsterCoins=int(monster[4])
    monsterItemsDropped=monster[5]

        # array([[ 0.,  0.,  0.,  0.,  0.],
        # [ 0.,  0.,  0.,  0.,  0.],
        # [ 0.,  0.,  0.,  0.,  0.],
        # [ 0.,  0.,  0.,  0.,  0.],
        # [ 0.,  0.,  0.,  0.,  0.]])

def actionPrompt():
    clearScreen()
    print("What would you like to do?")
    print("Enter 'help' for more options.")
    action=input("Action: ")
    if (action in actionList):
        if (action==actionList[0]):
            prefight()
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
            print("this doesn't work")
    else:
        print("broken")
        clearScreen()
        actionPrompt()

def help_func():
    print("Fight: Begins a fight")
    print("Fish: Try to fish for food")
    print("Cook: Cook the fish, or other food")
    print("Help: Gives general information about commands")
    time.sleep(3)
    actionPrompt()
def attackOpt():
    print("You attacked!")
    global monsterHP
    global playerHP
    print("Enemy has lost 5 HP")
    time.sleep(0.3)
    print("Enemy attacks! You lost 1 HP")
    monsterHP -= 5
    playerHP -= 1
def attackAdv():
    clearScreen()
    global monsterHP
    global playerHP
    global monsterMaxHit
    playerDMG = random.randint(0, 10)
    monsterDMG = random.randint(0, monsterMaxHit)
    time.sleep(0.1)
    print("You attacked! Enemy has lost %iHP" % playerDMG)
    time.sleep(0.1)
    print("Enemy attacks! You lost %i HP" % monsterDMG)
    monsterHP -= playerDMG
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
        print("\nYou have healed 5 HP! You have %i cooked fish left" % cookedFish)
        playerHP += 5
        print("Your health is %i" % playerHP)
        cookedFish -= 1
        time.sleep(0.8)
        actionPrompt()
    else:
        print("\nNot enough cooked fish!")
        time.sleep(0.6)
        actionPrompt()


def prefight():
    clearScreen()
    selectMonster()
    global monsterName
    global monsterXP
    print("")
    print(monsterName + " has appeared! HP:" + str(monsterHP))
    print("")
    time.sleep(1)
    fightAdv()

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
    clearScreen()
    global monsterGoblin
    global monsterName
    global monsterHP
    global monsterMaxHit
    global monsterXP
    global monsterCoins
    global monsterItemsDropped
    global playerBal
    while(monsterHP > 0):
        fightActionList = ["a","h","r"]
        print("\nYour HP: %i || Monster HP: %i" % (playerHP, monsterHP))
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
        if(playerHP < 0):
            print("You Lost")
            # Loss code here
        else:
            playerBal += monsterCoins
            time.sleep(3)
            print("You earned %i coins! Your balance is now: %i" % (monsterCoins, playerBal))
            time.sleep(1)
            actionPrompt()

def fish():
    clearScreen()
    global baitCount
    global fishCount
    global playerBal
    print("What would you like to do?")
    print("Type 'f' to fish, 'b' to buy bait, or 'e' to exit")
    fishAction=input("Fish action:")
    if(fishAction=="f"):
        if(baitCount == 0):
            print("You don't have any bait!")
            time.sleep(0.5)
            fish()
        else:
            fishCatch=["null", "Catfish", "Carp", "Salmon", "Whale, somehow"]
            fishChoose=random.randint(1, 4)
            print("You cast your line..")
            time.sleep(0.2)
            print("You feel a bite!")
            time.sleep(0.2)
            print("You reel in your fish!")
            time.sleep(0.2)
            print("You have caught: %a" % fishCatch[fishChoose])
            baitCount -= 1
            fishCount += 1
            time.sleep(0.6)
            fish()
    if(fishAction=="b"):
        print("\nWould you like to purchase some bait for 3 coins?")
        print("Your balance: %i" % playerBal)
        print("Type 'y' to buy 3 bait, or 'n' to cancel.")
        buyBait=input("Buy?: ")
        if (buyBait == "y"):
            if (playerBal>=3):
                print("\nYou have bought some bait!")
                playerBal -= 3
                baitCount += 3
                time.sleep(0.3)
                fish()
            else:
                print("You don't have enough coins!")
        elif (buyBait == "n"):
            print("That's not an option!")
            fish()
        else:
            fish()
    if(fishAction=="e"):
        actionPrompt()
    else:
        print("Invalid action!")
        actionPrompt()

def cook():
    global fishCount
    global cookedFish
    print("\nYou have %i raw fish & %i cooked fish." % (fishCount, cookedFish))
    print("Type the amount you'd like to cook, or 'e' to exit!")
    cookAction=input("Cook action: ")
    if(cookAction=="e"):
        actionPrompt()
    else:
        if(int(cookAction) > fishCount):
            print("\nYou don't have that many fish!")
        elif(int(cookAction) <= fishCount):
            fishCount -= int(cookAction)
            cookedFish += int(cookAction)
            print("\nYou have cooked %i fish!" % int(cookAction))
            print("You now have %i raw fish & %i cooked fish!" % (fishCount, cookedFish))
            time.sleep(1)
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
# Name, HP, MaxDamage, XP, Coins, Items
global monsterList
global monsterGoblin
global monsterSkeleton
global monsterRat
global monsterThief

monsterGoblin =   ["Goblin",   50, 8,  25, 3,    "Bones"]
monsterSkeleton = ["Skeleton", 30, 10, 15, 5,    "Bones"]
monsterRat =      ["Rat",      10, 1,  5,  0,    "Bones"]
monsterThief =    ["Thief",    75, 15, 38, 100,  "Bones"]
monsterList=["null",monsterGoblin,monsterSkeleton,monsterRat,monsterThief]
#

# Run program
actionPrompt()
