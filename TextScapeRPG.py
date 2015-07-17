# Base game file
# v1.7.4-beta
# official version: 2.3

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
global caughtFish
# Global monster stats
global monsterGoblin
global monsterName
global monsterHP
global monsterMaxHit
global monsterXP
global monsterCoins
global monsterItemsDropped

# Functions
class unix:
    def clear():
        os.system('clear')

class windows:
    def clear():
        os.system('cls')

if platform.system()=="Windows":
    system = windows
else:
    system = unix

def loadTitle():
    s = "\n                                   Welcome to                                   \n\nd888888P                   dP   .d88888b                                      \n   88                      88   88.    \"'                                     \n   88  .d8888b. dP.  .dP d8888P `Y88888b. .d8888b. .d8888b. 88d888b. .d8888b. \n   88  88ooood8  `8bd8'    88         `8b 88'  `\"\" 88'  `88 88'  `88 88ooood8 \n   88  88.  ...  .d88b.    88   d8'   .8P 88.  ... 88.  .88 88.  .88 88.  ... \n   dP  `88888P' dP'  `dP   dP   `Y88888P' `88888P' `88888P8 88Y888P' `88888P' \n                                                            88                \n                                                            dP                \n"
    for c in s:
        sys.stdout.write('%s' % c )
        sys.stdout.flush()
        time.sleep(0.010)
def nameSelect():
    global playerHP
    global monsterHP
    global playerBal
    global baitCount
    global fishCount
    global cookedFish
    global caughtFish
    bonusNames = ["Elijah", "Evan", "betaTest"]
    print("Please enter your name!")
    name = input("Name: ")
    if(name in bonusNames):
        if(name==bonusNames[2]):
            playerBal = 9999
            playerHP = 999
            baitCount = 99
            fishCount = 99
            cookedFish = 99
            caughtFish = 99
        elif(name==bonusNames[0]):
            print("Welcome, Senpai.")
            playerBal = 1200
            playerHP = 130
            baitCount = 0
            fishCount = 0
            cookedFish = 0
            caughtFish = 0
            time.sleep(1.5)
        elif(name==bonusNames[1]):
            print("Welcome, Grandmaster Evan.")
            playerBal = 1200
            playerHP = 130
            baitCount = 0
            fishCount = 0
            cookedFish = 0
            caughtFish = 0
            time.sleep(1.5)
        else:
            print("Missing code for bonusName %s" % name)
    else:
        print("Welcome to TextScapeRPG, %s!" % name)
        playerBal = 1000
        playerHP = 100
        baitCount = 0
        fishCount = 0
        cookedFish = 0
        caughtFish = 0
        time.sleep(1.5)

class stats:
    def init():
        system.clear()
        stats.general()
        stats.fish()
        time.sleep(6)
        actionPrompt()
    def general():
        print("General Stats")
        print("Player Coins: %i" % playerBal)
        print("Player Health: %i" % playerHP)
    def fish():
        print("\nFishing Stats")
        print("Cooked Fish: %i" % cookedFish)
        print("Uncooked Fish: %i" % fishCount)
        print("Amount of Bait: %i" % baitCount)
        print("Total Fish Caught: %i" % caughtFish)

def runGame():
    system.clear()
    # loadTitle()
    nameSelect()
    actionPrompt()

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


def selectMonster():
    global monsterName
    global monsterHP
    global monsterMaxHit
    global monsterXP
    global monsterCoins
    global monsterItemsDropped
    monsterSelect = random.randint(1, (len(monsterList)-1))
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
    system.clear()
    print("What would you like to do?")
    print("Enter 'help' for more options.")
    action=input("Action: ").lower()
    if (action in actionList):
        if (action==actionList[0]):
            fight.setup()
        elif(action==actionList[1]):
            fish.init()
        elif(action==actionList[2]):
            #Jesse, we need to-
            cook.init()
        elif(action==actionList[3]):
            heal()
        elif(action==actionList[4]):
            help_func()
        elif(action==actionList[5]):
            fuck()
        elif(action==actionList[6]):
            fart()
        elif(action==actionList[7]):
            stats.init()
        elif(action==actionList[8]):
            system.clear()
            exit()
        else:
            print("this doesn't work")
    else:
        print("Sorry, invalid option.")
        time.sleep(1)
        system.clear()
        actionPrompt()

def help_func():
    print("Fight: Begins a fight")
    print("Fish: Try to fish for food")
    print("Cook: Cook the fish, or other food")
    print("Stats: Displays the current player stats")
    print("Heal: Heals the player")
    print("Help: Gives general information about commands")
    print("Exit: Closes the game")
    time.sleep(3)
    actionPrompt()

class fight:
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
    def run():
        print("You have run away!")
        time.sleep(0.1)
        actionPrompt()
    def setup():
        system.clear()
        selectMonster()
        global monsterName
        global monsterXP
        print("")
        print(monsterName + " has appeared! HP:" + str(monsterHP))
        print("")
        time.sleep(1)
        fight.adv()
    def message():
        system.clear()
        global monsterHP
        global playerHP
        global monsterMaxHit
        playerDMG = random.randint(0, 10)
        monsterDMG = random.randint(0, monsterMaxHit)
        time.sleep(0.1)
        print("You attacked! %s has lost %i HP" % (monsterName, playerDMG))
        time.sleep(0.1)
        print("%s attacks! You lost %i HP" % (monsterName, monsterDMG))
        monsterHP -= playerDMG
        playerHP -= monsterDMG
        time.sleep(0.3)
    def init():
        system.clear()
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
            if(action in fightActionList):
                if (action==fightActionList[0]):
                    fight.message()
                elif(action==fightActionList[1]):
                    fight.heal()
                elif(action==fightActionList[2]):
                    fight.run()
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

class fish:
    def init():
        system.clear()
        print("What would you like to do?")
        print("Type 'f' to fish, 'b' to buy bait, or 'e' to exit")
        fishAction=input("Fish action:")
        if(fishAction=="f"):
            fish.checkBait()
        elif(fishAction=="b"):
            fish.buyBait()
        elif(fishAction=="e"):
            actionPrompt()
        else:
            print("Invalid action!")
            fish.init()
    def checkBait():
        if (baitCount == 0):
            print("You don't have any bait!")
            time.sleep(0.5)
            fish.init()
        else:
            fish.fishing()
    def fishing():
        global baitCount
        global fishCount
        fishCatch=["null", "Catfish", "Carp", "Salmon", "Whale, somehow"]
        fishChoose=random.randint(1, (len(fishCatch)-1))
        print("You cast your line..")
        time.sleep(0.5)
        print("You feel a bite!")
        time.sleep(0.3)
        print("You reel in your fish!")
        time.sleep(0.2)
        print("You have caught: %a" % fishCatch[fishChoose])
        baitCount -= 1
        fishCount += 1
        caughtFish += 1
        time.sleep(0.6)
        fish.init()
    def buyBait():
        global playerBal
        global baitCount
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
                fish.init()
            else:
                print("You don't have enough coins!")
        elif (buyBait == "n"):
            fish.init()
        else:
            print("That's not an option!")
            fish.buyBait()

class cook:
    def init():
        global cookAmount
        print("\nYou habe %i raw fish & %i cooked fish." % (fishCount, cookedFish))
        print("Type the amount you'd like to cook, or 'e' to exit!")
        cookAction=input("Cook action: ")
        if(cookAction=="e"):
            actionPrompt()
        else:
            try:
                cookAmount=int(cookAction)
            except:
                cook.init()
            cook.cookFish()
    def cookFish():
        global cookAmount
        global fishCount
        global cookedFish
        if(cookAmount > fishCount):
            print("\nYou don't have that many fish!")
        elif(cookAmount <= fishCount and cookAmount > 0):
            fishCount -= cookAmount
            cookedFish += cookAmount
            print("\nYou have cooked %i fish!" % cookAmount)
            print("You now have %i raw fish & %i cooked fish!" % (fishCount, cookedFish))
            time.sleep(1)
            actionPrompt()
        else:
            system.clear()
            cook.init()

# Actions
actionList = ["fight", "fish", "cook", "heal", "help", "fuck", "fart", "stats", "exit"]
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
monsterWolf =     ["Wolf",     18, 12, 15, 0,    "Bones"]
monsterTroll =    ["Troll",    40, 9,  20, 15,   "Bones"]
monsterList=["null",monsterGoblin,monsterSkeleton,monsterRat,monsterThief,monsterWolf,monsterTroll]
#

# Run program
runGame()
