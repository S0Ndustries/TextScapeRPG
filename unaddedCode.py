import os
import platform
import time
import random

global fishPoss

def bankList():
#   slots 1 - 50
    print("bankList")
def loadingScreen():
   print(topBar)
   time.sleep(0.3)
   print(coderList)
   time.sleep(0.3)
   print(betaTesters)
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
ranged= 1
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
   while(loading < 11):
       print("[" + equal + "]")
       loading += 1
       sleep(0.1)

fishl=26
class fishChoose:
    def init():
        fishChoose.arrays()
        if(fishl < 5):
            return
        elif(fishl < 10):
            fishChoose.level5()
        elif(fishl < 15):
            fishChoose.level10()
        elif(fishl < 16):
            fishChoose.level15()
        elif(fishl < 20):
            fishChoose.level16()
        elif(fishl < 23):
            fishChoose.level20()
        elif(fishl < 25):
            fishChoose.level23()
        else:
            fishChoose.level25()

    def arrays():
        global fishPoss
        global fishl5
        global fishl10
        global fishl15
        global fishl16
        global fishl20
        global fishl23
        global fishl25
        fishPoss=["Shrimp", "Crayfish", "Minnow"]
        fishl5=["Karabwanji", "Sardine"]
        fishl10=["Herring"]
        fishl15=["Anchovies"]
        fishl16=["Mackeral"]
        fishl20=["Trout"]
        fishl23=["Cod"]
        fishl25=["Pike"]

    def level5():
        global fishPoss
        fishPoss.extend(fishl5)
    def level10():
        global fishPoss
        fishChoose.level5()
        fishPoss.extend(fishl10)
    def level15():
        global fishPoss
        fishChoose.level10()
        fishPoss.extend(fishl15)
    def level16():
        global fishPoss
        fishChoose.level15()
        fishPoss.extend(fishl16)
    def level20():
        global fishPoss
        fishChoose.level16()
        fishPoss.extend(fishl20)
    def level23():
        global fishPoss
        fishChoose.level20()
        fishPoss.extend(fishl23)
    def level25():
        global fishPoss
        fishChoose.level23()
        fishPoss.extend(fishl25)

fishChoose.init()
print(fishPoss)
