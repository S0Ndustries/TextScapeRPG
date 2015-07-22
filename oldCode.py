
def defFish():
    global shrimp
    global crayfish
    global minnow
    global karambwanji
    global sardine
    global herring
    global anchovies
    shrimp=fishType("Shrimp", 1, 'net')
    crayfish=fishType("Crayfish", 1, 'crayfish cage')
    minnow=fishType("Minnow", 1, 'net')
    karambwanji=fishType("Karambwanji", 5, 'net')
    sardine=fishType("Sardine", 5, 'bait')
    herring=fishType("Herring", 10, 'bait')
    anchovies=fishType("Anchovies", 15, 'net')

class fishType(object):
    def __init__(self, name, levelReq, caughtWith):
        self.name = name
        self.levelReq = levelReq
        self.caughtWith = caughtWith
    def catchAble(self):
        global fishPoss
        if(self.caughtWith == bait and self.levelReq <= fishingSkill):
            fishPoss.append(self.name)
        else:
            pass

def checkCatch():
    fishType.catchAble(shrimp)
    fishType.catchAble(crayfish)
    fishType.catchAble(minnow)
    fishType.catchAble(karambwanji)
    fishType.catchAble(sardine)
    fishType.catchAble(herring)
    fishType.catchAble(anchovies)

class fish:
    def init():
        system.clear()
        global fishPoss
        fishPoss=[]
        print("Raw fish: %i || Bait: %i" % (fishCount, baitCount))
        print("What would you like to do?")
        print("Type 'f' to fish, 'b' to buy bait, 's' to display stats or 'e' to exit")
        fishAction=input("Fish action:")
        if(fishAction=="f"):
            fish.checkBait()
        elif(fishAction=="b"):
            fish.buyBait()
        elif(fishAction=="s"):
            fish.stats()
        elif(fishAction=="e"):
            actionPrompt()
        else:
            print("Invalid action!")
            fish.init()
    def askBait():
        global bait
        validBait=["net", "crayfish cage", "bait"]
        print("What bait would you like to use?")
        bait=input("Bait type: ").lower()
        if(bait in validBait):
            defFish()
            checkCatch()
            fish.fishing()
        else:
            print("Invalid Bait Type")
            time.sleep(1)
            fish.askBait()
    def checkBait():
        if (baitCount == 0):
            print("You don't have any bait!")
            time.sleep(0.5)
            fish.init()
        else:
            fish.askBait()
    def fishing():
        global baitCount
        global fishCount
        global caughtFish
        fishCatch=random.randint(0, (len(fishPoss)-1))
        print("You cast your line..")
        time.sleep(0.5)
        print("You feel a bite!")
        time.sleep(0.3)
        print("You reel in your fish!")
        time.sleep(0.2)
        print("You have caught: %a" % fishPoss[fishCatch])
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
    def stats():
        stats.fish()
        time.sleep(4)
        fish.init()
