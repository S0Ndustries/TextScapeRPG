print(“Welcome to the pyRPG”)
name = input(“Enter your username: ”)
if(name=="Elijah" or name=="Evan"):
    #add some kind of levels
else:
    return

def bankList():
#   slots 1 - 50

def loadingScreen():
   print topBar
   time.sleep(0.3)
   print coderList
   time.sleep(0.3)
   print betaTesters
   time.sleep(0.3)
   oloop=6
   while(oloop > 0):
       print('o', end="")
       time.sleep(0.3)
       oloop-=1

def inventoryList():
# Will store item IDs
# Format item:variation:uses:addons(fire, poison, enchantments, etc)
# Example: 1:0:100:2,5,3

   slot1a = ""
   slot1b = ""
   slot1c = ""

   slot2a = ""
   slot2b = ""
   slot2c = ""

   slot3a = ""
   slot3b = ""
   slot3c = ""

   slot4a = ""
   slot4b = ""
   slot4c = ""

   slot5a = ""
   slot5b = ""
   slot5c = ""

   slot6a = ""
   slot6b = ""
   slot6c = ""

   slot7a = ""
   slot7b = ""
   slot7c = ""

   slot8a = ""
   slot8b = ""
   slot8c = ""

   slot9a = ""
   slot9b = ""
   slot9c = ""


# Game info
topBar = "<>-<>-<> || TextScapeRPG by S0Ndustries || <>-<>-<>"
coderList = "Coded by Evan Young & Elijah Keane"
betaTesters = "Evan, Elijah"
#

# User stats
money = 0
experience = 0
inventorySlotRows=9
bankSlotRows=50
memberStatus=0
#

# User skills
attack = 1
strength = 1
defence = 1
ranged  = 1
magic = 1
health = 1
crafting = 1
mining = 1
fishing = 1
cooking = 1
woodcutting = 1
agility = 1
herblore = 1
farming = 1
hunting = 1
summoning = 1
#

def loadingBar():
   while(loading < 11)
   print("[" + equal + "]"
   loading += 1
   sleep(0.1)

for i in {1..20};
do
	echo -n “*”
	sleep 0.1
done


for x in range(1, 20):
   print(“=”)
   sleep(0.1)


def clear():
    import os
    import platform
    sys_type=platform.system()
    if(sys_type=="Windows"):
        os.system('cls')
    else:
        os.system('clear')
