def fishAdv():
   "You are now fishing!"
   time.sleep(5)
   #run loadingBar

#

def cookAdv():
   "What would you like to cool? List cookable items in inventoryList"

def cook():
    global fishCount
    global cookedFish
    print("You have %i raw fish. Type the amount you'd like to cook, or 'e' to exit!")
    cookAction=input("Cook action: ")


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
