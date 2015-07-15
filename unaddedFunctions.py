def fishAdv():
   "You are now fishing!"
   time.sleep(5)
   #run loadingBar

#

def cookAdv():
   "What would you like to cool? List cookable items in inventoryList"

#

def healAdv():
   "What would you like to use to heal? List items in inventoryList"

def heal():
   print ("Healed %i HP" % 10)
   playerHP += 10
#

def fightAdv():
    global monsterGoblin
    global monsterName
    global monsterHP
    global monsterMaxHit
    global monsterXP
    global monsterCoins
    global monsterItemsDropped
    fightMonster()
    while(monsterHP > 0):
        fightActionList = ["a","h","r"]
        print(monsterName + " has appeared! HP:" + str(monsterXP))
        print("Your health: %i" % (playerHP)
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
        playerBal += monsterCoins
#
