import time
import os
class fishAdv():
    global fishAction
    global fishingLevel
    global feathers
    fishingLevel = 48
    feathers = 4
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
        

    def tBait(fish):



    def fish(baitSel):
        global fishAction
        global fishingLevel
        global feathers
        fishAction = baitSel
        baitType = ["bait","crayfishcage","smallnet","bignet","flyfishingrod","harpoon","lobsterpot","oilyfishingrod","karambwanvessel","livingminerals"]
        baitTypeNum = ["0","1","2","3","4","5","6","7","8","9"]
        if(str(fishAction) in baitTypeNum):
            if(fishAction == "0"):
                if(fishLevel >= 85):

                elif(fishLevel >= 38):

                elif(fishLevel >= 28):

                elif(fishLevel >= 25):

                elif(fishLevel >= 10):

                elif(fishLevel >= 5):

                else:

                fishAdv.prompt()
            elif(fishAction == "1"):
                print("Code for Crayfish cage")
                print("Code goes here! 1")
                fishAdv.prompt()
            elif(fishAction == "2"):
                print("Code for Small fishing net")
                print("Code goes here! 2")
                fishAdv.prompt()
            elif(fishAction == "3"):
                if(fishingLevel >= 16):
                    print("Code for Big fishing net")
                print("Code goes here! 3")
                fishAdv.prompt()
            elif(fishAction == "4"):
                if(fishingLevel >= 20 & feathers >= 1):
                    print("Code for Fishing rod + feathers")
                print("Code goes here! 4")
                fishAdv.prompt()
            elif(fishAction == "5"):
                if(fishingLevel >= 35):
                    print("Code for Harpoon")
                print("Code goes here! 5")
                fishAdv.prompt()
            elif(fishAction == "6"):
                if(fishingLevel >= 40):
                    print("Code for Lobster pot")
                print("Code goes here! 6")
                fishAdv.prompt()
            elif(fishAction == "7"):
                if(fishingLevel >= 53):
                    print("Code for Oily fishing rod")
                print("Code goes here! 7")
                fishAdv.prompt()
            elif(fishAction == "8"):
                if(fishingLevel >= 65):
                    print("Code for Karambwan vessel")
                print("Code goes here! 8")
                fishAdv.prompt()
            elif(fishAction == "9"):
                if(fishingLevel >= 90):
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

fishAdv.prompt()
