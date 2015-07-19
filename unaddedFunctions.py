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










class mining:
    def 
