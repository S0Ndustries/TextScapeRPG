import os
import platform
import time
import random

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
    def __init__():
        mining.oreAble()
        ore=input("What Ore Would You Like To Mine: ")
        if(mining.ismineAble(ore)):
            print("You obtained: %s" % ore)
        else:
            print("You cant mine %s!" % ore)
    def ismineAble(ore):
        if ore in mineAble:
            return True
        else:
            return False
    def oreAble():
        global mineAble
        mineAble=["Copper", "Tin"]
        if(miningSkill < 15):
            pass
        elif(miningSkill < 20):
            mineAble.append("Iron")
        elif(miningSkill < 30):
            mineAble.append("Iron")
            mineAble.append("Silver")
        elif(miningSkill < 40):
            mineAble.append("Iron")
            mineAble.append("Silver")
            mineAble.append("Coal")
        elif(miningSkill < 50):
            mineAble.append("Iron")
            mineAble.append("Silver")
            mineAble.append("Coal")
            mineAble.append("Gold")
        elif(miningSkill < 70):
            mineAble.append("Iron")
            mineAble.append("Silver")
            mineAble.append("Coal")
            mineAble.append("Gold")
            mineAble.append("Mithril")
        elif(miningSkill < 77):
            mineAble.append("Iron")
            mineAble.append("Silver")
            mineAble.append("Coal")
            mineAble.append("Gold")
            mineAble.append("Mithril")
            mineAble.append("Adamantite")
        elif(miningSkill < 85):
            mineAble.append("Iron")
            mineAble.append("Silver")
            mineAble.append("Coal")
            mineAble.append("Gold")
            mineAble.append("Mithril")
            mineAble.append("Adamantite")
            mineAble.append("Bane")
        else:
            mineAble.append("Iron")
            mineAble.append("Silver")
            mineAble.append("Coal")
            mineAble.append("Gold")
            mineAble.append("Mithril")
            mineAble.append("Adamantite")
            mineAble.append("Bane")
            mineAble.append("Runite")





bait=input("Bait: ")
level=input("Level: ")
level=int(level)
fishPoss=[]

class fishType(object):
    def __init__(self, name, levelReq, caughtWith):
        self.name = name
        self.levelReq = levelReq
        self.caughtWith = caughtWith
    def catchAble(self):
        if(self.caughtWith == bait and self.levelReq <= level):
            self.canCatch=True
        else:
            self.canCatch=False
        self.catchMsg()
    def catchMsg(self):
        global fishPoss
        if(self.canCatch):
            fishPoss.append(self.name)
        else:
            pass



shrimp=fishType("Shrimp", 1, 'net')
crayfish=fishType("Crayfish", 1, 'crayfish cage')
minnow=fishType("Minnow", 1, 'net')
karambwanji=fishType("Karambwanji", 5, 'net')
sardine=fishType("Sardine", 5, 'bait')
herring=fishType("Herring", 10, 'bait')
anchovies=fishType("Anchovies", 15, 'net')

fishType.catchAble(shrimp)
fishType.catchAble(crayfish)
fishType.catchAble(minnow)
fishType.catchAble(karambwanji)
fishType.catchAble(sardine)
fishType.catchAble(herring)
fishType.catchAble(anchovies)

print("You Can Catch: %a" % fishPoss)
fishPossChoose=random.randint(0, (len(fishPoss)-1))
print("You Caught: '%s'" % fishPoss[fishPossChoose])
