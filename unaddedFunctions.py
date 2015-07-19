import os
import platform
import time

def fishAdv():
    clearScreen()
    global baitCount
    global fishCount
    global playerBal
    print("What kind of fishing would you like to do?")
    print("Type the kind, 'l' to list kinds, or type 'e' to exit")
    fishAction=input("Fish action:")
    if(fishAction=="f"):
        if(baitCount == 0):
            print("You don't have any bait!")
            time.sleep(0.5)
            fish()
        else:
            fishCatch=["null", "Catfish", "Carp", "Salmon", "Whale, somehow"]
            mining=random.randint(1, 4)
            print("You cast your line..")
            time.sleep(0.2)
            print("You feel a bite!")
            time.sleep(0.2)
            print("You reel in your fish!")
            time.sleep(0.2)
            print("You have caught: %a" % fishCatch[mining])
            baitCount -= 1
            fishCount += 1
            time.sleep(0.6)
            fish()
    if(fishAction=="l"):
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

#

def levellingSystem():
    points = 0
    for level in range(1,100):
        diff = int(level + 300 * math.pow(2, float(level)/7) )
        points += diff
        str = "Level %d = %d" % (level + 1, points / 4)
    print(str)

def cookAdv():
   "What would you like to cool? List cookable items in inventoryList"

#

def healAdv():
   "What would you like to use to heal? List items in inventoryList"

def heal():
   print ("Healed %i HP" % 10)
   playerHP += 10
#

#








miningSkill=65

class mining:
    def init():
        mining.arrays()
        if(miningSkill < 15):
            return
        elif(miningSkill < 20):
            mining.level15()
        elif(miningSkill < 30):
            mining.level20()
        elif(miningSkill < 40):
            mining.level30()
        elif(miningSkill < 50):
            mining.level40()
        elif(miningSkill < 70):
            mining.level50()
        elif(miningSkill < 77):
            mining.level70()
        elif(miningSkill < 85):
            mining.level77()
        else:
            mining.level85()

    def arrays():
        global oreAble
        global minel15
        global minel20
        global minel30
        global minel40
        global minel50
        global minel70
        global minel77
        global minel85
        oreAble=["Copper", "Tin"]
        minel15=["Iron"]
        minel20=["Silver"]
        minel30=["Coal"]
        minel40=["Gold"]
        minel50=["Mithril"]
        minel70=["Adamantite"]
        minel77=["Bane"]
        minel85=["Runite"]

    def level15():
        global oreAble
        oreAble.extend(minel15)
    def level20():
        global oreAble
        mining.level15()
        oreAble.extend(minel20)
    def level30():
        global oreAble
        mining.level20()
        oreAble.extend(minel30)
    def level40():
        global oreAble
        mining.level30()
        oreAble.extend(minel40)
    def level50():
        global oreAble
        mining.level40()
        oreAble.extend(minel50)
    def level70():
        global oreAble
        mining.level50()
        oreAble.extend(minel70)
    def level77():
        global oreAble
        mining.level70()
        oreAble.extend(minel77)
    def level85():
        global oreAble
        mining.level77()
        oreAble.extend(minel85)

mining.init()
ore="Runite"
if(ore in oreAble):
    print("You Obtained: %s" % ore)
else:
    print("You Can't Mine: %s" % ore)
