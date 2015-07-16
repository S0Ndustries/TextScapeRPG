# Base game file
# v0.80-alpha
# official version: 2.1

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

def printStats():
    clearScreen()
    print("General Stats")
    print("Current Coins: %i" % playerBal)
    print("Player Health: %i" % playerHP)
    print("\nFishing Stats")
    print("Cooked Fish: %i" % cookedFish)
    print("Uncooked Fish: %i" % fishCount)
    print("Amount of Bait: %i" % baitCount)
    actionPrompt
def fuck():
    global playerHP
    global playerBal
    fuckChoose=random.randint(1, 5)
    if(fuckChoose==1):
        print("You walk out onto the street...")
        time.sleep(0.7)
        print("You give Prostitute dirty looks.")
        time.sleep(1)
        print("Prostitute approaches!")
        time.sleep(0.7)
        print("Everything fades away.")
        time.sleep(1)
        print("You wake up with AIDS! You lose 25HP and 25 coins!")
        time.sleep(1.5)
        playerHP -= 25
        playerBal -= 25
        actionPrompt()
    elif(fuckChoose==2):
        print("You walk out onto the street...")
        time.sleep(0.7)
        print("You give Old Lady dirty looks.")
        time.sleep(1)
        print("Old Lady approaches!")
        time.sleep(0.7)
        print("Everything fades away.")
        time.sleep(1)
        print("You were pepper sprayed! You lose 10HP")
        time.sleep(1.5)
        playerHP -= 10
        actionPrompt()
    elif(fuckChoose==3):
        print("You walk out onto the street...")
        time.sleep(0.7)
        print("You give Little Boy dirty looks.")
        time.sleep(1)
        print("Police Officer approaches!")
        time.sleep(0.7)
        print("Everything fades away.")
        time.sleep(1)
        print("You were arrested! You were fined 50 coins")
        time.sleep(1.5)
        playerBal -= 50
        actionPrompt()
    elif(fuckChoose==4):
        print("You walk out onto the street...")
        time.sleep(0.7)
        print("You give Nun dirty looks.")
        time.sleep(1)
        print("Pope approaches!")
        time.sleep(0.7)
        print("Everything fades away.")
        time.sleep(1)
        print("You wake up with AIDS! You lost 25HP!")
        time.sleep(1.5)
        playerHP -= 25
        actionPrompt()
    elif(fuckChoose==5):
        print("You walk out onto the street...")
        time.sleep(0.7)
        print("You give Prostitute dirty looks.")
        time.sleep(1)
        print("Prostitute approaches!")
        time.sleep(0.7)
        print("Everything fades away.")
        time.sleep(1)
        print("You wake up satisfied! You gained 25HP and lost 25 coins")
        time.sleep(1.5)
        playerHP += 25
        playerBal -= 25
        actionPrompt()
def fart():
    print("You empty your bowels of the fumes plaguing them.")
    time.sleep(0.7)
    print("Everything fades away...")
    time.sleep(1)
    print("You wake up in Hospital! You have lost 5HP")
    time.sleep(1.5)
    actionPrompt()

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
        elif(action==actionList[5]):
            fuck()
        elif(action==actionList[6]):
            fart()
        elif(action=actionList[7]):
            printStats()
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
    print("Stats: Displays the current player stats")
    print("Heal: Heals the player")
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
    print("You attacked! %s has lost %iHP" % (monsterName, playerDMG))
    time.sleep(0.1)
    print("%s attacks! You lost %i HP" % (monsterName, monsterDMG))
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
    elif(type(cookAction) == int):
        cookAction=int(cookAction)
        if(cookAction > fishCount):
            print("\nYou don't have that many fish!")
        elif(cookAction <= fishCount):
            fishCount -= cookAction
            cookedFish += cookAction
            print("\nYou have cooked %i fish!" % cookAction)
            print("You now have %i raw fish & %i cooked fish!" % (fishCount, cookedFish))
            time.sleep(1)
            actionPrompt()
    else:
        cook()
#

# Actions
actionList = ["fight", "fish", "cook", "heal", "help", "fuck", "fart", "stats"]
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
