class game:
    def myEXP(iEXP):
        global exp
        global level
        exp = iEXP
        if(exp < 83):
            level = 1
        elif(exp < 174):
            level = 2
        elif(exp < 276):
            level = 3
        elif(exp < 388):
            level = 4
        elif(exp < 512):
            level = 5
        elif(exp < 650):
            level = 6
        elif(exp < 801):
            level = 7
        elif(exp < 969):
            level = 8
        elif(exp < 1154):
            level = 9
        elif(exp < 1358):
            level = 10
        elif(exp < 1584):
            level = 11
        elif(exp < 1833):
            level = 12
        elif(exp < 2107):
            level = 13
        elif(exp < 2411):
            level = 14
        elif(exp < 2746):
            level = 15
        elif(exp < 3115):
            level = 16
        elif(exp < 3523):
            level = 17
        elif(exp < 3973):
            level = 18
        elif(exp < 4470):
            level = 19
        elif(exp < 5018):
            level = 20
        elif(exp < 5624):
            level = 21
        elif(exp < 6291):
            level = 22
        elif(exp < 7028):
            level = 23
        elif(exp < 7842):
            level = 24
        elif(exp < 8740):
            level = 25
        elif(exp < 9730):
            level = 26
        elif(exp < 10824):
            level = 27
        elif(exp < 12031):
            level = 28
        elif(exp < 13363):
            level = 29
        elif(exp < 14833):
            level = 30
        elif(exp < 16456):
            level = 31
        elif(exp < 18247):
            level = 32
        elif(exp < 20224):
            level = 33
        elif(exp < 22406):
            level = 34
        elif(exp < 24815):
            level = 35
        elif(exp < 27473):
            level = 36
        elif(exp < 30408):
            level = 37
        elif(exp < 33648):
            level = 38
        elif(exp < 37224):
            level = 39
        elif(exp < 41171):
            level = 40
        elif(exp < 45529):
            level = 41
        elif(exp < 50339):
            level = 42
        elif(exp < 55649):
            level = 43
        elif(exp < 61512):
            level = 44
        elif(exp < 67983):
            level = 45
        elif(exp < 75127):
            level = 46
        elif(exp < 83014):
            level = 47
        elif(exp < 91721):
            level = 48
        elif(exp < 101333):
            level = 49
        elif(exp < 111945):
            level = 50
        elif(exp < 123660):
            level = 51
        elif(exp < 136594):
            level = 52
        elif(exp < 150872):
            level = 53
        elif(exp < 166636):
            level = 54
        elif(exp < 184040):
            level = 55
        elif(exp < 203254):
            level = 56
        elif(exp < 224466):
            level = 57
        elif(exp < 247886):
            level = 58
        elif(exp < 273742):
            level = 59
        elif(exp < 302288):
            level = 60
        elif(exp < 333804):
            level = 61
        elif(exp < 368599):
            level = 62
        elif(exp < 407015):
            level = 63
        elif(exp < 449428):
            level = 64
        elif(exp < 496254):
            level = 65
        elif(exp < 547953):
            level = 66
        elif(exp < 605032):
            level = 67
        elif(exp < 668051):
            level = 68
        elif(exp < 737627):
            level = 69
        elif(exp < 814445):
            level = 70
        elif(exp < 899257):
            level = 71
        elif(exp < 992895):
            level = 72
        elif(exp < 1096278):
            level = 73
        elif(exp < 1210421):
            level = 74
        elif(exp < 1336443):
            level = 75
        elif(exp < 1475581):
            level = 76
        elif(exp < 1629200):
            level = 77
        elif(exp < 1798808):
            level = 78
        elif(exp < 1986068):
            level = 79
        elif(exp < 2192818):
            level = 80
        elif(exp < 2421087):
            level = 81
        elif(exp < 2673114):
            level = 82
        elif(exp < 2951373):
            level = 83
        elif(exp < 3258594):
            level = 84
        elif(exp < 3597792):
            level = 85
        elif(exp < 3972294):
            level = 86
        elif(exp < 4385776):
            level = 87
        elif(exp < 4842295):
            level = 88
        elif(exp < 5346332):
            level = 89
        elif(exp < 5902831):
            level = 90
        elif(exp < 6517253):
            level = 91
        elif(exp < 7195629):
            level = 92
        elif(exp < 7944614):
            level = 93
        elif(exp < 8771558):
            level = 94
        elif(exp < 9684577):
            level = 95
        elif(exp < 10692629):
            level = 96
        elif(exp < 11805606):
            level = 97
        elif(exp < 13034431):
            level = 98
        elif(exp < 14391160):
            level = 99
        else:
            level = 99
    def actionPrompt():
        print("Bye!")

global cookEXP
global cookLevel
cookEXP = 0
cookLevel = 1
global loadCTime
loadCTime = 0.2 / ((cookLevel * 0.005) + 0.995)
class cookAdv:
    global itemRAWMinnow; global itemRAWCrayfish; global itemRAWShrimp; global itemRAWSardine; global itemRAWKarambwanji; global itemRAWHerring; global itemRAWAnchovies; global itemRAWMackerel; global itemRAWSeaweed; global itemRAWTrout; global itemRAWCod; global itemRAWPike; global itemRAWSlimyEel; global itemRAWSalmon; global itemRAWFrogSpawn; global itemRAWTuna; global itemRAWCaveEel; global itemRAWRainbowFish; global itemRAWLobster; global itemRAWBass; global itemRAWSwordfish; global itemRAWLavaEel; global itemRAWMonkfish; global itemRAWKarambwan; global itemRAWShark; global itemRAWBaronShark; global itemRAWCavefish; global itemRAWRocktail
    itemRAWMinnow = ["Raw Minnow", 111, 000, 111, 000, 0]; itemRAWCrayfish = ["Raw Crayfish", 111, 000, 111, 000, 0]; itemRAWShrimp = ["Raw Shrimp", 111, 000, 111, 000, 0]; itemRAWSardine = ["Raw Sardine", 111, 000, 111, 000, 0]; itemRAWKarambwanji = ["Raw Karambwanji", 111, 000, 111, 000, 0]; itemRAWHerring = ["Raw Herring", 111, 000, 111, 000, 0]; itemRAWAnchovies = ["Raw Anchovies", 111, 000, 111, 000, 0]; itemRAWMackerel = ["Raw Mackerel", 111, 000, 111, 000, 0]; itemRAWSeaweed = ["Raw Seaweed", 111, 000, 111, 000, 0]; itemRAWTrout = ["Raw Trout", 111, 000, 111, 000, 0]; itemRAWCod = ["Raw Cod", 111, 000, 111, 000, 0]; itemRAWPike = ["Raw Pike", 111, 000, 111, 000, 0]; itemRAWSlimyEel = ["Raw Slimy eel", 111, 000, 111, 000, 0]; itemRAWSalmon = ["Raw Salmon", 111, 000, 111, 000, 0]; itemRAWFrogSpawn = ["Raw Frog spawn", 111, 000, 111, 000, 0]; itemRAWTuna = ["Raw Tuna", 111, 000, 111, 000, 0]; itemRAWCaveEel = ["Raw Cave eel", 111, 000, 111, 000, 0]; itemRAWRainbowFish = ["Raw Rainbow fish", 111, 000, 111, 000, 0]; itemRAWLobster = ["Raw Lobster", 111, 000, 111, 000, 0]; itemRAWBass = ["Raw Bass", 111, 000, 111, 000, 0]; itemRAWSwordfish = ["Raw Swordfish", 111, 000, 111, 000, 0]; itemRAWLavaEel = ["Raw Lava eel", 111, 000, 111, 000, 0]; itemRAWMonkfish = ["Raw Monkfish", 111, 000, 111, 000, 0]; itemRAWKarambwan = ["Raw Karambwan", 111, 000, 111, 000, 0]; itemRAWShark = ["Raw Shark", 111, 000, 111, 000, 0]; itemRAWBaronShark = ["Raw Baron shark", 111, 000, 111, 000, 0]; itemRAWCavefish = ["Raw Cave fish", 111, 000, 111, 000, 0]; itemRAWRocktail = ["Raw Rocktail", 111, 000, 111, 000, 0]
    global rawFishList
    rawFishList = [itemRAWMinnow, itemRAWCrayfish, itemRAWShrimp, itemRAWSardine, itemRAWKarambwanji, itemRAWHerring, itemRAWAnchovies, itemRAWMackerel, itemRAWSeaweed, itemRAWTrout, itemRAWCod, itemRAWPike, itemRAWSlimyEel, itemRAWSalmon, itemRAWFrogSpawn, itemRAWTuna, itemRAWCaveEel, itemRAWRainbowFish, itemRAWLobster, itemRAWBass, itemRAWSwordfish, itemRAWLavaEel, itemRAWMonkfish, itemRAWKarambwan, itemRAWShark, itemRAWBaronShark, itemRAWCavefish, itemRAWRocktail]
    # Cooked items
    global itemMinnow; global itemCrayfish; global itemShrimp; global itemSardine; global itemKarambwanji; global itemHerring; global itemAnchovies; global itemMackerel; global itemSeaweed; global itemTrout; global itemCod; global itemPike; global itemSlimyEel; global itemSalmon; global itemFrogSpawn; global itemTuna; global itemCaveEel; global itemRainbowFish; global itemLobster; global itemBass; global itemSwordfish; global itemLavaEel; global itemMonkfish; global itemKarambwan; global itemShark; global itemBaronShark; global itemCavefish; global itemRocktail
    itemMinnow = ["Minnow", 000, 111, 111, 000, 0]; itemCrayfish = ["Crayfish", 000, 111, 111, 000, 0]; itemShrimp = ["Shrimp", 000, 111, 111, 000, 0]; itemSardine = ["Sardine", 000, 111, 111, 000, 0]; itemKarambwanji = ["Karambwanji", 000, 111, 111, 000, 0]; itemHerring = ["Herring", 000, 111, 111, 000, 0]; itemAnchovies = ["Anchovies", 000, 111, 111, 000, 0]; itemMackerel = ["Mackeral", 000, 111, 111, 000, 0]; itemSeaweed = ["Seaweed", 000, 111, 111, 000, 0]; itemTrout = ["Trout", 000, 111, 111, 000, 0]; itemCod = ["Cod", 000, 111, 111, 000, 0]; itemPike = ["Pike", 000, 111, 111, 000, 0]; itemSlimyEel = ["Slimy eel", 000, 111, 111, 000, 0]; itemSalmon = ["Salmon", 000, 111, 111, 000, 0]; itemFrogSpawn = ["Frog spawn", 000, 111, 111, 000, 0]; itemTuna = ["Tuna", 000, 111, 111, 000, 0]; itemCaveEel = ["Cave eel", 000, 111, 111, 000, 0]; itemRainbowFish = ["Rainbow fish", 000, 111, 111, 000, 0]; itemLobster = ["Lobster", 000, 111, 111, 000, 0]; itemBass = ["Bass", 000, 111, 111, 000, 0]; itemSwordfish = ["Swordfish", 000, 111, 111, 000, 0]; itemLavaEel = ["Lava eel", 000, 111, 111, 000, 0]; itemMonkfish = ["Monkfish", 000, 111, 111, 000, 0]; itemKarambwan = ["Karambwan", 000, 111, 111, 000, 0]; itemShark = ["Shark", 000, 111, 111, 000, 0]; itemBaronShark = ["Baron shark", 000, 111, 111, 000, 0]; itemCavefish = ["Cave fish", 000, 111, 111, 000, 0]; itemRocktail = ["Rocktail", 000, 111, 111, 000, 0]
    global doneFishList
    doneFishList = [itemMinnow, itemCrayfish, itemShrimp, itemSardine, itemKarambwanji, itemHerring, itemAnchovies, itemMackerel, itemSeaweed, itemTrout, itemCod, itemPike, itemSlimyEel, itemSalmon, itemFrogSpawn, itemTuna, itemCaveEel, itemRainbowFish, itemLobster, itemBass, itemSwordfish, itemLavaEel, itemMonkfish, itemKarambwan, itemShark, itemBaronShark, itemCavefish, itemRocktail]

    global cookLevel
    global cookEXP

    def prompt():
        print()
        cookActionList = ["food", "stats", "exit", "help"]
        global rawFishList
        global doneFishList
        print("Enter an action, type 'help' for help, or 'exit' to exit!")
        cookAction=input("Cook action: ")
        if(cookAction in cookActionList):
            if(cookAction == "food"):
                cookAdv.food()
            elif(cookAction == "stats"):
                cookAdv.stats()
            elif(cookAction == "exit"):
                game.actionPrompt()
            elif(cookAction == "help"):
                cookAdv.help()
        else:
            cookAdv.cook(cookAction)

    def cook(cookAction):
        runCook = 1
        incX = 0
        while(runCook == 1):
            fishCook = rawFishList[incX]
            fishDone = doneFishList[incX]
            if(cookAction.lower() == fishDone[0].lower()):
                if(fishCook[5] >= 1):
                    print("Cooked: %s!" % fishCook[0])
                    fishCook[5] -= 1
                    fishDone[5] += 1
                    go=input("Press enter to continue.")
                    runCook = 0
                else:
                    print("\nYou don't have any %s to cook!" % fishCook[0])
                    go=input("Press enter to continue.")
                    runCook = 0
            else:
                if(incX <= 26):
                    incX += 1
                else:
                    print("\nInvalid command, sorry!")
                    go=input("Press enter to continue.")
                    cookAdv.prompt()
        cookAdv.prompt()
    def loadBar():
        global cookedLevel
        global loadCTime
        loadCTime = 0.2 / ((cookLevel * 0.1 * 0.005) + 0.995)
        s = "[==========]"
        for c in s:
            sys.stdout.write('%s' % c )
            sys.stdout.flush()
            time.sleep(loadCTime)

    def food():
        print("\nRaw food:")
        incY1 = 0
        rF = 1
        while(rF == 1):
            rawFood = rawFishList[incY1]
            print("    %s: %i" % (rawFood[0], rawFood[5]))
            incY1 += 1
            if(incY1 == 28):
                rF = 0
        print("\nCooked food:")
        incY2 = 0
        dF = 1
        while(dF == 1):
            doneFood = doneFishList[incY2]
            print("    %s: %i" % (doneFood[0], doneFood[5]))
            incY2 += 1
            if(incY2 == 28):
                dF = 0
        go=input("\nPress enter to continue.")
        cookAdv.prompt()
    def help():
        print("\nCommands: ")
        print("    food = Displays your raw & cooked foods")
        print("    stats = Displays cooking statistics")
        print("    exit = Exits the program")
        print("    help = Displays this screen")
        print("\nOr enter a fish name to cook it.")
        go=input("Press enter to continue.")
        cookAdv.prompt()
    def stats():
        global cookEXP
        global cookLevel
        global exp
        global level
        global loadCTime
        game.myEXP(cookEXP)
        cookLevel = level
        print("\nYour cooking XP amount is: %i" % cookEXP)
        print("Your cooking level is now: %i" % cookLevel)
        print("You take: %s seconds to cook food!" % (loadCTime * 12))
        rexturn = input("\nPress enter to return")
        cookAdv.prompt()
    def firstStats():
        global cookEXP
        global cookLevel
        global exp
        global level
        game.myEXP(cookEXP)
        cookLevel = level
cookAdv.prompt()
