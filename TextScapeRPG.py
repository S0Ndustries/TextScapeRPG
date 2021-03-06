# Base game file
# v3.0.0-beta

import sys
import time
import os
import random
import platform
import math
# Mining items
global itemClay; global itemRuneEssence; global itemCopperOre; global itemTinOre; global itemLimestone; global itemIronOre; global itemSilverOre; global itemPureEssence; global itemCoal; global itemSandstone; global itemGoldOre; global itemGranite; global itemMithrilOre; global itemAdamantOre; global itemLivingMinerals; global itemRuniteOre
itemClay = ["Clay", 111, 111, 111, 000, 0, 153, 5, 1]; itemRuneEssence = ["Rune Essence", 111, 111, 111, 000, 0, 63, 5, 1]; itemCopperOre = ["Copper", 111, 111, 111, 000, 0, 96, 17.5, 1]; itemTinOre = ["Tin", 111, 111, 111, 000, 0, 92, 17.5, 1]; itemLimestone = ["Limestone", 111, 111, 111, 000, 0, 320, 26.5, 10]; itemIronOre = ["Iron", 111, 111, 111, 000, 0, 204, 35, 15]; itemSilverOre = ["Silver", 111, 111, 111, 000, 0, 76, 40, 20]; itemPureEssence = ["Pure Essence", 111, 111, 111, 000, 0, 30, 5, 30]; itemCoal = ["Coal", 111, 111, 111, 000, 0, 365, 50, 30]; itemSandstone = ["Sandstone", 111, 111, 111, 000, 0, 16, 30, 35]; itemGoldOre = ["Gold", 111, 111, 111, 000, 0, 162, 65, 40]; itemGranite = ["Granite", 111, 111, 111, 000, 0, 230, 50, 45]; itemMithrilOre = ["Mithril", 111, 111, 111, 000, 0, 231, 80, 55]; itemAdamantOre = ["Adamant", 111, 111, 111, 000, 0, 1227, 95, 70]; itemLivingMinerals = ["Living minerals", 111, 111, 111, 000, 0, 241, 25, 73]; itemRuniteOre = ["Runite", 111, 111, 111, 000, 0, 10372, 125, 85]
global oreList
oreList = [itemClay, itemRuneEssence, itemCopperOre, itemTinOre, itemLimestone, itemIronOre, itemSilverOre, itemPureEssence, itemCoal, itemSandstone, itemGoldOre, itemGranite, itemMithrilOre, itemAdamantOre, itemLivingMinerals, itemRuniteOre]

# Game items
    # Raw fished items
global itemCasket; global itemOyster; global itemSeaweed; global itemFrogSpawn
global itemRAWMinnow; global itemRAWCrayfish; global itemRAWShrimp; global itemRAWSardine; global itemRAWKarambwanji; global itemRAWHerring; global itemRAWAnchovies; global itemRAWMackerel; global itemSeaweed; global itemRAWTrout; global itemRAWCod; global itemRAWPike; global itemRAWSlimyEel; global itemRAWSalmon; global itemFrogSpawn; global itemRAWTuna; global itemRAWCaveEel; global itemRAWRainbowFish; global itemRAWLobster; global itemRAWBass; global itemRAWSwordfish; global itemRAWLavaEel; global itemRAWMonkfish; global itemRAWKarambwan; global itemRAWShark; global itemRAWBaronShark; global itemRAWCavefish; global itemRAWRocktail
itemRAWMinnow = ["Raw Minnow", 111, 000, 111, 000, 0, 0]; itemRAWCrayfish = ["Raw Crayfish", 111, 000, 111, 000, 0, 74]; itemRAWShrimp = ["Raw Shrimp", 111, 000, 111, 000, 0, 18]; itemRAWSardine = ["Raw Sardine", 111, 000, 111, 000, 0, 24]; itemRAWKarambwanji = ["Raw Karambwanji", 111, 000, 111, 000, 0, 0]; itemRAWHerring = ["Raw Herring", 111, 000, 111, 000, 0, 35]; itemRAWAnchovies = ["Raw Anchovies", 111, 000, 111, 000, 0, 14]; itemRAWMackerel = ["Raw Mackerel", 111, 000, 111, 000, 0, 16]; itemSeaweed = ["Seaweed", 111, 000, 111, 000, 0, 32]; itemRAWTrout = ["Raw Trout", 111, 000, 111, 000, 0, 27]; itemRAWCod = ["Raw Cod", 111, 000, 111, 000, 0, 61]; itemRAWPike = ["Raw Pike", 111, 000, 111, 000, 0, 71]; itemRAWSlimyEel = ["Raw Slimy eel", 111, 000, 111, 000, 0, 851]; itemRAWSalmon = ["Raw Salmon", 111, 000, 111, 000, 0, 90]; itemFrogSpawn = ["Raw Frog spawn", 111, 000, 111, 000, 0, 0]; itemRAWTuna = ["Raw Tuna", 111, 000, 111, 000, 0, 109]; itemRAWCaveEel = ["Raw Cave eel", 111, 000, 111, 000, 0, 431]; itemRAWRainbowFish = ["Raw Rainbow fish", 111, 000, 111, 000, 0, 193]; itemRAWLobster = ["Raw Lobster", 111, 000, 111, 000, 0, 235]; itemRAWBass = ["Raw Bass", 111, 000, 111, 000, 0, 419]; itemRAWSwordfish = ["Raw Swordfish", 111, 000, 111, 000, 0, 510]; itemRAWLavaEel = ["Raw Lava eel", 111, 000, 111, 000, 0, 0]; itemRAWMonkfish = ["Raw Monkfish", 111, 000, 111, 000, 0, 555]; itemRAWKarambwan = ["Raw Karambwan", 111, 000, 111, 000, 0, 3356]; itemRAWShark = ["Raw Shark", 111, 000, 111, 000, 0, 816]; itemRAWBaronShark = ["Raw Baron shark", 111, 000, 111, 000, 0, 816]; itemRAWCavefish = ["Raw Cave fish", 111, 000, 111, 000, 0, 2036]; itemRAWRocktail = ["Raw Rocktail", 111, 000, 111, 000, 0, 2690]
global buyableItemList

global itemMinnow; global itemCrayfish; global itemShrimp; global itemSardine; global itemKarambwanji; global itemHerring; global itemAnchovies; global itemMackerel; global itemTrout; global itemCod; global itemPike; global itemSlimyEel; global itemSalmon; global itemTuna; global itemCaveEel; global itemRainbowFish; global itemLobster; global itemBass; global itemSwordfish; global itemLavaEel; global itemMonkfish; global itemKarambwan; global itemShark; global itemBaronShark; global itemCavefish; global itemRocktail
itemMinnow = ["Minnow", 000, 111, 111, 000, 0, 10, 150]; itemCrayfish = ["Crayfish", 000, 111, 111, 000, 0, 21, 200]; itemShrimp = ["Shrimp", 000, 111, 111, 000, 0, 14, 200]
itemSardine = ["Sardine", 000, 111, 111, 000, 0, 10, 108]; itemKarambwanji = ["Karambwanji", 000, 111, 111, 000, 0, 666, 200]; itemHerring = ["Herring", 000, 111, 111, 000, 0, 10, 200]; itemAnchovies = ["Anchovies", 000, 111, 111, 000, 0, 16, 200]; itemMackerel = ["Mackeral", 000, 111, 111, 000, 0, 5, 200]; itemTrout = ["Trout", 000, 111, 111, 000, 0, 37, 300]; itemCod = ["Cod", 000, 111, 111, 000, 0, 65, 450]; itemPike = ["Pike", 000, 111, 111, 000, 0, 42, 400]; itemSlimyEel = ["Slimy eel", 000, 111, 111, 000, 0, 233, 700]; itemSalmon = ["Salmon", 000, 111, 111, 000, 0, 101, 500]; itemTuna = ["Tuna", 000, 111, 111, 000, 0, 167, 750]; itemCaveEel = ["Cave eel", 000, 111, 111, 000, 0, 160, 950]; itemRainbowFish = ["Rainbow fish", 000, 111, 111, 000, 0, 176, 875]; itemLobster = ["Lobster", 000, 111, 111, 000, 0, 252, 1200]; itemBass = ["Bass", 000, 111, 111, 000, 0, 306, 1300]; itemSwordfish = ["Swordfish", 000, 111, 111, 000, 0, 379, 1400]; itemLavaEel = ["Lava eel", 000, 111, 111, 000, 0, 666, 1060]; itemMonkfish = ["Monkfish", 000, 111, 111, 000, 0, 441, 1600]; itemKarambwan = ["Karambwan", 000, 111, 111, 000, 0, 3347, 750]; itemShark = ["Shark", 000, 111, 111, 000, 0, 817, 2000]; itemBaronShark = ["Baron shark", 000, 111, 111, 000, 0, 1302, 2100]; itemCavefish = ["Cave fish", 000, 111, 111, 000, 0, 1827, 2000]; itemRocktail = ["Rocktail", 000, 111, 111, 000, 0, 2559, 2300]

itemCasket = ["Casket", 111, 111, 111, 000, 0]; itemOyster = ["Oyster", 111, 111, 111, 000, 0]; itemSeaweed = ["Seaweed", 111, 000, 111, 000, 0, 0, 0]; itemFrogSpawn = ["Frog spawn", 111, 000, 111, 000, 0, 0, 0];

global doneFishList
global rawFishList
doneFishList = [itemMinnow, itemCrayfish, itemShrimp, itemSardine, itemKarambwanji, itemHerring, itemAnchovies, itemMackerel, itemSeaweed, itemTrout, itemCod, itemPike, itemSlimyEel, itemSalmon, itemFrogSpawn, itemTuna, itemCaveEel, itemRainbowFish, itemLobster, itemBass, itemSwordfish, itemLavaEel, itemMonkfish, itemKarambwan, itemShark, itemBaronShark, itemCavefish, itemRocktail]
rawFishList = [itemRAWMinnow, itemRAWCrayfish, itemRAWShrimp, itemRAWSardine, itemRAWKarambwanji, itemRAWHerring, itemRAWAnchovies, itemRAWMackerel, itemSeaweed, itemRAWTrout, itemRAWCod, itemRAWPike, itemRAWSlimyEel, itemRAWSalmon, itemFrogSpawn, itemRAWTuna, itemRAWCaveEel, itemRAWRainbowFish, itemRAWLobster, itemRAWBass, itemRAWSwordfish, itemRAWLavaEel, itemRAWMonkfish, itemRAWKarambwan, itemRAWShark, itemRAWBaronShark, itemRAWCavefish, itemRAWRocktail]

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
global feathers
# Global monster stats
global monsterGoblin
global monsterName
global monsterHP
global monsterMaxHit
global monsterXP
global monsterCoins
global monsterItemsDropped

# EXP stats
global luckEXP; global attackEXP; global strengthEXP; global defenceEXP; global rangedEXP; global magicEXP; global healthEXP; global buildEXP; global mineEXP; global fishEXP; global cookingEXP; global woodcuttingEXP; global agilityEXP; global herbloreEXP; global farmingEXP; global huntingEXP; global summoningEXP
luckEXP = 0; attackEXP = 0; strengthEXP = 0; defenceEXP = 0; rangedEXP = 0; magicEXP = 0; healthEXP = 0; buildEXP = 0; mineEXP = 0; fishEXP = 0; cookingEXP = 0; woodcuttingEXP = 0; agilityEXP = 0; herbloreEXP = 0; farmingEXP = 0; huntingEXP = 0; summoningEXP = 0
global skillEXPList
skillEXPList = [luckEXP, attackEXP, strengthEXP, defenceEXP, rangedEXP, magicEXP, healthEXP, buildEXP, mineEXP, fishEXP, cookingEXP, woodcuttingEXP, agilityEXP, herbloreEXP, farmingEXP, huntingEXP, summoningEXP]
# Player Skills
global luckLevel; global attackLevel; global strengthLevel; global defenceLevel; global rangedLevel; global magicLevel; global healthLevel; global buildLevel; global mineLevel; global fishLevel; global cookingLevel; global woodcuttingLevel; global agilityLevel; global herbloreLevel; global farmingLevel; global huntingLevel; global summoningLevel
luckLevel = 1; attackLevel = 1; strengthLevel = 1; defenceLevel = 1; rangedLevel = 1; magicLevel = 1; healthLevel = 1; buildLevel = 1; mineLevel = 1; fishLevel = 1; cookingLevel = 1; woodcuttingLevel = 1; agilityLevel = 1; herbloreLevel = 1; farmingLevel = 1; huntingLevel = 1; summoningLevel = 1
    # Skill list
global skillList
skillList = [luckLevel, attackLevel, strengthLevel, defenceLevel, rangedLevel, magicLevel, healthLevel, buildLevel, mineLevel, fishLevel, cookingLevel, woodcuttingLevel, agilityLevel, herbloreLevel, farmingLevel, huntingLevel, summoningLevel]

global itemNullFiller; itemNullFiller = ["Null Filler Item", 111, 111, 111, 000, 1337]

global itemUncutHydrix; itemUncutHydrix = ["Uncut Hydrix", 111, 111, 111, 000, 0, 13356199]
global itemUncutOnyx; itemUncutOnyx = ["Uncut Onyx", 111, 111, 111, 000, 0, 1126129]
global itemUncutDragonstone; itemUncutDragonstone = ["Uncut Dragonstone", 111, 111, 111, 000, 0, 12840]
global itemUncutDiamond; itemUncutDiamond = ["Uncut Diamond", 111, 111, 111, 000, 0, 3971]
global itemUncutRuby; itemUncutRuby = ["Uncut Ruby", 111, 111, 111, 000, 0, 2239]
global itemUncutEmerald; itemUncutEmerald = ["Uncut Emerald", 111, 111, 111, 000, 0, 1462]
global itemUncutSapphire; itemUncutSapphire = ["Uncut Sapphire", 111, 111, 111, 000, 0, 690]
global itemUncutRedTopaz; itemUncutRedTopaz = ["Uncut Red Topaz", 111, 111, 111, 000, 0, 1059]
global itemUncutJade; itemUncutJade = ["Uncut Jade", 111, 111, 111, 000, 0, 398]
global itemUncutOpal;itemUncutOpal = ["Uncut Opal", 111, 111, 111, 000, 0, 509]
uncutGemList = [itemUncutHydrix, itemUncutOnyx, itemUncutDragonstone, itemUncutDiamond, itemUncutRuby, itemUncutEmerald, itemUncutSapphire, itemUncutRedTopaz, itemUncutJade, itemUncutOpal]

global itemHydrix; itemHydrix = ["Hydrix", 111, 111, 111, 000, 0, 19538637, 197.5, 79]
global itemOnyx; itemOnyx = ["Onyx", 111, 111, 111, 000, 0, 1135644, 167.5, 67]
global itemDragonstone; itemDragonstone = ["Dragonstone", 111, 111, 111, 000, 0, 9468, 137.5, 55]
global itemDiamond; itemDiamond = ["Diamond", 111, 111, 111, 000, 0, 1825, 107.5, 43]
global itemRuby; itemRuby = ["Ruby", 111, 111, 111, 000, 0, 911, 85, 34]
global itemEmerald; itemEmerald = ["Emerald", 111, 111, 111, 000, 0, 673, 67.5, 27]
global itemSapphire; itemSapphire = ["Sapphire", 111, 111, 111, 000, 0, 191, 50, 20]
global itemRedTopaz; itemRedTopaz = ["Red Topaz", 111, 111, 111, 000, 0, 659, 25, 16]
global itemJade; itemJade = ["Jade", 111, 111, 111, 000, 0, 290, 20, 13]
global itemOpal; itemOpal = ["Opal", 111, 111, 111, 000, 0, 182, 15, 1]
gemList = [itemHydrix, itemOnyx, itemDragonstone, itemDiamond, itemRuby, itemEmerald, itemSapphire, itemRedTopaz, itemJade, itemOpal]

global itemBronzeBar; itemBronzeBar = ["Bronze bar", 111, 111, 111, 000, 0, 283, 6.2, 1, itemCopperOre, itemTinOre, 1]
global itemIronBar; itemIronBar = ["Iron bar", 111, 111, 111, 000, 0, 347, 12.5, 15, itemIronOre, itemNullFiller, 0]
global itemSilverBar; itemSilverBar = ["Silver bar", 111, 111, 111, 000, 0, 138, 13.7, 20, itemSilverOre, itemNullFiller, 0]
global itemSteelBar;itemSteelBar = ["Steel bar", 111, 111, 111, 000, 0, 809, 17.5, 30, itemIronOre, itemCoal, 2]
global itemGoldBar; itemGoldBar = ["Gold bar", 111, 111, 111, 000, 0, 90, 22.5, 40, itemGoldOre, itemNullFiller, 0]
global itemMithrilBar; itemMithrilBar = ["Mithril bar", 111, 111, 111, 000, 0, 1358, 30, 50, itemMithrilOre, itemCoal, 4]
global itemAdamantBar; itemAdamantBar = ["Adamant bar", 111, 111, 111, 000, 0, 2559, 37.5, 70, itemAdamantOre, itemCoal, 6]
global itemRuneBar; itemRuneBar = ["Rune bar", 111, 111, 111, 000, 0, 14214, 50, 85, itemRuniteOre, itemCoal, 8]
barList = [itemBronzeBar, itemIronBar, itemSilverBar, itemSteelBar, itemGoldBar, itemMithrilBar, itemAdamantBar, itemRuneBar]

global loadTime

buyableItemList = doneFishList + rawFishList + gemList + uncutGemList + oreList + barList

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

def help_func():
    print("Fight: Begins a fight")
    print("Fish: Try to fish for food")
    print("Cook: Cook the fish, or other food")
    print("Stats: Displays the current player stats")
    print("Heal: Heals the player")
    print("Help: Gives general information about commands")
    print("Exit: Closes the game")
    go=input("\nPress enter to continue.")
    game.actionPrompt()

class randomActions:
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
            game.actionPrompt()
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
            game.actionPrompt()
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
            game.actionPrompt()
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
            game.actionPrompt()
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
            game.actionPrompt()
    def fart():
        print("You empty your bowels of the fumes plaguing them.")
        time.sleep(0.7)
        print("Everything fades away...")
        time.sleep(1)
        print("You wake up in Hospital! You have lost 5HP")
        time.sleep(1.5)
        game.actionPrompt()

class game:
    def runGame():
        system.clear()
        try:
            if((str(sys.argv[1] == "show"))):
                game.loadTitle()
        except:
            pass
        game.initializeGame()
        game.nameSelect()
        game.actionPrompt()
    def actionPrompt():
        actionList = ["fight", "fish", "cook", "heal", "help", "fuck", "fart", "stats", "exit", "skills", "shop", "mine", "build"]
        system.clear()
        print("What would you like to do?")
        print("Enter 'help' for more options.")
        action=input("Action: ").lower()
        if (action in actionList):
            if (action.lower() == actionList[0]):
                fight.setup()
            elif(action.lower() == actionList[1]):
                fishAdv.prompt()
            elif(action.lower() == actionList[2]):
                # Jesse, we need to -
                cookAdv.prompt()
            elif(action.lower() == actionList[3]):
                healAdv.prompt(0)
            elif(action.lower() == actionList[4]):
                help_func()
            elif(action.lower() == actionList[5]):
                randomActions.fuck()
            elif(action.lower() == actionList[6]):
                randomActions.fart()
            elif(action.lower() == actionList[7]):
                stats.init()
            elif(action.lower() == actionList[8]):
                system.clear()
                exit()
            elif(action.lower() == actionList[9]):
                game.skills()
            elif(action.lower() == actionList[10]):
                shop.prompt()
            elif(action.lower() == actionList[11]):
                mine.prompt()
            elif(action.lower() == actionList[12]):
                build.prompt()
            else:
                print("\nThis doesn't work.. Notify Senpai pl0x.")
                go=input("Press enter to continue.")
                game.actionPrompt()
        else:
            game.otherActions(action)
    def initializeGame():
        # Sets all fish item traits.
        global loadTime
        loadTime = 0.4 / ((fishLevel * (agilityLevel * 0.1) * (strengthLevel * 0.1) * 0.005) + 0.995)
        fishAdv.fishes()
        fishAdv.firstStats()
        # Anything else to be initialized can go here
    def loadTitle():
        system.clear()
        s = "\n                                   Welcome to                                   \n\nd888888P                   dP   .d88888b                                      \n   88                      88   88.    \"'                                     \n   88  .d8888b. dP.  .dP d8888P `Y88888b. .d8888b. .d8888b. 88d888b. .d8888b. \n   88  88ooood8  `8bd8'    88         `8b 88'  `\"\" 88'  `88 88'  `88 88ooood8 \n   88  88.  ...  .d88b.    88   d8'   .8P 88.  ... 88.  .88 88.  .88 88.  ... \n   dP  `88888P' dP'  `dP   dP   `Y88888P' `88888P' `88888P8 88Y888P' `88888P' \n                                                            88                \n                                                            dP        <RPG>   \n"
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
        bonusNames = ["Son", "Evan", "betaTest"]
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
    def skills():
        global attackLevel; global strengthLevel; global defenceLevel; global rangedLevel; global magicLevel; global healthLevel; global buildLevel; global mineLevel; global fishLevel; global cookingLevel; global woodcuttingLevel; global agilityLevel; global herbloreLevel; global farmingLevel; global huntingLevel; global summoningLevel
        global attackEXP; global strengthEXP; global defenceEXP; global rangedEXP; global magicEXP; global healthEXP; global buildEXP; global mineEXP; global fishEXP; global cookingEXP; global woodcuttingEXP; global agilityEXP; global herbloreEXP; global farmingEXP; global huntingEXP; global summoningEXP
        print("Skills: \n")
        print("attack      | Level: %i  | EXP: %i" % (attackLevel, attackEXP))
        print("strength    | Level: %i  | EXP: %i" % (strengthLevel, strengthEXP))
        print("defence     | Level: %i  | EXP: %i" % (defenceLevel, defenceEXP))
        print("ranged      | Level: %i  | EXP: %i" % (rangedLevel, rangedEXP))
        print("magic       | Level: %i  | EXP: %i" % (magicLevel, magicEXP))
        print("health      | Level: %i  | EXP: %i" % (healthLevel, healthEXP))
        print("build       | Level: %i  | EXP: %i" % (buildLevel, buildEXP))
        print("mine        | Level: %i  | EXP: %i" % (mineLevel, mineEXP))
        print("fish        | Level: %i  | EXP: %i" % (fishLevel, fishEXP))
        print("cooking     | Level: %i  | EXP: %i" % (cookingLevel, cookingEXP))
        print("woodcutting | Level: %i  | EXP: %i" % (woodcuttingLevel, woodcuttingEXP))
        print("agility     | Level: %i  | EXP: %i" % (agilityLevel, agilityEXP))
        print("herblore    | Level: %i  | EXP: %i" % (herbloreLevel, herbloreEXP))
        print("farming     | Level: %i  | EXP: %i" % (farmingLevel, farmingEXP))
        print("hunting     | Level: %i  | EXP: %i" % (huntingLevel, huntingEXP))
        print("summoning   | Level: %i  | EXP: %i" % (summoningLevel, summoningEXP))
        go=input("Press enter to continue.")
        game.actionPrompt()
    def otherActions(action):
        a = action.lower()
        if(a == "walk"):
            print("\nWalk? Walk where? If you go too far you may fall into cyberspace!")
            go=input("\nPress enter to continue.")
            game.actionPrompt()
        elif(a == "jump"):
            print("\nNow why would you want to do that? You're not on a trampoline.")
            go=input("\nPress enter to continue.")
            game.actionPrompt()
        elif(a == "poop"):
            print("\nYou drop a huge log on the floor..")
            time.sleep(0.5)
            print("Everyone stares at you.")
            time.sleep(0.3)
            print("You run away in shame.")
            time.sleep(0.3)
            go=input("\nPress enter to awkwardly continue.")
            game.actionPrompt()
        elif(a == "kill"):
            system.clear()
            print("You remove the blade from your razor..")
            go=input("Press enter to continue.")
            system.clear()
            print("An old man looking in the window whispers:\"Remember kids, down the street, not across the road!\"")
            go=input("Press enter to continue.")
            system.clear()
            print("You scream in shock and drop the razor blade.")
            go=input("Press enter to continue.")
            system.clear()
            print("You run out of the room, but step on the razor blade. Retard.")
            go=input("Press enter to continue.")
            system.clear()
            print("You *bleed out* from the cut on your foot.")
            go=input("Press enter to continue.")
            system.clear()
            print("You wake up in the old man's basement wearing a unicorn outfit.")
            go=input("Press enter to continue.")
            system.clear()
            print("You black out.")
            go=input("Press enter to continue.")
            system.clear()
            print("You open your eyes & see Senpai standing in front of you. You have been saved!")
            time.sleep(0.7)
            go=input("Press enter to continue.")
            game.actionPrompt()
        elif(a == "run"):
            print("\nRun? Run where? There's nowhere to hide...")
            time.sleep(1)
            go=input("Press enter to continue.")
            game.actionPrompt()
        elif(a == "die"):
            print("\nYou have died. Game over.")
            go=input("Press enter to continue.")
        elif(a=="travel"):
            print("A magical force prevents you from moving.")
            time.sleep(0.1)
            go=input("Press enter to continue.")
            game.actionPrompt()
        else:
            print("\nYou can't %s! what are you, stupid? Type help, because you obviously need it n00b!" % action)
            go=input("\nPress enter to continue.")
            game.actionPrompt()
class stats:
    def init():
        system.clear()
        stats.general()
        stats.fish()
        go=input("\nPress enter to continue.")
        game.actionPrompt()
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
        print("Fishing Level: %i" % fishLevel)

class fight:
    def run():
        print("You have run away!")
        time.sleep(0.1)
        game.actionPrompt()
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
                if (action.lower() == fightActionList[0]):
                    fight.message()
                elif(action.lower() == fightActionList[1]):
                    healAdv.prompt(1)
                elif(action.lower() == fightActionList[2]):
                    fight.run()
                else:
                    print("Something's up...")
        else:
            if(playerHP < 0):
                print("You Lost")
                # Loss code here
                game.actionPrompt()
            else:
                playerBal += monsterCoins * 10
                time.sleep(0.5)
                print("\nYou earned %i coins! Your balance is now: %i" % (monsterCoins * 10, playerBal))
                time.sleep(2.5)
                game.actionPrompt()

class cookAdv:
    global itemRAWMinnow; global itemRAWCrayfish; global itemRAWShrimp; global itemRAWSardine; global itemRAWKarambwanji; global itemRAWHerring; global itemRAWAnchovies; global itemRAWMackerel; global itemSeaweed; global itemRAWTrout; global itemRAWCod; global itemRAWPike; global itemRAWSlimyEel; global itemRAWSalmon; global itemFrogSpawn; global itemRAWTuna; global itemRAWCaveEel; global itemRAWRainbowFish; global itemRAWLobster; global itemRAWBass; global itemRAWSwordfish; global itemRAWLavaEel; global itemRAWMonkfish; global itemRAWKarambwan; global itemRAWShark; global itemRAWBaronShark; global itemRAWCavefish; global itemRAWRocktail
    global rawFishList
    # Cooked items
    global itemMinnow; global itemCrayfish; global itemShrimp; global itemSardine; global itemKarambwanji; global itemHerring; global itemAnchovies; global itemMackerel; global itemTrout; global itemCod; global itemPike; global itemSlimyEel; global itemSalmon; global itemFrogSpawn; global itemTuna; global itemCaveEel; global itemRainbowFish; global itemLobster; global itemBass; global itemSwordfish; global itemLavaEel; global itemMonkfish; global itemKarambwan; global itemShark; global itemBaronShark; global itemCavefish; global itemRocktail
    global doneFishList
    global cookLevel
    global cookEXP

    def prompt():
        system.clear()
        cookActionList = ["food", "stats", "exit", "help"]
        global rawFishList
        global doneFishList
        print("Enter an action, type 'help' for help, or 'exit' to exit!")
        cookAction=input("Cook action: ")
        if(cookAction in cookActionList):
            if(cookAction == "food"):
                cookAdv.food()
            elif(cookAction == "stats"):
                cookAdv.stats()
            elif(cookAction == "exit"):
                game.actionPrompt()
            elif(cookAction == "help"):
                cookAdv.help()
        else:
            cookAdv.cook(cookAction)

    def cook(cookAction):
        runCook = 1
        incX = 0
        while(runCook == 1):
            fishCook = rawFishList[incX]
            fishDone = doneFishList[incX]
            if(cookAction.lower() == fishDone[0].lower()):
                if(fishCook[5] >= 1):
                    print("Cooked: %s!" % fishCook[0])
                    fishCook[5] -= 1
                    fishDone[5] += 1
                    go=input("Press enter to continue.")
                    runCook = 0
                else:
                    print("\nYou don't have any %s to cook!" % fishCook[0])
                    go=input("Press enter to continue.")
                    runCook = 0
            else:
                if(incX < 25):
                    incX += 1
                else:
                    print("\nInvalid command, sorry!")
                    go=input("Press enter to continue.")
                    cookAdv.prompt()
        cookAdv.prompt()
    def loadBar():
        global cookedLevel
        global loadCTime
        loadCTime = 0.2 / ((cookLevel * 0.1 * 0.005) + 0.995)
        s = "[==========]"
        for c in s:
            sys.stdout.write('%s' % c )
            sys.stdout.flush()
            time.sleep(loadCTime)

    def food():
        print("\nRaw food:")
        y = 0
        x = 0
        lol = 0
        while(x <= 27):
            rawFood = rawFishList[x]
            if(rawFood[5] > 0):
                print("    %s: %i" % (rawFood[0], rawFood[5]))
                lol += 1
            x += 1
        else:
            y = 0
            if(lol == 0):
                print("None!")
        y = 0
        x = 0
        lol = 0
        print("\nCooked food:")
        while(x < 26):
            doneFood = doneFishList[x]
            if(doneFood[5] > 0):
                print("    %s: %i" % (doneFood[0], doneFood[5]))
                lol += 1
            x += 1
        else:
            if(lol == 0):
                print("None!")
            y = 0
        go=input("\nPress enter to continue.")
        cookAdv.prompt()
    def help():
        print("\nCommands: ")
        print("    food = Displays your raw & cooked foods")
        print("    stats = Displays cooking statistics")
        print("    exit = Exits the program")
        print("    help = Displays this screen")
        print("\nOr enter a fish name to cook it.")
        go=input("Press enter to continue.")
        cookAdv.prompt()
    def stats():
        global cookEXP
        global cookLevel
        global exp
        global level
        global loadCTime
        game.myEXP(cookEXP)
        cookLevel = level
        print("\nYour cooking XP amount is: %i" % cookEXP)
        print("Your cooking level is now: %i" % cookLevel)
        print("You take: %s seconds to cook food!" % (loadCTime * 12))
        rexturn = input("\nPress enter to return")
        cookAdv.prompt()
    def firstStats():
        global cookEXP
        global cookLevel
        global exp
        global level
        game.myEXP(cookEXP)
        cookLevel = level

class fishAdv:
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

    def fishInv():
        rawArray = (itemRAWMinnow, itemRAWCrayfish, itemRAWShrimp, itemRAWSardine, itemRAWKarambwanji, itemRAWHerring, itemRAWAnchovies, itemRAWMackerel, itemSeaweed, itemRAWTrout, itemRAWCod, itemRAWPike, itemRAWSlimyEel, itemRAWSalmon, itemFrogSpawn, itemRAWTuna, itemRAWCaveEel, itemRAWRainbowFish, itemRAWLobster, itemRAWBass, itemRAWSwordfish, itemRAWLavaEel, itemRAWMonkfish, itemRAWKarambwan, itemRAWShark, itemRAWBaronShark, itemRAWCavefish, itemRAWRocktail)
        print("\nYour fish\n")
        x = 0
        lol = 0
        while(x < 28):
            theFish = rawArray[x]
            if(theFish[5] > 0):
                print("%s: %s" % (theFish[0], theFish[5]))
                lol += 1
            x += 1
        if(lol == 0):
            print("None!")
        go=input("\nPress enter to continue.")
        fishAdv.prompt()
    def stats():
        global fishEXP
        global fishLevel
        global exp
        global level
        global loadTime
        game.myEXP(fishEXP)
        fishLevel = level
        print("\nYour fishing XP amount is: %i" % fishEXP)
        print("Your fishing level is now: %i" % fishLevel)
        print("You take: %s seconds to catch a fish!" % (loadTime * 12))
        rexturn = input("\nPress enter to return")
        fishAdv.prompt()
    def firstStats():
        global fishEXP
        global fishLevel
        global exp
        global level
        game.myEXP(fishEXP)
        fishLevel = level

    def loadBar():
        global fishLevel
        global loadTime
        global agilityLevel
        global strengthLevel
        global loadTimeX
        loadTimeX = loadTime * 7
        loadTime = 0.2 / ((fishLevel * (strengthLevel * 0.1) * 0.005) + 0.995)
        s = "[==========]"
        for c in s:
            sys.stdout.write('%s' % c )
            sys.stdout.flush()
            time.sleep(loadTime)

    def tBaits(fType):
        global fishEXP
        global strengthEXP
        global fishLevel
        fishAdv.firstStats()
        if(fType[2] == 0):
            print("\nYou cast your line into the water.")
            fishAdv.loadBar()
            print("\nYour line is hooked!")
        elif(fType[2] == 1):
            print("\nYou thrust your cage into the water.")
            fishAdv.loadBar()
            print("\nYou pull it back out!")
        elif(fType[2] == 2):
            print("\nYou dip your small net into the water.")
            fishAdv.loadBar()
            print("\nYou pull it back out!")
        elif(fType[2] == 3):
            print("\nYou cast your large net into the water.")
            fishAdv.loadBar()
            print("\nYou pull it back out!")
        elif(fType[2] == 4):
            print("\nYou cast your line into the water.")
            fishAdv.loadBar()
            print("\nYou reel it in!")
        elif(fType[2] == 5):
            print("\nYou stab your harpoon into the water.")
            fishAdv.loadBar()
            print("\nYou pull it back out!")
        elif(fType[2] == 6):
            print("\nYou place your lobster pot into the water.")
            fishAdv.loadBar()
            print("\nYou pull it back out!")
        elif(fType[2] == 7):
            print("\nYou cast your line into the water.")
            fishAdv.loadBar()
            print("\nYou reel it in!")
        elif(fType[2] == 6):
            print("\nYou mysteriously use your karambwanvessel.")
            fishAdv.loadBar()
            print("\nYou feel a bite!")
        elif(fType[2] == 7):
            print("\nYou mysteriously use your living minerals.")
            fishAdv.loadBar()
            print("\nYou feel a bite!")
        print("You have caught: %s! & gained + %0.1f XP!" % (fType[0], fType[3]))
        fishEXP += (fType[3] * (1.0 + ((fishLevel - 1) * 0.01)))
        strengthEXP += (fType[3] / 10)
        go=input("Press enter to continue.")
    def betaTest():
        global strengthLevel
        global fishEXP
        global agilityLevel
        levelUp=input("Enter beta command:")
        if(levelUp == "str"):
            strengthLevel += 1
            print(strengthLevel)
            time.sleep(0.5)
            fishAdv.betaTest()
        elif(levelUp == "agil"):
            agilityLevel += 1
            print(agilityLevel)
            time.sleep(0.5)
            fishAdv.betaTest()
        elif(levelUp == "fsh"):
            fishEXP += 500
            fishAdv.firstStats()
            print(fishLevel)
            time.sleep(0.5)
            fishAdv.betaTest()
        elif(levelUp == "exit"):
            fishAdv.prompt()
        else:
            print("Please leave this command prompt if you are not a beta tester")
            go=input("Press enter to leave")
            fishAdv.prompt()
    def prompt():
        system.clear()
        global fishAction
        fishCMDs = ["0","1","2","3","4","5","6","7","8","9", "list", "guide", "exit", "stats", "fish", "fish1", "betaTest"]
        print("Enter an action, type 'guide' for help, or 'exit' to exit!")
        fishAction=input("Fish action: ")
        if (fishAction in fishCMDs):
            if (fishAction == "list"):
                fishAdv.list()
            elif(fishAction == "guide"):
                fishAdv.guide()
            elif(fishAction == "exit"):
                game.actionPrompt()
            elif(fishAction == "stats"):
                fishAdv.stats()
            elif(fishAction == "fish"):
                fishAdv.fishInv()
            elif(fishAction == "betaTest"):
                fishAdv.betaTest()
            elif(fishAction == "fish1"):
                fishAction1=input("Enter bait type: ")
                fishAdv.fish(fishAction1)
            else:
                fishAdv.fish2(fishAction)
        else:
            print("That's not a command!")
            time.sleep(1.5)
            fishAdv.prompt()

    def guide():
        print("\n Fishing bait type command:\n")
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
        print("   Level(s): 90\n")
        print("\nOther fishing commands:")
        print("\n   list = Displays a list of all fish + level & bait needed.") #fishAdv.list()
        print("\n   exit = Exits back to the main action prompt.") # actionPrompt()
        print("\n   stats = Displays fishing stats.") # fishAdv.stats()
        print("\n   fish = Displays amount of all fish in your bag.") # fishAdv.fishInv()
        done = input("\nPress enter to continue")
        fishAdv.prompt()

    def list():
        print("\nFish list\n")
        print("Minnow       - Level: 1  | XP: 10  | Bait: 0")
        print("Crayfish     - Level: 1  | XP: 10  | Bait: 1")
        print("Shrimps      - Level: 1  | XP: 10  | Bait: 2")
        print("Sardine      - Level: 5  | XP: 20  | Bait: 0")
        print("Karambwanji  - Level: 5  | XP: 5   | Bait: 2")
        print("Herring      - Level: 10 | XP: 30  | Bait: 0")
        print("Anchovies    - Level: 15 | XP: 40  | Bait: 1")
        print("Casket       - Level: 16 | XP: 10  | Bait: 3")
        print("Mackerel     - Level: 16 | XP: 20  | Bait: 3")
        print("Oyster       - Level: 16 | XP: 10  | Bait: 3")
        print("Seaweed      - Level: 16 | XP: 1   | Bait: 3")
        print("Trout        - Level: 20 | XP: 50  | Bait: 4")
        print("Cod          - Level: 23 | XP: 45  | Bait: 3")
        print("Pike         - Level: 25 | XP: 60  | Bait: 0")
        print("Slimy eel    - Level: 28 | XP: 65  | Bait: 0")
        print("Salmon       - Level: 30 | XP: 70  | Bait: 4")
        print("Frog spawn   - Level: 33 | XP: 75  | Bait: 2")
        print("Tuna         - Level: 35 | XP: 80  | Bait: 5")
        print("Cave eel     - Level: 38 | XP: 80  | Bait: 0")
        print("Rainbow fish - Level: 38 | XP: 80  | Bait: 4")
        print("Lobster      - Level: 40 | XP: 90  | Bait: 6")
        print("Bass         - Level: 46 | XP: 100 | Bait: 3")
        print("Swordfish    - Level: 50 | XP: 100 | Bait: 5")
        print("Lava eel     - Level: 53 | XP: 60  | Bait: 7")
        print("Monkfish     - Level: 62 | XP: 120 | Bait: 2")
        print("Karambwan    - Level: 65 | XP: 105 | Bait: 8")
        print("Shark        - Level: 76 | XP: 110 | Bait: 5")
        print("Baron shark  - Level: 76 | XP: 110 | Bait: 5")
        print("Cavefish     - Level: 85 | XP: 300 | Bait: 0")
        print("Rocktail     - Level: 90 | XP: 380 | Bait: 9")

        go=input("\nPress enter to continue")
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
                        itemRAWCavefish[5] += 1
                    elif(fishLevel >= 38):
                        fishAdv.tBaits(caveeel)
                        itemRAWCaveEel[5] += 1
                    elif(fishLevel >= 28):
                        fishAdv.tBaits(slimyeel)
                        itemRAWSlimyEel[5] += 1
                    elif(fishLevel >= 25):
                        fishAdv.tBaits(pike)
                        itemRAWPike[5] += 1
                    elif(fishLevel >= 10):
                        fishAdv.tBaits(herring)
                        itemRAWHerring[5] += 1
                    elif(fishLevel >= 5):
                        fishAdv.tBaits(sardine)
                        itemRAWSardine[5] += 1
                    else:
                        fishAdv.tBaits(minnow)
                        itemRAWMinnow[5] += 1
                else:
                    print("Not enough bait!")
                    time.sleep(1)
                fishAdv.prompt()
            elif(fishAction == "1"):
                fishAdv.tBaits(crayfish)
                itemRAWCrayfish[5] += 1
                fishAdv.prompt()
            elif(fishAction == "2"):
                if(fishLevel >= 62):
                    fishAdv.tBaits(monkfish)
                    itemRAWMonkfish[5] += 1
                elif(fishLevel >= 33):
                    fishAdv.tBaits(frogspawn)
                    itemFrogSpawn[5] += 1
                elif(fishLevel >= 15):
                    fishAdv.tBaits(anchovies)
                    itemRAWAnchovies[5] += 1
                elif(fishLevel >= 5):
                    fishAdv.tBaits(karambwanji)
                    itemRAWKarambwanji[5] += 1
                else:
                    fishAdv.tBaits(shrimp)
                    itemRAWShrimp[5] += 1
                fishAdv.prompt()
            elif(fishAction == "3"):
                if(fishLevel >= 46):
                    fishAdv.tBaits(bass)
                    itemRAWBass[5] += 1
                elif(fishLevel >= 23):
                    fishAdv.tBaits(cod)
                    itemRAWCod[5] += 1
                elif(fishLevel >=16):
                    whichFish = random.randint(1, 100)
                    if(whichFish in range(67,99)):
                        fishAdv.tBaits(seaweed)
                        itemSeaweed[5] += 1
                    elif(whichFish in range(34,66)):
                        fishAdv.tBaits(mackerel)
                        itemRAWMackerel[5] += 1
                    elif(whichFish in range(1,33)):
                        fishAdv.tBaits(oyster)
                        itemOyster[5] += 1
                    elif(whichFish == 100):
                        fishAdv.tBaits(casket)
                        casketCash = random.randint(1, 10000)
                        print("You have found %i coins!" % casketCash)
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
                        itemRAWRainbowFish[5] += 1
                    elif(fishLevel >= 30):
                        fishAdv.tBaits(salmon)
                        itemRAWSalmon[5] += 1
                    elif(fishLevel >= 20):
                        fishAdv.tBaits(trout)
                        itemRAWTrout[5] += 1
                    else:
                        print("You are not a high enough level! Minimum level: 20")
                        go=input("Press enter to continue")
                fishAdv.prompt()
            elif(fishAction == "5"):
                if(fishLevel >= 76):
                    whichFish = random.randint(1, 100)
                    if(whichFish in range(1,49)):
                        fishAdv.tBaits(shark)
                        itemRAWShark[5] += 1
                    elif(whichFish in range(50,100)):
                        fishAdv.tBaits(baronshark)
                        itemRAWBaronShark[5] += 1
                elif(fishLevel >= 50):
                    fishAdv.tBaits(swordfish)
                    itemRAWSwordfish[5] += 1
                elif(fishLevel >= 35):
                    fishAdv.tBaits(tuna)
                    itemRAWTuna[5] += 1
                else:
                    print("You are not a high enough level! Minimum level: 35")
                    go=input("Press enter to continue")
                fishAdv.prompt()
            elif(fishAction == "6"):
                if(fishLevel >= 40):
                    fishAdv.tBaits(lobster)
                    itemRAWLobster[5] += 1
                else:
                    print("You are not a high enough level! Minimum level: 40")
                    go=input("Press enter to continue")
                fishAdv.prompt()
            elif(fishAction == "7"):
                if(fishLevel >= 53):
                    fishAdv.tBaits(lavaeel)
                    itemRAWLavaEel[5] += 1
                else:
                    print("You are not a high enough level! Minimum level: 53")
                    go=input("Press enter to continue")
                fishAdv.prompt()
            elif(fishAction == "8"):
                if(fishLevel >= 65):
                    fishAdv.tBaits(karambwan)
                    itemRAWKarambwan[5] += 1
                else:
                    print("You are not a high enough level! Minimum level: 65")
                    go=input("Press enter to continue")
                fishAdv.prompt()
            elif(fishAction == "9"):
                if(fishLevel >= 90):
                    fishAdv.tBaits(rocktail)
                    itemRAWRocktail[5] += 1
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
    def fish2(baitSel):
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
        global rawFishList
        fishAction = baitSel
        fishList = [minnow, crayfish, shrimp, sardine, karambwanji, herring, anchovies, casket, mackerel, oyster, seaweed, trout, cod, pike, slimyeel, salmon, frogspawn, tuna, caveeel, rainbowfish, lobster, bass, swordfish, lavaeel, monkfish, karambwan, shark, baronshark, cavefish, rocktail]
        baitType = ["bait","crayfishcage","smallnet","bignet","flyfishingrod","harpoon","lobsterpot","oilyfishingrod","karambwanvessel","livingminerals"]
        baitTypeNum = ["0","1","2","3","4","5","6","7","8","9"]
        fishSel = 29
        runLoop = 0
        while(runLoop == 0 and fishSel >= 0):
            fishType = fishList[fishSel]
            if(fishType[2] == int(fishAction)):
                if(fishType[1] <= fishLevel):
                    fishAdv.tBaits(fishType)
                    addFish = rawFishList[fishSel]
                    addFish[5] += 1
                    runLoop = 1
                    fishAdv.prompt()
                else:
                    if(fishSel >= 0):
                        fishSel -= 1
            else:
                if(fishSel >= 0):
                    fishSel -= 1
                else:
                    print("Error")
                    time.sleep(1.5)
                    fishAdv.prompt()
        else:
            print("\nYou aren't a high enough level!")
            print("Try 'guide' to find level required")
            time.sleep(1)
            fishAdv.prompt()

class healAdv:
    global itemMinnow; global itemCrayfish; global itemShrimp; global itemSardine; global itemKarambwanji; global itemHerring; global itemAnchovies; global itemMackerel; global itemTrout; global itemCod; global itemPike; global itemSlimyEel; global itemSalmon; global itemTuna; global itemCaveEel; global itemRainbowFish; global itemLobster; global itemBass; global itemSwordfish; global itemLavaEel; global itemMonkfish; global itemKarambwan; global itemShark; global itemBaronShark; global itemCavefish; global itemRocktail
    global doneFishList
    def prompt(m):
        global f
        global playerHP
        f = m
        print()
        print("Your HP: %i" % playerHP)
        healActionList = ["food", "exit", "help"]
        print("Enter an action, type 'help' for help, or 'exit' to exit!")
        healAction=input("Heal action: ")
        if(healAction in healActionList):
            if(healAction == "food"):
                healAdv.food()
            elif(healAction == "exit"):
                game.actionPrompt()
            elif(healAction == "help"):
                healAdv.help()
        else:
            healAdv.heal(healAction)

    def heal(healAction):
        global f
        global playerHP
        runHeal = 1
        incX = 0
        while(runHeal == 1):
            fishDone = doneFishList[incX]
            if(healAction.lower() == fishDone[0].lower()):
                if(fishDone[5] >= 1):
                    print("Healed!")
                    fishDone[5] -= 1
                    playerHP += fishDone[7]
                    go=input("Press enter to continue.")
                    runHeal = 0
                else:
                    print("\nYou don't have any %s to eat!" % fishDone[0])
                    go=input("Press enter to continue.")
                    runHeal = 0
            else:
                if(incX <= 24):
                    incX += 1
                else:
                    print("\nInvalid command, sorry!")
                    go=input("Press enter to continue.")
                    healAdv.prompt(f)
        healAdv.prompt(f)

    def food():
        global f
        print("\nYour food:")
        incY2 = 0
        dF = 1
        lol = 0
        while(dF == 1):
            doneFood = doneFishList[incY2]
            if(doneFood[5] > 0):
                print("    %s: %i" % (doneFood[0], doneFood[5]))
                lol += 1
            incY2 += 1
            if(incY2 == 26):
                dF = 0
        if(lol == 0):
            print("None!")
        go=input("\nPress enter to continue.")
        healAdv.prompt(f)

    def help():
        global f
        global playerHP
        print("Your health: %i\n" % playerHP)
        print("\nCommands: ")
        print("    food = Displays your food")
        print("    exit = Exits the program")
        print("    help = Displays this screen")
        print("\nOr enter a food name to heal.")
        go=input("Press enter to continue.")
        healAdv.prompt(f)

class shop:
    def prompt():
        global playerBal
        system.clear()
        print("<> The Market <>")
        print("Type 'buy', 'sell', or try 'help' / 'exit'")
        buyAction = input("Shop action: ")
        if(buyAction == "help"):
            shop.help()
        elif(buyAction == "exit"):
            game.actionPrompt()
        elif(buyAction == "buy"):
            shop.buy()
        elif(buyAction == "sell"):
            shop.sell()
        else:
            print("Invalid comand!")
            go=input("Press enter to continue.")
            shop.prompt()
    def help():
        print("\n<-- Shop help menu -->\n")
        print("'help' = Displays this interface")
        print("'exit' = Exits back to the main action prompt")
        print("'buy' = Displayer buying interface")
        print("'sell' = Displays selling interface")
        go=input("\nPress enter to continue.")
        shop.prompt()
    def buy():
        system.clear()
        global itemRAWMinnow; global itemRAWCrayfish; global itemRAWShrimp; global itemRAWSardine; global itemRAWKarambwanji; global itemRAWHerring; global itemRAWAnchovies; global itemRAWMackerel; global itemSeaweed; global itemRAWTrout; global itemRAWCod; global itemRAWPike; global itemRAWSlimyEel; global itemRAWSalmon; global itemFrogSpawn; global itemRAWTuna; global itemRAWCaveEel; global itemRAWRainbowFish; global itemRAWLobster; global itemRAWBass; global itemRAWSwordfish; global itemRAWLavaEel; global itemRAWMonkfish; global itemRAWKarambwan; global itemRAWShark; global itemRAWBaronShark; global itemRAWCavefish; global itemRAWRocktail
        global itemMinnow; global itemCrayfish; global itemShrimp; global itemSardine; global itemKarambwanji; global itemHerring; global itemAnchovies; global itemMackerel; global itemTrout; global itemCod; global itemPike; global itemSlimyEel; global itemSalmon; global itemTuna; global itemCaveEel; global itemRainbowFish; global itemLobster; global itemBass; global itemSwordfish; global itemLavaEel; global itemMonkfish; global itemKarambwan; global itemShark; global itemBaronShark; global itemCavefish; global itemRocktail
        global buyableItemList
        global playerBal
        print("[+] Buying interface [+] || Balance: %i\n" % playerBal)
        print("Enter item you'd like to buy, 'list' to display items, or 'exit'")
        buyItem = input("Buy action: ")
        x = 0
        if(buyItem == "list"):
            print("Buyable items: \n")
            y = 0
            lol = 0
            while(y == 0):
                if(x < len(buyableItemList)):
                    itemBuy = buyableItemList[x]
                    print("%s" % itemBuy[0])
                    x += 1
                    lol += 1
                else:
                    if(lol == 0):
                        print("None!\n")
                    go=input("Press enter to continue.")
                    shop.buy()
        elif(buyItem == "exit"):
            shop.prompt()
        elif(buyItem.lower() in str(buyableItemList).lower()):
            y = 0
            while(y == 0):
                if(x < 56):
                    itemBuy = buyableItemList[x]
                    if(buyItem.lower() == itemBuy[0].lower()):
                        if(itemBuy[6] <= playerBal):
                            itemBuy[5] += 1
                            playerBal -= itemBuy[6]
                            print("You purchased 1 %s for %i" % (itemBuy[0], itemBuy[6]))
                            time.sleep(0.3)
                            shop.buy()
                        else:
                            print("Not enough money! Item costs: %i" % itemBuy[6])
                            time.sleep(0.3)
                            shop.buy()
                    else:
                        x += 1
                else:
                    print("Invalid item!")
                    go=input("Press enter to continue.")
                    shop.buy()
        else:
            print("Invalid action!")
            shop.buy()
    def sell():
        system.clear()
        global itemRAWMinnow; global itemRAWCrayfish; global itemRAWShrimp; global itemRAWSardine; global itemRAWKarambwanji; global itemRAWHerring; global itemRAWAnchovies; global itemRAWMackerel; global itemSeaweed; global itemRAWTrout; global itemRAWCod; global itemRAWPike; global itemRAWSlimyEel; global itemRAWSalmon; global itemFrogSpawn; global itemRAWTuna; global itemRAWCaveEel; global itemRAWRainbowFish; global itemRAWLobster; global itemRAWBass; global itemRAWSwordfish; global itemRAWLavaEel; global itemRAWMonkfish; global itemRAWKarambwan; global itemRAWShark; global itemRAWBaronShark; global itemRAWCavefish; global itemRAWRocktail
        global itemMinnow; global itemCrayfish; global itemShrimp; global itemSardine; global itemKarambwanji; global itemHerring; global itemAnchovies; global itemMackerel; global itemTrout; global itemCod; global itemPike; global itemSlimyEel; global itemSalmon; global itemTuna; global itemCaveEel; global itemRainbowFish; global itemLobster; global itemBass; global itemSwordfish; global itemLavaEel; global itemMonkfish; global itemKarambwan; global itemShark; global itemBaronShark; global itemCavefish; global itemRocktail
        global buyableItemList
        global playerBal
        print("[-] Selling interface [-] || Balance: %i\n" % playerBal)
        print("Enter item you'd like to sell, 'list' to display items, or 'exit'")
        sellItem = input("Sell action: ")
        if(sellItem == "list"):
            print("\nSellable items: \n")
            y = 0
            x = 0
            lol = 0
            while(y == 0):
                if(x < len(buyableItemList)):
                    itemSell = buyableItemList[x]
                    if(itemSell[5] > 0):
                        print("%s: %s" % (itemSell[0], itemSell[5]))
                        lol +=  1
                    x += 1
                else:
                    if(lol == 0):
                        print("None!\n")
                    go=input("Press enter to continue.")
                    shop.sell()
        elif(sellItem == "exit"):
            shop.prompt()
        elif(sellItem.lower() in str(buyableItemList).lower()):
            y = 0
            x = 0
            while(y == 0):
                if(x < 56):
                    itemSell = buyableItemList[x]
                    if(sellItem.lower() == itemSell[0].lower()):
                        if(itemSell[5] > 0):
                            itemSell[5] -= 1
                            playerBal += itemSell[6]
                            print("You sold 1 %s for %s" % (itemSell[0], itemSell[6]))
                            time.sleep(0.3)
                            shop.sell()
                        else:
                            print("You don't have any %s to sell!" % itemSell[0])
                            time.sleep(0.3)
                            shop.sell()
                    else:
                        x += 1
                else:
                    print("Invalid item!")
                    go=input("Press enter to continue.")
                    shop.sell()
        else:
            print("Invalid action!")
            shop.sell()

class mine:
    def prompt():
        system.clear()
        print("# The Quarry # | Level %i\n" % mineLevel)
        print("Enter an ore to mine, try 'help' or 'exit'")
        mineAction=input("Mining action: ")
        if(mineAction=="help"):
            mine.help()
        elif(mineAction=="ores" or mineAction=="list"):
            mine.listOres()
        elif(mineAction=="exit"):
            game.actionPrompt()
        elif(mineAction=="stats"):
            mine.stats()
        else:
            mine.mine(mineAction)
    def help():
        print("Mining help")
        print("'ores' = Lists ores")
        print("'help' = Displays this interface")
        print("'exit' = Exits back to the main prompt")
        print("\nOr enter an ore type to mine it.")
    def listOres():
        global oreList
        x = 0
        oreNow = oreList[x]
        print("Clay            - Level: %i  | XP: %i" % (oreNow[8], oreNow[7]))
        x += 1
        oreNow = oreList[x]
        print("Rune Essence    - Level: %i  | XP: %i" % (oreNow[8], oreNow[7]))
        x += 1
        oreNow = oreList[x]
        print("Copper          - Level: %i  | XP: %i" % (oreNow[8], oreNow[7]))
        x += 1
        oreNow = oreList[x]
        print("Tin             - Level: %i  | XP: %i" % (oreNow[8], oreNow[7]))
        x += 1
        oreNow = oreList[x]
        print("Limestone       - Level: %i | XP: %i" % (oreNow[8], oreNow[7]))
        x += 1
        oreNow = oreList[x]
        print("Iron            - Level: %i | XP: %i" % (oreNow[8], oreNow[7]))
        x += 1
        oreNow = oreList[x]
        print("Silver          - Level: %i | XP: %i" % (oreNow[8], oreNow[7]))
        x += 1
        oreNow = oreList[x]
        print("Pure Essence    - Level: %i | XP: %i" % (oreNow[8], oreNow[7]))
        x += 1
        oreNow = oreList[x]
        print("Coal            - Level: %i | XP: %i" % (oreNow[8], oreNow[7]))
        x += 1
        oreNow = oreList[x]
        print("Sandstone       - Level: %i | XP: %i" % (oreNow[8], oreNow[7]))
        x += 1
        oreNow = oreList[x]
        print("Gold            - Level: %i | XP: %i" % (oreNow[8], oreNow[7]))
        x += 1
        oreNow = oreList[x]
        print("Granite         - Level: %i | XP: %i" % (oreNow[8], oreNow[7]))
        x += 1
        oreNow = oreList[x]
        print("Mithril         - Level: %i | XP: %i" % (oreNow[8], oreNow[7]))
        x += 1
        oreNow = oreList[x]
        print("Adamant         - Level: %i | XP: %i" % (oreNow[8], oreNow[7]))
        x += 1
        oreNow = oreList[x]
        print("Living minerals - Level: %i | XP: %i" % (oreNow[8], oreNow[7]))
        x += 1
        oreNow = oreList[x]
        print("Runite          - Level: %i | XP: %i" % (oreNow[8], oreNow[7]))
        go=input("Press enter to continue")
        mine.prompt()
    def mine(ore):
        global itemClay; global itemRuneEssence; global itemCopperOre; global itemTinOre; global itemLimestone; global itemIronOre; global itemSilverOre; global itemPureEssence; global itemCoal; global itemSandstone; global itemGoldOre; global itemGranite; global itemMithrilOre; global itemAdamantOre; global itemLivingMinerals; global itemRuniteOre
        global mineLevel
        global mineEXP
        global level
        global strengthLevel
        global strengthEXP
        global luckLevel
        x = 0
        game.myEXP(mineEXP)
        while(x < len(oreList)):
            oreNow = oreList[x]
            if(ore.lower() == str(oreNow[0]).lower()):
                if(mineLevel >= oreNow[8]):
                    oreNow[5] += 1
                    mineEXP += (oreNow[7] * (1.0 + ((mineLevel - 1) * 0.01)))
                    strengthEXP += (oreNow[7] / 10)

                    mineLevel = level
                    game.myEXP(strengthEXP)
                    strengthLevel = level

                    print("\nYou swing your pickaxe..")
                    mine.loadBar()
                    print("\nYou mined %s and gained + %0.1f XP!" % (oreNow[0], oreNow[7]))
                    gemFound = "false"
                    luckinessF = ( (luckLevel * 10) / 2 ) + 10
                    luckiness = int(luckinessF)
                    while(gemFound == "false"):
                        gemFind = random.randint(1, 1000)
                        if(gemFind in range(0, (10 + mineLevel))):
                            mine.gemFound(1) # Dragonstone
                            gemFound == "true"
                        elif(gemFind in range(0, (luckiness + 20 + mineLevel))):
                            mine.gemFound(2) # Diamond
                            gemFound == "true"
                        elif(gemFind in range(0, (luckiness + 30 + mineLevel))):
                            mine.gemFound(3) # Ruby
                            gemFound == "true"
                        elif(gemFind in range(0, (luckiness + 40 + mineLevel))):
                            mine.gemFound(4) # Emerald
                            gemFound == "true"
                        elif(gemFind in range(0, (luckiness + 50 + mineLevel))):
                            mine.gemFound(5) # Sapphire
                            gemFound == "true"
                        else:
                            gemFound = "true"
                    go=input("Press enter to continue.")
                    mine.prompt()
                else:
                    print("\nNot high enough level! Level needed: %i" % oreNow[8])
                    go=input("Press enter to continue")
                    mine.prompt()
            else:
                x += 1
        else:
            print("Invalid action: '%s'" % ore)
            go=input("Press enter to continue.")
            mine.prompt()
    def gemFound(gem):
        global mineEXP
        global luckEXP
        if(gem == 0):
            print("<> YOU FOUND AN ONYX!!! + 10000.0 XP")
            itemUncutOnyx[5] += 1
            mineEXP += 10000
            luckEXP += 1000
        elif(gem == 1):
            print("<> YOU FOUND A DRAGONSTONE! + 5000.0 XP")
            itemUncutDragonstone[5] += 1
            mineEXP += 5000
            luckEXP += 500
        elif(gem == 2):
            print("<> You found a Diamond!!! + 2500.0 XP")
            itemUncutDiamond[5] += 1
            mineEXP += 2500
            luckEXP += 250
        elif(gem == 3):
            print("<> You found a Ruby! + 1000.0 XP")
            itemUncutRuby[5] += 1
            mineEXP += 1000
            luckEXP += 100
        elif(gem == 4):
            print("<> You found an Emerald! + 500.0 XP")
            itemUncutEmerald[5] += 1
            mineEXP += 500
            luckEXP += 50
        elif(gem == 5):
            print("<> You found a Sapphire! + 100.0 XP")
            itemUncutSapphire[5] += 1
            mineEXP += 100
            luckEXP += 10
        game.myEXP(mineEXP)
        minelevel = level
    def stats():
        global mineLevel
        global mineEXP
        global strengthLevel
        global strengthEXP
        game.myEXP(mineEXP)
        mineLevel = level
        game.myEXP(strengthEXP)
        strengthLevel = level
        print("Mining stats:\n")
        print("Mining level: %i" % mineLevel)
        print("Mining EXP: %i" % mineEXP)
        print("\nStrength Level: %i" % strengthLevel)
        print("Strength EXP: %i" % strengthEXP)
        go=input("Press enter to continue.")
        mine.prompt()
    def loadBar():
        global mineLevel
        global strengthLevel
        loadTime = 0.2 / ((mineLevel * (strengthLevel * 0.1) * 0.005) + 0.995)
        s = "[==========]"
        for c in s:
            sys.stdout.write('%s' % c )
            sys.stdout.flush()
            time.sleep(loadTime)

class build:
    def prompt():
        system.clear()
        print(":: Building Station :: | Level: %i" % buildLevel)
        print("Enter type of building, or try 'help' / 'exit'")
        buildAction=input("Building action: ")
        if(buildAction.lower() == "help"):
            build.help()
        elif(buildAction.lower() == "exit"):
            game.actionPrompt()
        elif(buildAction.lower() == "craft"):
            craft.prompt()
        elif(buildAction.lower() == "smelt"):
            smelt.prompt()
        elif(buildAction.lower() == "smith"):
            smith.prompt()
        elif(buildAction.lower() == "fletch"):
            fletch.prompt()
        else:
            print("\nInvalid action: %s" % buildAction)
            go=input("Press enter to continue")
            build.prompt()

    def help():
        print("Building help")
        print("'craft'  = Displays crafting interface")
        print("'smelt'  = Displays smelting interface")
        print("'smith'  = Displays smithing interface")
        print("'fletch' = Displays fletching interface")
        print("'help'   = Displays this interface")
        print("'exit'   = Exits back to the main prompt")
        go=input("\nPress enter to continue.")
        build.prompt()

class smelt:
    def prompt():
        system.clear()
        print("** Blacksmith Workshop **")
        print("Enter an item to smelt, or try 'help' / exit'")
        smeltAction=input("Smelting action: ")
        if(smeltAction.lower() == "bars" or smeltAction.lower() == "list"):
            smelt.barList()
        elif(smeltAction.lower() == "help"):
            smelt.help()
        elif(smeltAction.lower() == "exit"):
            build.prompt()
        else:
            smelt.smeltBar(smeltAction)
    def smeltBar(barType):
        global buildEXP
        global buildLevel
        runLoop = 1
        x = 0
        smeltBar = barList[x]
        while(runLoop == 1):
            if(barType.lower() == smeltBar[0].lower()):
                if(buildLevel >= smeltBar[8]):
                    primaryOre = smeltBar[9]
                    secondaryOre = smeltBar[10]
                    if(primaryOre[5] >= 1):
                        if(secondaryOre[5] >= smeltBar[11]):
                            primaryOre[5] -= 1
                            secondaryOre[5] -= smeltBar[11]
                            smeltBar[5] += 1
                            buildEXP += smeltBar[7]
                            print("\nYou have smelted %s and earned + %0.1f XP!" % (smeltBar[0], smeltBar[7]))
                            go=input("Press enter to continue.")
                            smelt.prompt()
                        else:
                            print("\nYou need at least 1 %s & %i %s to do that!" % (primaryOre[0], smeltBar[11], secondaryOre[0]))
                            print("You have: %i %s & %i %s" % (primaryOre[5], primaryOre[0], secondaryOre[5], secondaryOre[0]))
                            go=input("Press enter to continue")
                            smelt.prompt()
                    else:
                        print("\nYou need at least 1 %s & %i %s to do that!" % (primaryOre[0], smeltBar[11], secondaryOre[0]))
                        print("You have: %i %s & %i %s" % (primaryOre[5] , primaryOre[0], secondaryOre[5], secondaryOre[0]))
                        go=input("Press enter to continue")
                        smelt.prompt()
                else:
                    print("\nNot high enough level! Required level: %i" % smeltBar[8])
                    go=input("Press enter to continue.")
                    smelt.prompt()
            else:
                if(x < len(barList)):
                    x += 1
                    smeltBar = barList[x - 1]
                else:
                    runLoop = 0
        else:
            print("\nInvalid action: %s. Try 'help'" % barType)
            go=input("Press enter to continue.")
            smelt.prompt()
        print(len(oreList))
        print(barType)
        time.sleep(5)
    def help():
        print("Smithing help:\n")
        print("'bars' = Lists bars")
        print("'help' = Displays this interface")
        print("'exit = Exits back to crafting prompt'")
        go=input("\nPress enter to continue.")
        smelt.prompt()
    def barList():
        print("\nBar list:\n")
        x = 0
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Bronze Bar      - Level: %i  | XP: %0.1f  | Requires: 1 %s ore & %i %s ore" % (barNow[8], barNow[7], primaryOre[0], barNow[11], secondaryOre[0]))
        x += 1; print("----------------------------+----------+--------->")
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Iron Bar        - Level: %i | XP: %0.1f | Requires: 1 %s ore" % (barNow[8], barNow[7], primaryOre[0]))
        x += 1; print("----------------------------+----------+--------->")
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Silver Bar      - Level: %i | XP: %0.1f | Requires: 1 %s ore" % (barNow[8], barNow[7], primaryOre[0]))
        x += 1; print("----------------------------+----------+--------->")
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Steel Bar       - Level: %i | XP: %0.1f | Requires: 1 %s ore & %i %s" % (barNow[8], barNow[7], primaryOre[0], barNow[11], secondaryOre[0]))
        x += 1; print("----------------------------+----------+--------->")
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Gold Bar        - Level: %i | XP: %0.1f | Requires: 1 %s ore" % (barNow[8], barNow[7], primaryOre[0]))
        x += 1; print("----------------------------+----------+--------->")
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Mithril Bar     - Level: %i | XP: %0.1f | Requires: 1 %s ore & %i %s" % (barNow[8], barNow[7], primaryOre[0], barNow[11], secondaryOre[0]))
        x += 1; print("----------------------------+----------+--------->")
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Adamant Bar     - Level: %i | XP: %0.1f | Requires: 1 %s ore & %i %s" % (barNow[8], barNow[7], primaryOre[0], barNow[11], secondaryOre[0]))
        x += 1; print("----------------------------+----------+--------->")
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Runite Bar      - Level: %i | XP: %0.1f | Requires: 1 %s ore & %i %s" % (barNow[8], barNow[7], primaryOre[0], barNow[11], secondaryOre[0]))

        go=input("\nPress enter to continue.")
        smelt.prompt()

class craft:
    global buildLevel
    global buildEXP
    def prompt():
        system.clear()
        print("== Crafting Workshop == | Level: %i" % buildLevel)
        print("Enter an item to craft, or try 'help' / exit'")
        craftAction=input("Crafting action: ")
        if(craftAction.lower() == "gems" or craftAction.lower() == "list"):
            craft.gemList()
        elif(craftAction.lower() == "help"):
            craft.help()
        elif(craftAction.lower() == "exit"):
            build.prompt()
        else:
            craft.craftGems(craftAction)
    def craftGems(gemType):
        global buildEXP
        global buildLevel
        runLoop = 1
        x = 0
        uncutGem = uncutGemList[x]
        cutGem = gemList[x]
        while(runLoop == 1):
            if(gemType.lower() == uncutGem[0].lower() or gemType.lower() == cutGem[0].lower()):
                if(buildLevel >= cutGem[8]):
                    if(uncutGem[5] >= 1):
                        uncutGem[5] -= 1
                        cutGem[5] += 1
                        buildEXP += cutGem[7]
                        print("\nYou have crafted %s and earned + %0.1f XP!" % (cutGem[0], cutGem[7]))
                        game.myEXP(buildEXP)
                        buildlevel = level
                        go=input("Press enter to continue.")
                        craft.prompt()
                    else:
                        print("\nYou need at least 1 %s & to do that!" % uncutGem[0])
                        print("You have: %i %s" % (uncutGem[5], uncutGem[0]))
                        go=input("Press enter to continue")
                        craft.prompt()
                else:
                    print("\nNot high enough level! Required level: %i" % cutGem[8])
                    go=input("Press enter to continue.")
                    craft.prompt()
            else:
                if(x < len(gemList)):
                    x += 1
                    uncutGem = uncutGemList[x - 1]
                    cutGem = gemList[x - 1]
                else:
                    runLoop = 0
        else:
            print("\nInvalid action: %s. Try 'help'" % gemType)
            go=input("Press enter to continue.")
            craft.prompt()

    def help():
        print("Crafting help:\n")
        print("'gems' = Lists gems")
        print("'help' = Displays this interface")
        print("'exit = Exits back to crafting prompt'")
        go=input("\nPress enter to continue.")
        craft.prompt()
    def gemList():
        print("\nBar list:\n")
        x = len(gemList) - 1
        gemNow = gemList[x]
        print("Opal            - Level: %i  | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Jade            - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Red Topaz       - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Sapphire        - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Emerald         - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Ruby            - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Diamond         - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Dragonstone     - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Onyx            - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Hydrix          - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))

        go=input("\nPress enter to continue.")
        craft.prompt()

class smith:
    def prompt():
        print("** Blacksmith Workshop **")
        print("Enter an item to smith, or try 'help' / exit'")
        smithAction=input("Smithing action: ")
        if(smithAction.lower() == "ores"):
            smith.oreList()
        elif(smithAction.lower() == "help"):
            smith.help()
        elif(smithAction.lower() == "exit"):
            game.actionPrompt()
        else:
            print("Invalid action")
            go=input("Press enter to continue.")
            smith.prompt()
    def help():
        print("Smithing help:\n")
        print("'ores' = Lists ores")
        print("'help' = Displays this interface")
        print("'exit = Exits back to crafting prompt'")
        go=input("\nPress enter to continue.")
        craft.smith()
    def oreList():
        print("Clay            - Level: %i  | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Rune Essence    - Level: %i  | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Copper          - Level: %i  | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Tin             - Level: %i  | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Limestone       - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Iron            - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Silver          - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Pure Essence    - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Coal            - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Sandstone       - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Gold            - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Granite         - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Mithril         - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Adamant         - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Living minerals - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Runite          - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))

class fletch:
    def prompt():
        print("Fletch")

# Actions
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
game.runGame()
