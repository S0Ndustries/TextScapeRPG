import time; import platform; import os
class unix:
    def clear():
        os.system('clear')
        print("<--- TextScapeRPG - by - S0Ndustries --->\n")
class windows:
    def clear():
        os.system('cls')
        print("<--- TextScapeRPG - by - S0Ndustries --->\n")
if platform.system()=="Windows":
    system = windows
else:
    system = unix


global itemClay; global itemRuneEssence; global itemCopperOre; global itemTinOre; global itemLimestone; global itemIronOre; global itemSilverOre; global itemPureEssence; global itemCoal; global itemSandstone; global itemGoldOre; global itemGranite; global itemMithrilOre; global itemAdamantOre; global itemLivingMinerals; global itemRuniteOre
itemClay = ["Clay", 111, 111, 111, 000, 0, 153, 5, 1]; itemRuneEssence = ["Rune Essence", 111, 111, 111, 000, 0, 63, 5, 1]; itemCopperOre = ["Copper", 111, 111, 111, 000, 0, 96, 17.5, 1]; itemTinOre = ["Tin", 111, 111, 111, 000, 0, 92, 17.5, 1]; itemLimestone = ["Limestone", 111, 111, 111, 000, 0, 320, 26.5, 10]; itemIronOre = ["Iron", 111, 111, 111, 000, 0, 204, 35, 15]; itemSilverOre = ["Silver", 111, 111, 111, 000, 0, 76, 40, 20]; itemPureEssence = ["Pure Essence", 111, 111, 111, 000, 0, 30, 5, 30]; itemCoal = ["Coal", 111, 111, 111, 000, 0, 365, 50, 30]; itemSandstone = ["Sandstone", 111, 111, 111, 000, 0, 16, 30, 35]; itemGoldOre = ["Gold", 111, 111, 111, 000, 0, 162, 65, 40]; itemGranite = ["Granite", 111, 111, 111, 000, 0, 230, 50, 45]; itemMithrilOre = ["Mithril", 111, 111, 111, 000, 0, 231, 80, 55]; itemAdamantOre = ["Adamant", 111, 111, 111, 000, 0, 1227, 95, 70]; itemLivingMinerals = ["Living minerals", 111, 111, 111, 000, 0, 241, 25, 73]; itemRuniteOre = ["Runite", 111, 111, 111, 000, 0, 10372, 125, 85]
global oreList
oreList = [itemClay, itemRuneEssence, itemCopperOre, itemTinOre, itemLimestone, itemIronOre, itemSilverOre, itemPureEssence, itemCoal, itemSandstone, itemGoldOre, itemGranite, itemMithrilOre, itemAdamantOre, itemLivingMinerals, itemRuniteOre]

global itemNullFiller; itemNullFiller = ["Null Filler Item", 111, 111, 111, 000, 1337]

global itemUncutHydrix; itemUncutHydrix = ["Uncut Hydrix", 111, 111, 111, 000, 0, 13356199]
global itemUncutOnyx; itemUncutOnyx = ["Uncut Onyx", 111, 111, 111, 000, 0, 1126129]
global itemUncutDragonstone; itemUncutDragonstone = ["Uncut Dragonstone", 111, 111, 111, 000, 0, 12840]
global itemUncutDiamond; itemUncutDiamond = ["Uncut Diamond", 111, 111, 111, 000, 0, 3971]
global itemUncutRuby; itemUncutRuby = ["Uncut Ruby", 111, 111, 111, 000, 0, 2239]
global itemUncutEmerald; itemUncutEmerald = ["Uncut Emerald", 111, 111, 111, 000, 0, 1462]
global itemUncutSapphire; itemUncutSapphire = ["Uncut Sapphire", 111, 111, 111, 000, 0, 690]
global itemUncutRedTopaz; itemUncutRedTopaz = ["Uncut Red Topaz", 111, 111, 111, 000, 0, 1059]
global itemUncutJade; itemUncutJade = ["Uncut Jade", 111, 111, 111, 000, 0, 398]
global itemUncutOpal;itemUncutOpal = ["Uncut Opal", 111, 111, 111, 000, 0, 509]
uncutGemList = [itemUncutHydrix, itemUncutOnyx, itemUncutDragonstone, itemUncutDiamond, itemUncutRuby, itemUncutEmerald, itemUncutSapphire, itemUncutRedTopaz, itemUncutJade, itemUncutOpal]

global itemHydrix; itemHydrix = ["Hydrix", 111, 111, 111, 000, 0, 19538637, 197.5, 79]
global itemOnyx; itemOnyx = ["Onyx", 111, 111, 111, 000, 0, 1135644, 167.5, 67]
global itemDragonstone; itemDragonstone = ["Dragonstone", 111, 111, 111, 000, 0, 9468, 137.5, 55]
global itemDiamond; itemDiamond = ["Diamond", 111, 111, 111, 000, 0, 1825, 107.5, 43]
global itemRuby; itemRuby = ["Ruby", 111, 111, 111, 000, 0, 911, 85, 34]
global itemEmerald; itemEmerald = ["Emerald", 111, 111, 111, 000, 0, 673, 67.5, 27]
global itemSapphire; itemSapphire = ["Sapphire", 111, 111, 111, 000, 0, 191, 50, 20]
global itemRedTopaz; itemRedTopaz = ["Red Topaz", 111, 111, 111, 000, 0, 659, 25, 16]
global itemJade; itemJade = ["Jade", 111, 111, 111, 000, 0, 290, 20, 13]
global itemOpal; itemOpal = ["Opal", 111, 111, 111, 000, 0, 182, 15, 1]
gemList = [itemHydrix, itemOnyx, itemDragonstone, itemDiamond, itemRuby, itemEmerald, itemSapphire, itemRedTopaz, itemJade, itemOpal]

global buildLevel; buildLevel = 1
global buildEXP; buildEXP = 0

class game:
    def actionPrompt():
        print("Bye!")

class build:
    def prompt():
        system.clear()
        print(":: Building Station :: | Level: %i" % buildLevel)
        print("Type 'smelt', 'craft', 'smelt', 'fletch', 'help', or 'exit'")
        buildAction=input("Building action: ")
        if(buildAction.lower() == "help"):
            build.help()
        elif(buildAction.lower() == "exit"):
            game.actionPrompt()
        elif(buildAction.lower() == "craft"):
            craft.prompt()
        elif(buildAction.lower() == "smelt"):
            smelt.prompt()
        elif(buildAction.lower() == "smith"):
            smith.prompt()
        elif(buildAction.lower() == "fletch"):
            fletch.prompt()
        else:
            print("\nInvalid action: %s" % buildAction)
            go=input("Press enter to continue")
            build.prompt()
    def help():
        print("Building help")
        print("'craft'  = Displays crafting interface")
        print("'smelt'  = Displays smelting interface")
        print("'smith'  = Displays smithing interface")
        print("'fletch' = Displays fletching interface")
        print("'help'   = Displays this interface")
        print("'exit'   = Exits back to the main prompt")
        go=input("\nPress enter to continue.")
        build.prompt()

class smelt:
    def prompt():
        system.clear()
        print("** Blacksmith Workshop **")
        print("Enter an item to smelt, or try 'help' / exit'")
        smeltAction=input("Smelting action: ")
        if(smeltAction.lower() == "bars" or smeltAction.lower() == "list"):
            smelt.barList()
        elif(smeltAction.lower() == "help"):
            smelt.help()
        elif(smeltAction.lower() == "exit"):
            build.prompt()
        else:
            smelt.smeltBar(smeltAction)
    def smeltBar(barType):
        global buildEXP
        global buildLevel
        runLoop = 1
        x = 0
        smeltBar = barList[x]
        while(runLoop == 1):
            if(barType.lower() == smeltBar[0].lower()):
                if(buildLevel >= smeltBar[8]):
                    primaryOre = smeltBar[9]
                    secondaryOre = smeltBar[10]
                    if(primaryOre[5] >= 1):
                        if(secondaryOre[5] >= smeltBar[11]):
                            primaryOre[5] -= 1
                            secondaryOre[5] -= smeltBar[11]
                            smeltBar[5] += 1
                            buildEXP += smeltBar[7]
                            print("\nYou have smelted %s and earned + %0.1f XP!" % (smeltBar[0], smeltBar[7]))
                            go=input("Press enter to continue.")
                            smelt.prompt()
                        else:
                            print("\nYou need at least 1 %s & %i %s to do that!" % (primaryOre[0], smeltBar[11], secondaryOre[0]))
                            print("You have: %i %s & %i %s" % (primaryOre[5], primaryOre[0], secondaryOre[5], secondaryOre[0]))
                            go=input("Press enter to continue")
                            smelt.prompt()
                    else:
                        print("\nYou need at least 1 %s & %i %s to do that!" % (primaryOre[0], smeltBar[11], secondaryOre[0]))
                        print("You have: %i %s & %i %s" % (primaryOre[5] , primaryOre[0], secondaryOre[5], secondaryOre[0]))
                        go=input("Press enter to continue")
                        smelt.prompt()
                else:
                    print("\nNot high enough level! Required level: %i" % smeltBar[8])
                    go=input("Press enter to continue.")
                    smelt.prompt()
            else:
                if(x < len(barList)):
                    x += 1
                    smeltBar = barList[x - 1]
                else:
                    runLoop = 0
        else:
            print("\nInvalid action: %s. Try 'help'" % barType)
            go=input("Press enter to continue.")
            smelt.prompt()
        print(len(oreList))
        print(barType)
        time.sleep(5)
    def help():
        print("Smithing help:\n")
        print("'bars' = Lists bars")
        print("'help' = Displays this interface")
        print("'exit = Exits back to crafting prompt'")
        go=input("\nPress enter to continue.")
        smelt.prompt()
    def barList():
        print("\nBar list:\n")
        x = 0
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Bronze Bar      - Level: %i  | XP: %0.1f  | Requires: 1 %s ore & %i %s ore" % (barNow[8], barNow[7], primaryOre[0], barNow[11], secondaryOre[0]))
        x += 1; print("----------------------------+----------+--------->")
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Iron Bar        - Level: %i | XP: %0.1f | Requires: 1 %s ore" % (barNow[8], barNow[7], primaryOre[0]))
        x += 1; print("----------------------------+----------+--------->")
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Silver Bar      - Level: %i | XP: %0.1f | Requires: 1 %s ore" % (barNow[8], barNow[7], primaryOre[0]))
        x += 1; print("----------------------------+----------+--------->")
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Steel Bar       - Level: %i | XP: %0.1f | Requires: 1 %s ore & %i %s" % (barNow[8], barNow[7], primaryOre[0], barNow[11], secondaryOre[0]))
        x += 1; print("----------------------------+----------+--------->")
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Gold Bar        - Level: %i | XP: %0.1f | Requires: 1 %s ore" % (barNow[8], barNow[7], primaryOre[0]))
        x += 1; print("----------------------------+----------+--------->")
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Mithril Bar     - Level: %i | XP: %0.1f | Requires: 1 %s ore & %i %s" % (barNow[8], barNow[7], primaryOre[0], barNow[11], secondaryOre[0]))
        x += 1; print("----------------------------+----------+--------->")
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Adamant Bar     - Level: %i | XP: %0.1f | Requires: 1 %s ore & %i %s" % (barNow[8], barNow[7], primaryOre[0], barNow[11], secondaryOre[0]))
        x += 1; print("----------------------------+----------+--------->")
        barNow = barList[x]
        primaryOre = barNow[9]; secondaryOre = barNow[10]
        print("Runite Bar      - Level: %i | XP: %0.1f | Requires: 1 %s ore & %i %s" % (barNow[8], barNow[7], primaryOre[0], barNow[11], secondaryOre[0]))

        go=input("\nPress enter to continue.")
        smelt.prompt()

class craft:
    global buildLevel
    global buildEXP
    def prompt():
        system.clear()
        print("== Crafting Workshop == | Level: %i" % buildLevel)
        print("Enter an item to craft, or try 'help' / exit'")
        craftAction=input("Crafting action: ")
        if(craftAction.lower() == "gems" or craftAction.lower() == "list"):
            craft.gemList()
        elif(craftAction.lower() == "help"):
            craft.help()
        elif(craftAction.lower() == "exit"):
            build.prompt()
        else:
            craft.craftGems(craftAction)
    def craftGems(gemType):
        global buildEXP
        global buildLevel
        runLoop = 1
        x = 0
        uncutGem = uncutGemList[x]
        cutGem = gemList[x]
        while(runLoop == 1):
            if(gemType.lower() == uncutGem[0].lower() or gemType.lower() == cutGem[0].lower()):
                if(buildLevel >= cutGem[8]):
                    if(uncutGem[5] >= 1):
                        uncutGem[5] -= 1
                        cutGem[5] += 1
                        buildEXP += cutGem[7]
                        print("\nYou have crafted %s and earned + %0.1f XP!" % (cutGem[0], cutGem[7]))
                        go=input("Press enter to continue.")
                        craft.prompt()
                    else:
                        print("\nYou need at least 1 %s & to do that!" % uncutGem[0])
                        print("You have: %i %s" % (uncutGem[5], uncutGem[0]))
                        go=input("Press enter to continue")
                        craft.prompt()
                else:
                    print("\nNot high enough level! Required level: %i" % cutGem[8])
                    go=input("Press enter to continue.")
                    craft.prompt()
            else:
                if(x < len(gemList)):
                    x += 1
                    uncutGem = uncutGemList[x - 1]
                    cutGem = gemList[x - 1]
                else:
                    runLoop = 0
        else:
            print("\nInvalid action: %s. Try 'help'" % gemType)
            go=input("Press enter to continue.")
            craft.prompt()

    def help():
        print("Crafting help:\n")
        print("'gems' = Lists gems")
        print("'help' = Displays this interface")
        print("'exit = Exits back to crafting prompt'")
        go=input("\nPress enter to continue.")
        craft.prompt()
    def gemList():
        print("\nBar list:\n")
        x = len(gemList) - 1
        gemNow = gemList[x]
        print("Opal            - Level: %i  | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Jade            - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Red Topaz       - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Sapphire        - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Emerald         - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Ruby            - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Diamond         - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Dragonstone     - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Onyx            - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))
        x -= 1; print("----------------------------+---------->")
        gemNow = gemList[x]
        print("Hydrix          - Level: %i | XP: %0.1f" % (gemNow[8], gemNow[7]))

        go=input("\nPress enter to continue.")
        craft.prompt()

class smith:
    def prompt():
        print("** Blacksmith Workshop **")
        print("Enter an item to smith, or try 'help' / exit'")
        smithAction=input("Smithing action: ")
        if(smithAction.lower() == "ores"):
            smith.oreList()
        elif(smithAction.lower() == "help"):
            smith.help()
        elif(smithAction.lower() == "exit"):
            game.actionPrompt()
        else:
            print("Invalid action")
            go=input("Press enter to continue.")
            smith.prompt()
    def help():
        print("Smithing help:\n")
        print("'ores' = Lists ores")
        print("'help' = Displays this interface")
        print("'exit = Exits back to crafting prompt'")
        go=input("\nPress enter to continue.")
        craft.smith()
    def oreList():
        print("Clay            - Level: %i  | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Rune Essence    - Level: %i  | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Copper          - Level: %i  | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Tin             - Level: %i  | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Limestone       - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Iron            - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Silver          - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Pure Essence    - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Coal            - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Sandstone       - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Gold            - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Granite         - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Mithril         - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Adamant         - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Living minerals - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))
        x += 1
        print("Runite          - Level: %i | XP: %i" % (oreNow[7], oreNow[8]))

class fletch:
    def prompt():
        print("Fletch")

build.prompt()
