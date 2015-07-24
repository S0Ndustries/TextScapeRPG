global playerHP
playerHP = 100

class healAdv:
    global itemMinnow; global itemCrayfish; global itemShrimp; global itemSardine; global itemKarambwanji; global itemHerring; global itemAnchovies; global itemMackerel; global itemTrout; global itemCod; global itemPike; global itemSlimyEel; global itemSalmon; global itemTuna; global itemCaveEel; global itemRainbowFish; global itemLobster; global itemBass; global itemSwordfish; global itemLavaEel; global itemMonkfish; global itemKarambwan; global itemShark; global itemBaronShark; global itemCavefish; global itemRocktail
    itemMinnow = ["Minnow", 000, 111, 111, 000, 0, 10, 150]; itemCrayfish = ["Crayfish", 000, 111, 111, 000, 0, 21, 200]; itemShrimp = ["Shrimp", 000, 111, 111, 000, 0, 14, 200]
    itemSardine = ["Sardine", 000, 111, 111, 000, 0, 10, 108]; itemKarambwanji = ["Karambwanji", 000, 111, 111, 000, 0, 666, 200]; itemHerring = ["Herring", 000, 111, 111, 000, 0, 10, 200]; itemAnchovies = ["Anchovies", 000, 111, 111, 000, 0, 16, 200]; itemMackerel = ["Mackeral", 000, 111, 111, 000, 0, 5, 200]; itemTrout = ["Trout", 000, 111, 111, 000, 0, 37, 300]; itemCod = ["Cod", 000, 111, 111, 000, 0, 65, 450]; itemPike = ["Pike", 000, 111, 111, 000, 0, 42, 400]; itemSlimyEel = ["Slimy eel", 000, 111, 111, 000, 0, 233, 700]; itemSalmon = ["Salmon", 000, 111, 111, 000, 0, 101, 500]; itemTuna = ["Tuna", 000, 111, 111, 000, 0, 167, 750]; itemCaveEel = ["Cave eel", 000, 111, 111, 000, 0, 160, 950]; itemRainbowFish = ["Rainbow fish", 000, 111, 111, 000, 0, 176, 875]; itemLobster = ["Lobster", 000, 111, 111, 000, 0, 252, 1200]; itemBass = ["Bass", 000, 111, 111, 000, 0, 306, 1300]; itemSwordfish = ["Swordfish", 000, 111, 111, 000, 0, 379, 1400]; itemLavaEel = ["Lava eel", 000, 111, 111, 000, 0, 666, 1060]; itemMonkfish = ["Monkfish", 000, 111, 111, 000, 0, 441, 1600]; itemKarambwan = ["Karambwan", 000, 111, 111, 000, 0, 3347, 750]; itemShark = ["Shark", 000, 111, 111, 000, 0, 817, 2000]; itemBaronShark = ["Baron shark", 000, 111, 111, 000, 1302, 2100]; itemCavefish = ["Cave fish", 000, 111, 111, 000, 0, 1827, 2000]; itemRocktail = ["Rocktail", 000, 111, 111, 000, 0, 2559, 2300]
    global doneFishList
    doneFishList = [itemMinnow, itemCrayfish, itemShrimp, itemSardine, itemKarambwanji, itemHerring, itemAnchovies, itemMackerel, itemTrout, itemCod, itemPike, itemSlimyEel, itemSalmon, itemTuna, itemCaveEel, itemRainbowFish, itemLobster, itemBass, itemSwordfish, itemLavaEel, itemMonkfish, itemKarambwan, itemShark, itemBaronShark, itemCavefish, itemRocktail]

    def prompt(m):
        global f
        f = m
        print()
        healActionList = ["food", "exit", "help"]
        print("Enter an action, type 'help' for help, or 'exit' to exit!")
        healAction=input("Heal action: ")
        if(healAction in healActionList):
            if(healAction == "food"):
                healAdv.food()
            elif(healAction == "exit"):
                game.actionPrompt()
            elif(healAction == "help"):
                healAdv.help()
        else:
            healAdv.heal(healAction)

    def heal(healAction):
        global f
        runHeal = 1
        incX = 0
        while(runHeal == 1):
            fishDone = doneFishList[incX]
            if(healAction.lower() == fishDone[0].lower()):
                if(fishDone[5] >= 1):
                    print("Healed!")
                    fishDone[5] -= 1
                    playerHP += fishDone[7]
                    go=input("Press enter to continue.")
                    runHeal = 0
                else:
                    print("\nYou don't have any %s to eat!" % fishDone[0])
                    go=input("Press enter to continue.")
                    runHeal = 0
            else:
                if(incX <= 26):
                    incX += 1
                else:
                    print("\nInvalid command, sorry!")
                    go=input("Press enter to continue.")
                    healAdv.prompt(f)
        healAdv.prompt(f)

    def food():
        global f
        print("\nYour food:")
        incY2 = 0
        dF = 1
        while(dF == 1):
            doneFood = doneFishList[incY2]
            print("    %s: %i" % (doneFood[0], doneFood[5]))
            incY2 += 1
            if(incY2 == 26):
                dF = 0
        go=input("\nPress enter to continue.")
        healAdv.prompt(f)

    def help():
        global f
        global playerHP
        print("Your health: %i\n" % playerHP)
        print("\nCommands: ")
        print("    food = Displays your food")
        print("    exit = Exits the program")
        print("    help = Displays this screen")
        print("\nOr enter a food name to heal.")
        go=input("Press enter to continue.")
        healAdv.prompt(f)

    def exit():
        global f
        if(f == 0):
            print("Action Prompt")
        else:
            print("Fight Prompt")
healAdv.prompt(0)
