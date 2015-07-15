def fishAdv():
   "You are now fishing!"
   time.sleep(5)
   #run loadingBar

global baitCount
global fishCount
baitCount = 0
fishCount = 0

def fish():
    print("You are now fishing.")
    if(baitCount == 0):
        print("You don't have any bait!")
        print("Would you like to purchase some bait for 3gp?")
        print("Your balance: %i" % playerBal)
        print("Type 'y' to buy, or 'n' to cancel.")
        buyBait=input("Buy?: ")
        if (buyBait = "y"):
            if (playerBal>=3):
                print("You have bought some bait!")
                playerBal -= 3
                baitCount += 1
    else:
        print("You cast your line..")
        time.sleep(0.4)
        print("You feel a bite!")
        time.sleep(0.2)
        print("You reel in your fish!")
        print("You have caught: %s!" % "a fish")
        baitCount -= 1
        fishCount += 1

#

def cookAdv():
   "What would you like to cool? List cookable items in inventoryList"

def cook():
   print("You are now cooking.")
#

def healAdv():
   "What would you like to use to heal? List items in inventoryList"

def heal():
   print ("Healed %i HP" % 10)
   playerHP += 10
#

def fightAdv():
   print("You are now fighting: %s." % monster)
#
