# Base game file
# v2.1.0-beta

import sys
import time
import os
import random
import platform
import math

# Global variables
global playerHP
global monsterHP
global playerBal
global baitCount
global fishCount
global cookedFish
global caughtFish
global exp
global level

# Global monster stats
global monsterGoblin
global monsterName
global monsterHP
global monsterMaxHit
global monsterXP
global monsterCoins
global monsterItemsDropped

# EXP stats
global fishEXP
fishEXP = 0

# Player Skills
attackSkill = 1
strengthSkill = 1
defenceSkill = 1
rangedSkill = 1
magicSkill = 1
healthSkill = 1
craftingSkill = 1
miningSkill = 1
fishingSkill = 1
cookingSkill = 1
woodcuttingSkill = 1
agilitySkill = 1
herbloreSkill = 1
farmingSkill = 1
huntingSkill = 1
summoningSkill = 1

# Functions
class unix:
    def clear():
        os.system('clear')
        print("<--- TextScapeRPG - by - S0Ndustries --->\n")

class windows:
    def clear():
        os.system('cls')
        print("<--- TextScapeRPG - by - S0Ndustries --->\n")

if platform.system()=="Windows":
    system = windows
else:
    system = unix

def initializeGame():
    # Sets all fish item traits.
    fishAdv.fishes()
    fishAdv.firstStats()
    # Anything else to be initialized can go here

def loadTitle():
    system.clear()
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
    global baitCount
    global fishEXP
    global feathers
    bonusNames = ["Elijah", "Evan", "betaTest"]
    print("Please enter your name!")
    name = input("Name: ")
    if(name in bonusNames):
        if(name==bonusNames[2]):
            print("Welcome, beta tester.")
            playerBal = 9999
            playerHP = 999
            baitCount = 99
            fishCount = 99
            cookedFish = 99
            caughtFish = 99
            baitCount = 99
            fishEXP = 99999999
            feathers = 99
            time.sleep(1.5)
        elif(name==bonusNames[0]):
            print("Welcome, Senpai.")
            playerBal = 1200
            playerHP = 130
            baitCount = 0
            fishCount = 0
            cookedFish = 0
            caughtFish = 0
            baitCount = 0
            fishEXP = 0
            feathers = 0
            time.sleep(1.5)
        elif(name==bonusNames[1]):
            print("Welcome, Coding Grandmaster Evan.")
            playerBal = 1200
            playerHP = 130
            baitCount = 0
            fishCount = 0
            cookedFish = 0
            caughtFish = 0
            baitCount = 0
            fishEXP = 0
            feathers = 0
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
        baitCount = 0
        fishEXP = 0
        feathers = 0
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
        print("Fishing Level: %i" % fishingSkill)

def runGame():
    system.clear()
    # loadTitle()
    initializeGame()
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

def luck():
    luckLevel = 1
    luckChancePercent = 1

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

def actionPrompt():
    system.clear()
    print("What would you like to do?")
    print("Enter 'help' for more options.")
    action=input("Action: ").lower()
    if (action in actionList):
        if (action==actionList[0]):
            fight.setup()
        elif(action==actionList[1]):
            fishAdv.prompt()
        elif(action==actionList[2]):
            # Jesse, we need to -
            cook.init()
        elif(action==actionList[3]):
            fight.heal(0)
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
            print("This doesn't work")
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
    def heal(m):
        global cookedFish
        global playerHP
        if(cookedFish > 0):
            print("\nYou have healed 5 HP! You have %i cooked fish left" % cookedFish)
            playerHP += 5
            print("Your health is %i" % playerHP)
            cookedFish -= 1
            time.sleep(0.8)
            if(m):
                fight.ask()
            else:
                actionPrompt()
        else:
            print("\nNot enough cooked fish!")
            time.sleep(0.6)
            if(m):
                fight.ask()
            else:
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
        fight.ask()
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
    def ask():
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
                    fight.heal(1)
                elif(action==fightActionList[2]):
                    fight.run()
                else:
                    print("Something's up...")
        else:
            if(playerHP < 0):
                print("You Lost")
                # Loss code here
                actionPrompt()
            else:
                playerBal += monsterCoins
                time.sleep(0.5)
                print("\nYou earned %i coins! Your balance is now: %i" % (monsterCoins, playerBal))
                time.sleep(2.5)
                actionPrompt()

class cook:
    def init():
        global cookAmount
        print("\nYou have %i raw fish & %i cooked fish." % (fishCount, cookedFish))
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
            cook.init()
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

class fishAdv():
    # Fish arrays
    global minnow
    global crayfish
    global shrimp
    global sardine
    global karambwanji
    global herring
    global anchovies
    global casket
    global mackerel
    global oyster
    global seaweed
    global trout
    global cod
    global pike
    global slimyeel
    global salmon
    global frogspawn
    global tuna
    global caveeel
    global rainbowfish
    global lobster
    global bass
    global swordfish
    global lavaeel
    global monkfish
    global karambwan
    global shark
    global baronshark
    global cavefish
    global rocktail
    # Other variables
    global fishAction
    global fishLevel
    global fishEXP
    global feathers
    global baitCount

    def myEXP(iEXP):
        global exp
        global level
        exp = iEXP
        if(exp < 83):
            level = 1
        elif(exp < 174):
            level = 2
        elif(exp < 276):
            level = 3
        elif(exp < 388):
            level = 4
        elif(exp < 512):
            level = 5
        elif(exp < 650):
            level = 6
        elif(exp < 801):
            level = 7
        elif(exp < 969):
            level = 8
        elif(exp < 1154):
            level = 9
        elif(exp < 1358):
            level = 10
        elif(exp < 1584):
            level = 11
        elif(exp < 1833):
            level = 12
        elif(exp < 2107):
            level = 13
        elif(exp < 2411):
            level = 14
        elif(exp < 2746):
            level = 15
        elif(exp < 3115):
            level = 16
        elif(exp < 3523):
            level = 17
        elif(exp < 3973):
            level = 18
        elif(exp < 4470):
            level = 19
        elif(exp < 5018):
            level = 20
        elif(exp < 5624):
            level = 21
        elif(exp < 6291):
            level = 22
        elif(exp < 7028):
            level = 23
        elif(exp < 7842):
            level = 24
        elif(exp < 8740):
            level = 25
        elif(exp < 9730):
            level = 26
        elif(exp < 10824):
            level = 27
        elif(exp < 12031):
            level = 28
        elif(exp < 13363):
            level = 29
        elif(exp < 14833):
            level = 30
        elif(exp < 16456):
            level = 31
        elif(exp < 18247):
            level = 32
        elif(exp < 20224):
            level = 33
        elif(exp < 22406):
            level = 34
        elif(exp < 24815):
            level = 35
        elif(exp < 27473):
            level = 36
        elif(exp < 30408):
            level = 37
        elif(exp < 33648):
            level = 38
        elif(exp < 37224):
            level = 39
        elif(exp < 41171):
            level = 40
        elif(exp < 45529):
            level = 41
        elif(exp < 50339):
            level = 42
        elif(exp < 55649):
            level = 43
        elif(exp < 61512):
            level = 44
        elif(exp < 67983):
            level = 45
        elif(exp < 75127):
            level = 46
        elif(exp < 83014):
            level = 47
        elif(exp < 91721):
            level = 48
        elif(exp < 101333):
            level = 49
        elif(exp < 111945):
            level = 50
        elif(exp < 123660):
            level = 51
        elif(exp < 136594):
            level = 52
        elif(exp < 150872):
            level = 53
        elif(exp < 166636):
            level = 54
        elif(exp < 184040):
            level = 55
        elif(exp < 203254):
            level = 56
        elif(exp < 224466):
            level = 57
        elif(exp < 247886):
            level = 58
        elif(exp < 273742):
            level = 59
        elif(exp < 302288):
            level = 60
        elif(exp < 333804):
            level = 61
        elif(exp < 368599):
            level = 62
        elif(exp < 407015):
            level = 63
        elif(exp < 449428):
            level = 64
        elif(exp < 496254):
            level = 65
        elif(exp < 547953):
            level = 66
        elif(exp < 605032):
            level = 67
        elif(exp < 668051):
            level = 68
        elif(exp < 737627):
            level = 69
        elif(exp < 814445):
            level = 70
        elif(exp < 899257):
            level = 71
        elif(exp < 992895):
            level = 72
        elif(exp < 1096278):
            level = 73
        elif(exp < 1210421):
            level = 74
        elif(exp < 1336443):
            level = 75
        elif(exp < 1475581):
            level = 76
        elif(exp < 1629200):
            level = 77
        elif(exp < 1798808):
            level = 78
        elif(exp < 1986068):
            level = 79
        elif(exp < 2192818):
            level = 80
        elif(exp < 2421087):
            level = 81
        elif(exp < 2673114):
            level = 82
        elif(exp < 2951373):
            level = 83
        elif(exp < 3258594):
            level = 84
        elif(exp < 3597792):
            level = 85
        elif(exp < 3972294):
            level = 86
        elif(exp < 4385776):
            level = 87
        elif(exp < 4842295):
            level = 88
        elif(exp < 5346332):
            level = 89
        elif(exp < 5902831):
            level = 90
        elif(exp < 6517253):
            level = 91
        elif(exp < 7195629):
            level = 92
        elif(exp < 7944614):
            level = 93
        elif(exp < 8771558):
            level = 94
        elif(exp < 9684577):
            level = 95
        elif(exp < 10692629):
            level = 96
        elif(exp < 11805606):
            level = 97
        elif(exp < 13034431):
            level = 98
        elif(exp < 14391160):
            level = 99
        else:
            level = 99

    def stats():
        global fishEXP
        global fishLevel
        global exp
        global level
        fishAdv.myEXP(fishEXP)
        fishLevel = level
        print("Your fishing XP amount is: %i" % fishEXP)
        print("Your fishing level is now: %i" % fishLevel)
        rexturn = input("Press enter to return")
        fishAdv.prompt()
    def firstStats():
        global fishEXP
        global fishLevel
        global exp
        global level
        fishAdv.myEXP(fishEXP)
        fishLevel = level

    def loadBar():
        s = "[==========]"
        for c in s:
            sys.stdout.write('%s' % c )
            sys.stdout.flush()
            time.sleep(0.2)

    def tBaits(fType):
        global fishEXP
        if(fType[2] == 0):
            print("\nYou cast your line into the water.")
            fishAdv.loadBar()
            print("\nYour line is hooked!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(1)
        elif(fType[2] == 1):
            print("\nYou thrust your cage into the water.")
            fishAdv.loadBar()
            print("\nYou pull it back out!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(1)
        elif(fType[2] == 2):
            print("\nYou dip your small net into the water.")
            fishAdv.loadBar()
            print("\nYou pull it back out!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(1)
        elif(fType[2] == 3):
            print("\nYou cast your large net into the water.")
            fishAdv.loadBar()
            print("\nYou pull it back out!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(1)
        elif(fType[2] == 4):
            print("\nYou cast your line into the water.")
            fishAdv.loadBar()
            print("\nYou reel it in!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(1)
        elif(fType[2] == 5):
            print("\nYou stab your harpoon into the water.")
            fishAdv.loadBar()
            print("\nYou pull it back out!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(1)
        elif(fType[2] == 6):
            print("\nYou place your lobster pot into the water.")
            fishAdv.loadBar()
            print("\nYou pull it back out!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(1)
        elif(fType[2] == 7):
            print("\nYou cast your line into the water.")
            fishAdv.loadBar()
            print("\nYou reel it in!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(1)
        elif(fType[2] == 6):
            print("\nYou mysteriously use your karambwanvessel.")
            fishAdv.loadBar()
            print("\nYou feel a bite!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(1)
        elif(fType[2] == 7):
            print("\nYou mysteriously use your living minerals.")
            fishAdv.loadBar()
            print("\nYou feel a bite!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(1)

    def prompt():
        system.clear()
        global fishAction
        fishCMDs = ["0","1","2","3","4","5","6","7","8","9","list","guide","exit", "stats"]
        print("Enter an action, type 'guide' for help, or 'exit' to exit!")
        fishAction=input("Fish action: ")
        if (fishAction in fishCMDs):
            if (fishAction == "list"):
                fishAdv.list()
            elif(fishAction == "guide"):
                fishAdv.guide()
            elif(fishAction == "exit"):
                print("Exiting...")
                time.sleep(1)
            elif(fishAction == "stats"):
                fishAdv.stats()
            else:
                fishAdv.fish(fishAction)
        else:
            print("That's not a command!")
            time.sleep(1.5)
            fishAdv.prompt()

    def guide():
        print("Fishing commands list:\n")
        print("0 = Fishing bait")
        print("   Level(s): 1, 5, 10, 25, 28, 38, 85\n")
        print("1 = Crayfish Cage")
        print("   Level(s): 1\n")
        print("2 = Small fishing net")
        print("   Level(s): 1, 5, 15, 33, 62\n")
        print("3 = Big fishing net")
        print("   Level(s): 16, 23, 46\n")
        print("4 = Fly fishing rod + feathers")
        print("   Level(s): 20, 30, 38\n")
        print("5 = Harpoon")
        print("   Level(s): 35, 50, 76\n")
        print("6 = Lobster Pot")
        print("   Level(s): 40\n")
        print("7 = Oily fishing rod")
        print("   Level(s): 53\n")
        print("8 = Karambwan vessel")
        print("   Level(s): 65\n")
        print("9 = Living minerals")
        print("   Level(s): 90")
        print("\nlist = Displays a list of all fish + level & bait needed.")
        print("\nexit = Will exit back to main menu")
        print("\nstats = Will display fishing stats.")
        done = input("\nPress enter to continue")
        fishAdv.prompt()

    def list():
        print("Help will be here!")
        time.sleep(1.5)
        fishAdv.prompt()

    def fishes():
        global minnow
        global crayfish
        global shrimp
        global sardine
        global karambwanji
        global herring
        global anchovies
        global casket
        global mackerel
        global oyster
        global seaweed
        global trout
        global cod
        global pike
        global slimyeel
        global salmon
        global frogspawn
        global tuna
        global caveeel
        global rainbowfish
        global lobster
        global bass
        global swordfish
        global lavaeel
        global monkfish
        global karambwan
        global shark
        global baronshark
        global cavefish
        global rocktail
        minnow      = ["Minnow",       1,  0, 10 ]
        crayfish    = ["Crayfish",     1,  1, 10 ]
        shrimp      = ["Shrimps",      1,  2, 10 ]
        sardine     = ["Sardine",      5,  0, 20 ]
        karambwanji = ["Karambwanji",  5,  2, 5  ]
        herring     = ["Herring",      10, 0, 30 ]
        anchovies   = ["Anchovies",    15, 1, 40 ]
        casket      = ["Casket",       16, 3, 10 ]
        mackerel    = ["Mackerel",     16, 3, 20 ]
        oyster      = ["Oyster",       16, 3, 10 ]
        seaweed     = ["Seaweed",      16, 3, 1  ]
        trout       = ["Trout",        20, 4, 50 ]
        cod         = ["Cod",          23, 3, 45 ]
        pike        = ["Pike",         25, 0, 60 ]
        slimyeel    = ["Slimy eel",    28, 0, 65 ]
        salmon      = ["Salmon",       30, 4, 70 ]
        frogspawn   = ["Frog spawn",   33, 2, 75 ]
        tuna        = ["Tuna",         35, 5, 80 ]
        caveeel     = ["Cave eel",     38, 0, 80 ]
        rainbowfish = ["Rainbow fish", 38, 4, 80 ]
        lobster     = ["Lobster",      40, 6, 90 ]
        bass        = ["Bass",         46, 3, 100]
        swordfish   = ["Swordfish",    50, 5, 100]
        lavaeel     = ["Lava eel",     53, 7, 60]
        monkfish    = ["Monkfish",     62, 2, 120]
        karambwan   = ["Karambwan",    65, 8, 105]
        shark       = ["Shark",        76, 5, 110]
        baronshark  = ["Baron shark",  76, 5, 110]
        # seaturtle   = ["Sea turtle",   79, 69, 38]
        # mantaray    = ["Manta Ray",    81, 69, 46]
        cavefish    = ["Cavefish",     85, 0, 300]
        rocktail    = ["Rocktail",     90, 9, 380]
        # tigershark  = ["Tiger Shark",  95, 69, 69]

    def fish(baitSel):
        # Fish arrays
        global minnow
        global crayfish
        global shrimp
        global sardine
        global karambwanji
        global herring
        global anchovies
        global casket
        global mackerel
        global oyster
        global seaweed
        global trout
        global cod
        global pike
        global slimyeel
        global salmon
        global frogspawn
        global tuna
        global caveeel
        global rainbowfish
        global lobster
        global bass
        global swordfish
        global lavaeel
        global monkfish
        global karambwan
        global shark
        global baronshark
        global cavefish
        global rocktail
        # Other variables
        global fishAction
        global fishLevel
        global feathers
        global baitCount
        fishAction = baitSel
        baitType = ["bait","crayfishcage","smallnet","bignet","flyfishingrod","harpoon","lobsterpot","oilyfishingrod","karambwanvessel","livingminerals"]
        baitTypeNum = ["0","1","2","3","4","5","6","7","8","9"]
        if(str(fishAction) in baitTypeNum):
            if(fishAction == "0"):
                if(baitCount >= 1):
                    baitCount -= 1
                    if(fishLevel >= 85):
                        fishAdv.tBaits(cavefish)
                    elif(fishLevel >= 38):
                        fishAdv.tBaits(caveeel)
                    elif(fishLevel >= 28):
                        fishAdv.tBaits(slimyeel)
                    elif(fishLevel >= 25):
                        fishAdv.tBaits(pike)
                    elif(fishLevel >= 10):
                        fishAdv.tBaits(herring)
                    elif(fishLevel >= 5):
                        print(baitCount)
                        fishAdv.tBaits(sardine)
                    else:
                        fishAdv.tBaits(minnow)
                else:
                    print("Not enough bait!")
                    time.sleep(1)
                fishAdv.prompt()
            elif(fishAction == "1"):
                fishAdv.tBaits(crayfish)
                fishAdv.prompt()
            elif(fishAction == "2"):
                if(fishLevel >= 62):
                    fishAdv.tBaits(monkfish)
                elif(fishLevel >= 33):
                    fishAdv.tBaits(frogspawn)
                elif(fishLevel >= 15):
                    fishAdv.tBaits(anchovies)
                elif(fishLevel >= 5):
                    fishAdv.tBaits(karambwanji)
                else:
                    fishAdv.tBaits(shrimp)
                fishAdv.prompt()
            elif(fishAction == "3"):
                if(fishLevel >= 46):
                    fishAdv.tBaits(bass)
                elif(fishLevel >= 23):
                    fishAdv.tBaits(cod)
                elif(fishLevel >=16):
                    whichFish = random.randint(1, 100)
                    if(whichFish in range(67,99)):
                        fishAdv.tBaits(seaweed)
                    elif(whichFish in range(34,66)):
                        fishAdv.tBaits(mackerel)
                    elif(whichFish in range(1,33)):
                        fishAdv.tBaits(oyster)
                    elif(whichFish == 100):
                        fishAdv.tBaits(casket)
                        casketCash = random.randint(1, 10000)
                    else:
                        print("Error, please post on forums: #FER%i" % whichFish)
                        go=input("Press enter to continue")
                else:
                    print("You are not a high enough level! Minimum level: 16")
                    go=input("Press enter to continue")
                fishAdv.prompt()
            elif(fishAction == "4"):
                if(feathers >= 1):
                    feathers -= 1
                    if(fishLevel >= 38):
                        fishAdv.tBaits(rainbowfish)
                    elif(fishLevel >= 30):
                        fishAdv.tBaits(salmon)
                    elif(fishLevel >= 20):
                        fishAdv.tBaits(trout)
                    else:
                        print("You are not a high enough level! Minimum level: 20")
                        go=input("Press enter to continue")
                fishAdv.prompt()
            elif(fishAction == "5"):
                if(fishLevel >= 76):
                    whichFish = random.randint(1, 100)
                    if(whichFish in range(1,49)):
                        fishAdv.tBaits(shark)
                    elif(whichFish in range(50,100)):
                        fishAdv.tBaits(baronshark)
                elif(fishLevel >= 50):
                    fishAdv.tBaits(swordfish)
                elif(fishLevel >= 35):
                    fishAdv.tBaits(tuna)
                else:
                    print("You are not a high enough level! Minimum level: 35")
                    go=input("Press enter to continue")
                fishAdv.prompt()
            elif(fishAction == "6"):
                if(fishLevel >= 40):
                    fishAdv.tBaits(lobster)
                else:
                    print("You are not a high enough level! Minimum level: 40")
                    go=input("Press enter to continue")
                fishAdv.prompt()
            elif(fishAction == "7"):
                if(fishLevel >= 53):
                    fishAdv.tBaits(lavaeel)
                else:
                    print("You are not a high enough level! Minimum level: 53")
                    go=input("Press enter to continue")
                fishAdv.prompt()
            elif(fishAction == "8"):
                if(fishLevel >= 65):
                    fishAdv.tBaits(karambwan)
                else:
                    print("You are not a high enough level! Minimum level: 65")
                    go=input("Press enter to continue")
                fishAdv.prompt()
            elif(fishAction == "9"):
                if(fishLevel >= 90):
                    fishAdv.tBaits(rocktail)
                else:
                    print("You are not a high enough level! Minimum level: 90")
                    go=input("Press enter to continue")
                fishAdv.prompt()
            else:
                print("Invalid bait. Sorry!")
                time.sleep(1.5)
                fishAdv.prompt()
        else:
            print("Unknown issue, please report: FBR00.")
            time.sleep(1.5)
            fishAdv.prompt()


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
