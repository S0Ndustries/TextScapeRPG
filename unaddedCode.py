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
attackSkill = 1
strengthSkill = 1
defenceSkill = 1
rangedSkill = 1
magicSkill = 1
healthSkill = 1
craftingSkill = 1
miningSkill = 1
fishingSkill = 1
cookingSkill = 1
woodcuttingSkill = 1
agilitySkill = 1
herbloreSkill = 1
farmingSkill = 1
huntingSkill = 1
summoningSkill = 1
#

def loadingBar():
   while(loading < 11):
       print("[" + equal + "]")
       loading += 1
       sleep(0.1)

class fishChoose:
    def init():
        fishChoose.arrays()
        if(fishingSkill < 5):
            return
        elif(fishingSkill < 10):
            fishChoose.level5()
        elif(fishingSkill < 15):
            fishChoose.level10()
        elif(fishingSkill < 16):
            fishChoose.level15()
        elif(fishingSkill < 20):
            fishChoose.level16()
        elif(fishingSkill < 23):
            fishChoose.level20()
        elif(fishingSkill < 25):
            fishChoose.level23()
        else:
            fishChoose.level25()

    def arrays():
        global fishPoss
        global fishingSkill5
        global fishingSkill10
        global fishingSkill15
        global fishingSkill16
        global fishingSkill20
        global fishingSkill23
        global fishingSkill25
        fishPoss=["Shrimp", "Crayfish", "Minnow"]
        fishingSkill5=["Karabwanji", "Sardine"]
        fishingSkill10=["Herring"]
        fishingSkill15=["Anchovies"]
        fishingSkill16=["Mackeral"]
        fishingSkill20=["Trout"]
        fishingSkill23=["Cod"]
        fishingSkill25=["Pike"]

    def level5():
        global fishPoss
        fishPoss.extend(fishingSkill5)
    def level10():
        global fishPoss
        fishChoose.level5()
        fishPoss.extend(fishingSkill10)
    def level15():
        global fishPoss
        fishChoose.level10()
        fishPoss.extend(fishingSkill15)
    def level16():
        global fishPoss
        fishChoose.level15()
        fishPoss.extend(fishingSkill16)
    def level20():
        global fishPoss
        fishChoose.level16()
        fishPoss.extend(fishingSkill20)
    def level23():
        global fishPoss
        fishChoose.level20()
        fishPoss.extend(fishingSkill23)
    def level25():
        global fishPoss
        fishChoose.level23()
        fishPoss.extend(fishingSkill25)

fishChoose.init()
print(fishPoss)
