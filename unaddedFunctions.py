def fishAdv():
   "You are now fishing!"
   time.sleep(5)
   #run loadingBar

def fish():
   print("You are now fishing.")
#

def cookAdv():
   "What would you like to cool? List cookable items in inventoryList"

def cook():
   print("You are now cooking.")
#

def healAdv():
   "What would you like to use to heal? List items in inventoryList"

def heal():
   print ("Healed %i HP", %, 10)
   playerHP += 10
#

def fightAdv():
   print("You are now fighting: %s.", %, monster)

def fight():
   playerHP = 10
   enemyHP = 20
   fightActionList = ["a","h","r"]
   print("You are now fighting!")
   print("Your health: %i, enemy health: %i ", %, 10, 20)
   print("Type 'a' to attack, 'h' to heal, or 'r' to run!")
   action=input("Action: ")
   if (action in fightActionList):
        if (action==fightActionList[0]):
            attack()
        elif(action==fightActionList[1]):
            heal()
        elif(action==fightActionList[2]):
            run()
        else:
            print("Something's up...")
   def attack()
      print("Enemy has lost %i HP", %, 5)
      enemyHP -= 5
      print("Enemy attacks! You lost %i HP", % 1)
      playerHP -= 1
      fight()
#
