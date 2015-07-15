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
        time.sleep(0.2)
        print("Type 'a' to attack, 'h' to heal, or 'r' to run!")
        action=input("Fight action: ")
        if (action in fightActionList):
             if (action==fightActionList[0]):
                attackOpt()
             elif(action==fightActionList[1]):
                heal()
             elif(action==fightActionList[2]):
                run()
             else:
                print("Something's up...")
    else:
        playerBal += monsterCoins
#
def attackAdv():
    print("You attacked!")
    global monsterHP
    global playerHP
    global monsterMaxHit
    playerDMG = random.randint(0, 10)
    monsterDMG = random.randint(0, monsterMaxHit)
    print("Enemy has lost %iHP" % playerDMG)
    time.sleep(0.3)
    print("Enemy attacks! You lost %i HP" % monsterDMG)
    enemyHP -= playerDMG
    playerHP -= monsterDMG
    time.sleep(0.3)
#
