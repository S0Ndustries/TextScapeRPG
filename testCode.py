# This code is runnable
# Here is a fishing table
# Click this link: http://services.runescape.com/m=rswiki/en/Fishing_Table

import time
import os
class fishAdv():
    # Fish arrays
    global minnow
    global crayfish
    global shrimp
    global sardine
    global karambwanji
    global herring
    global anchovies
    global casket
    global mackerel
    global oyster
    global seaweed
    global trout
    global cod
    global pike
    global slimyeel
    global salmon
    global frogspawn
    global tuna
    global caveeel
    global rainbowfish
    global lobster
    global bass
    global swordfish
    global lavaeel
    global monkfish
    global karambwan
    global shark
    global baronshark
    global cavefish
    global rocktail
    # Other variables
    global fishAction
    global fishLevel
    global fishEXP
    global feathers
    fishEXP = 1000
    fishLevel = 20
    feathers = 4

    def tBaits(fType):
        global fishEXP
        if(fType[2] == 0):
            print("You cast your line into the water.")
            print("Your line is hooked!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(2)
        elif(fType[2] == 1):
            print("You thrust your cage into the water.")
            print("You pull it back out!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(2)
        elif(fType[2] == 2):
            print("You dip your small net into the water.")
            print("You pull it back out!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(2)
        elif(fType[2] == 3):
            print("You cast your large net into the water.")
            print("You pull it back out!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(2)
        elif(fType[2] == 4):
            print("You cast your line into the water.")
            print("You reel it in!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(2)
        elif(fType[2] == 5):
            print("You stab your harpoon into the water.")
            print("You pull it back out!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(2)
        elif(fType[2] == 6):
            print("You place your lobster pot into the water.")
            print("You pull it back out!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(2)
        elif(fType[2] == 7):
            print("You cast your line into the water.")
            print("You reel it in!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(2)
        elif(fType[2] == 6):
            print("You mysteriously use your karambwanvessel.")
            print("You feel a bite!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(2)
        elif(fType[2] == 7):
            print("You mysteriously use your living minerals.")
            print("You feel a bite!")
            print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3]))
            fishEXP += fType[3]
            time.sleep(2)

    def prompt():
        global fishAction
        fishCMDs = ["0","1","2","3","4","5","6","7","8","9","list","guide","exit"]
        # clearScreen()
        os.system('clear')
        print("Enter an action, type 'guide' for help, or 'exit' to exit!")
        fishAction=input("Fish action: ")
        if (fishAction in fishCMDs):
            if (fishAction == "list"):
                fishAdv.list()
            elif(fishAction == "guide"):
                fishAdv.guide()
            elif(fishAction == "exit"):
                print("Exiting...")
                time.sleep(1)
            else:
                fishAdv.fish(fishAction)
        else:
            print("That's not a command!")
            time.sleep(1.5)
            fishAdv.prompt()

    def guide():
        print("Fishing commands list:\n")
        print("0 = Fishing bait")
        print("   Level(s): 1, 5, 10, 25, 28, 38, 85\n")
        print("1 = Crayfish Cage")
        print("   Level(s): 1\n")
        print("2 = Small fishing net")
        print("   Level(s): 1, 5, 15, 33, 62\n")
        print("3 = Big fishing net")
        print("   Level(s): 16, 23, 46\n")
        print("4 = Fly fishing rod + feathers")
        print("   Level(s): 20, 30, 38\n")
        print("5 = Harpoon")
        print("   Level(s): 35, 50, 76\n")
        print("6 = Lobster Pot")
        print("   Level(s): 40\n")
        print("7 = Oily fishing rod")
        print("   Level(s): 53\n")
        print("8 = Karambwan vessel")
        print("   Level(s): 65\n")
        print("9 = Living minerals")
        print("   Level(s): 90")
        print("\nlist = Displays a list of all fish + level & bait needed.")
        print("\nexit = Will exit back to main menu")
        done=input("Press enter to continue")
        fishAdv.prompt()

    def list():
        print("Help will be here!")
        time.sleep(1.5)
        fishAdv.prompt()

    def fishes():
        global minnow
        global crayfish
        global shrimp
        global sardine
        global karambwanji
        global herring
        global anchovies
        global casket
        global mackerel
        global oyster
        global seaweed
        global trout
        global cod
        global pike
        global slimyeel
        global salmon
        global frogspawn
        global tuna
        global caveeel
        global rainbowfish
        global lobster
        global bass
        global swordfish
        global lavaeel
        global monkfish
        global karambwan
        global shark
        global baronshark
        global cavefish
        global rocktail
        minnow      = ["Minnow",       1,  0, 10 ]
        crayfish    = ["Crayfish",     1,  1, 10 ]
        shrimp      = ["Shrimps",      1,  2, 10 ]
        sardine     = ["Sardine",      5,  0, 20 ]
        karambwanji = ["Karambwanji",  5,  2, 5  ]
        herring     = ["Herring",      10, 0, 30 ]
        anchovies   = ["Anchovies",    15, 1, 40 ]
        casket      = ["Casket",       16, 3, 10 ]
        mackerel    = ["Mackerel",     16, 3, 20 ]
        oyster      = ["Oyster",       16, 3, 10 ]
        seaweed     = ["Seaweed",      16, 3, 1  ]
        trout       = ["Trout",        20, 4, 50 ]
        cod         = ["Cod",          23, 3, 45 ]
        pike        = ["Pike",         25, 0, 60 ]
        slimyeel    = ["Slimy eel",    28, 0, 65 ]
        salmon      = ["Salmon",       30, 4, 70 ]
        frogspawn   = ["Frog spawn",   33, 2, 75 ]
        tuna        = ["Tuna",         35, 5, 80 ]
        caveeel     = ["Cave eel",     38, 0, 80 ]
        rainbowfish = ["Rainbow fish", 38, 4, 80 ]
        lobster     = ["Lobster",      40, 6, 90 ]
        bass        = ["Bass",         46, 3, 100]
        swordfish   = ["Swordfish",    50, 5, 100]
        lavaeel     = ["Lava eel",     53, 7, 60]
        monkfish    = ["Monkfish",     62, 2, 120]
        karambwan   = ["Karambwan",    65, 8, 105]
        shark       = ["Shark",        76, 5, 110]
        baronshark  = ["Baron shark",  76, 5, 110]
        # seaturtle   = ["Sea turtle",   79, 69, 38]
        # mantaray    = ["Manta Ray",    81, 69, 46]
        cavefish    = ["Cavefish",     85, 0, 300]
        rocktail    = ["Rocktail",     90, 9, 380]
        # tigershark  = ["Tiger Shark",  95, 69, 69]
    def fish(baitSel):
        # Fish arrays
        global minnow
        global crayfish
        global shrimp
        global sardine
        global karambwanji
        global herring
        global anchovies
        global casket
        global mackerel
        global oyster
        global seaweed
        global trout
        global cod
        global pike
        global slimyeel
        global salmon
        global frogspawn
        global tuna
        global caveeel
        global rainbowfish
        global lobster
        global bass
        global swordfish
        global lavaeel
        global monkfish
        global karambwan
        global shark
        global baronshark
        global cavefish
        global rocktail
        # Other variables
        global fishAction
        global fishLevel
        global feathers
        baitCount = 10
        fishAction = baitSel
        baitType = ["bait","crayfishcage","smallnet","bignet","flyfishingrod","harpoon","lobsterpot","oilyfishingrod","karambwanvessel","livingminerals"]
        baitTypeNum = ["0","1","2","3","4","5","6","7","8","9"]
        if(str(fishAction) in baitTypeNum):
            if(fishAction == "0"):
                if(baitCount >= 1):
                    baitCount -= 1
                    if(fishLevel >= 85):
                        fishAdv.tBaits(cavefish)
                    elif(fishLevel >= 38):
                        fishAdv.tBaits(caveeel)
                    elif(fishLevel >= 28):
                        fishAdv.tBaits(slimyeel)
                    elif(fishLevel >= 25):
                        fishAdv.tBaits(pike)
                    elif(fishLevel >= 10):
                        fishAdv.tBaits(herring)
                    elif(fishLevel >= 5):
                        fishAdv.tBaits(sardine)
                    else:
                        fishAdv.tBaits(minnow)
                else:
                    print("Not enough bait!")
                fishAdv.prompt()
            elif(fishAction == "1"):
                fishAdv.tBaits(crayfish)
                fishAdv.prompt()
            elif(fishAction == "2"):
                if(fishLevel >= 62):
                    fishAdv.tBaits(monkfish)
                elif(fishLevel >= 33):
                    fishAdv.tBaits(frogspawn)
                elif(fishLevel >= 15):
                    fishAdv.tBaits(anchovies)
                elif(fishLevel >= 5):
                    fishAdv.tBaits(karambwanji)
                else:
                    fishAdv.tBaits(shrimps)
                fishAdv.prompt()
            elif(fishAction == "3"):
                if(fishLevel >= 16):
                    print("Code for Big fishing net")
                print("Code goes here! 3")
                fishAdv.prompt()
            elif(fishAction == "4"):
                if(fishLevel >= 20 & feathers >= 1):
                    print("Code for Fishing rod + feathers")
                print("Code goes here! 4")
                fishAdv.prompt()
            elif(fishAction == "5"):
                if(fishLevel >= 35):
                    print("Code for Harpoon")
                print("Code goes here! 5")
                fishAdv.prompt()
            elif(fishAction == "6"):
                if(fishLevel >= 40):
                    print("Code for Lobster pot")
                print("Code goes here! 6")
                fishAdv.prompt()
            elif(fishAction == "7"):
                if(fishLevel >= 53):
                    print("Code for Oily fishing rod")
                print("Code goes here! 7")
                fishAdv.prompt()
            elif(fishAction == "8"):
                if(fishLevel >= 65):
                    print("Code for Karambwan vessel")
                print("Code goes here! 8")
                fishAdv.prompt()
            elif(fishAction == "9"):
                if(fishLevel >= 90):
                    print("Code for Living minerals")
                print("Code goes here! 9")
                fishAdv.prompt()
            else:
                print("Invalid bait. Sorry!")
                time.sleep(1.5)
                fishAdv.prompt()
        else:
            print("You done f**ked up, mate.")
            time.sleep(1.5)
            fishAdv.prompt()

fishAdv.fishes()
fishAdv.prompt()
