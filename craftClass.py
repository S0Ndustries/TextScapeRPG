import time

global itemClay; global itemRuneEssence; global itemCopperOre; global itemTinOre; global itemLimestone; global itemIronOre; global itemSilverOre; global itemPureEssence; global itemCoal; global itemSandstone; global itemGoldOre; global itemGranite; global itemMithrilOre; global itemAdamantOre; global itemLivingMinerals; global itemRuniteOre
itemClay = ["Clay", 111, 111, 111, 000, 0, 153, 5, 1]; itemRuneEssence = ["Rune Essence", 111, 111, 111, 000, 0, 63, 5, 1]; itemCopperOre = ["Copper", 111, 111, 111, 000, 0, 96, 17.5, 1]; itemTinOre = ["Tin", 111, 111, 111, 000, 0, 92, 17.5, 1]; itemLimestone = ["Limestone", 111, 111, 111, 000, 0, 320, 26.5, 10]; itemIronOre = ["Iron", 111, 111, 111, 000, 0, 204, 35, 15]; itemSilverOre = ["Silver", 111, 111, 111, 000, 0, 76, 40, 20]; itemPureEssence = ["Pure Essence", 111, 111, 111, 000, 0, 30, 5, 30]; itemCoal = ["Coal", 111, 111, 111, 000, 0, 365, 50, 30]; itemSandstone = ["Sandstone", 111, 111, 111, 000, 0, 16, 30, 35]; itemGoldOre = ["Gold", 111, 111, 111, 000, 0, 162, 65, 40]; itemGranite = ["Granite", 111, 111, 111, 000, 0, 230, 50, 45]; itemMithrilOre = ["Mithril", 111, 111, 111, 000, 0, 231, 80, 55]; itemAdamantOre = ["Adamant", 111, 111, 111, 000, 0, 1227, 95, 70]; itemLivingMinerals = ["Living minerals", 111, 111, 111, 000, 0, 241, 25, 73]; itemRuniteOre = ["Runite", 111, 111, 111, 000, 0, 10372, 125, 85]
global oreList
oreList = [itemClay, itemRuneEssence, itemCopperOre, itemTinOre, itemLimestone, itemIronOre, itemSilverOre, itemPureEssence, itemCoal, itemSandstone, itemGoldOre, itemGranite, itemMithrilOre, itemAdamantOre, itemLivingMinerals, itemRuniteOre]

global itemNullFiller; itemNullFiller = ["Null Filler Item", 111, 111, 111, 000, 1337]

global itemUncutOnyx; itemUncutOnyx = ["Uncut Onyx", 111, 111, 111, 000, 0, 1117368]
global itemUncutDragonstone; itemUncutDragonstone = ["Uncut Dragonstone", 111, 111, 111, 000, 0, 12,970]
global itemUncutDiamond; itemUncutDiamond = ["Uncut Diamond", 111, 111, 111, 000, 0, 4018]
global itemUncutRuby; itemUncutRuby = ["Uncut Ruby", 111, 111, 111, 000, 0, 2132]
global itemUncutEmerald; itemUncutEmerald = ["Uncut Emerald", 111, 111, 111, 000, 0, 1440]
global itemUncutSapphire; itemUncutSapphire = ["Uncut Sapphire", 111, 111, 111, 000, 0, 707]
global itemUncutRedTopaz; itemUncutRedTopaz = ["Uncut Red Topaz", 111, 111, 111, 000, 0, 1014]
global itemUncutJade; itemUncutJade = ["Uncut Jade", 111, 111, 111, 000, 0, 408]
global itemUncutOpal; itemUncutOpal = ["Uncut Opal", 111, 111, 111, 000, 0, 489]
gemList = [itemUncutOnyx, itemUncutDragonstone, itemUncutDiamond, itemUncutRuby, itemUncutEmerald, itemUncutSapphire]

global itemBronzeBar; itemBronzeBar = ["Bronze bar", 111, 111, 111, 000, 0, 283, 6.2, 1, itemCopperOre, itemTinOre, 1]
global itemIronBar; itemIronBar = ["Iron bar", 111, 111, 111, 000, 0, 347, 12.5, 15, itemIronOre, itemNullFiller, 0]
global itemSilverBar; itemSilverBar = ["Silver bar", 111, 111, 111, 000, 0, 138, 13.7, 20, itemSilverOre, itemNullFiller, 0]
global itemSteelBar;itemSteelBar = ["Steel bar", 111, 111, 111, 000, 0, 809, 17.5, 30, itemIronOre, itemCoal, 2]
global itemGoldBar; itemGoldBar = ["Gold bar", 111, 111, 111, 000, 0, 90, 22.5, 40, itemGoldOre, itemNullFiller, 0]
global itemMithrilBar; itemMithrilBar = ["Mithril bar", 111, 111, 111, 000, 0, 1358, 30, 50, itemMithrilOre, itemCoal, 4]
global itemAdamantBar; itemAdamantBar = ["Adamant bar", 111, 111, 111, 000, 0, 2559, 37.5, 70, itemAdamantOre, itemCoal, 6]
global itemRuneBar; itemRuneBar = ["Rune bar", 111, 111, 111, 000, 0, 14214, 50, 85, itemRuniteOre, itemCoal, 8]
barList = [itemBronzeBar, itemIronBar, itemSilverBar, itemSteelBar, itemGoldBar, itemMithrilBar, itemAdamantBar, itemRuneBar]

global buildLevel; buildLevel = 1
global buildEXP; buildEXP = 0

class game:
    def actionPrompt():
        print("Bye!")

class build:
    def prompt():
        print(":: Building Station :: | Level: %i" % buildLevel)
        print("Enter type of building, or try 'help' / 'exit'")
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
            print("Invalid action: %s" % buildAction)
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

class craft:
    def craft():
        print("Hi")
class smelt:
    def prompt():
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
        x = 1
        smeltBar = barList[x - 1]
        while(x < len(oreList)):
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
                            print("You have smelted %s and earned + %0.1f XP!" % (smeltBar[0], smeltBar[7]))
                        else:
                            print("You need at least 1 %s & %i %s to do that!" % (primaryOre[0], smeltBar[11], secondaryOre[0]))
                            print("You have: %i %s & %i %s" % (primaryOre[5], primaryOre[0], secondaryOre[5], secondaryOre[0]))
                            go=input("Press enter to continue")
                            smelt.prompt()
                    else:
                        print("You need at least 1 %s & %i %s to do that!" % (primaryOre[0], smeltBar[11], secondaryOre[0]))
                        print("You have: %i %s & %i %s" % (primaryOre[5] , primaryOre[0], secondaryOre[5], secondaryOre[0]))
                        go=input("Press enter to continue")
                        smelt.prompt()
                else:
                    print("\nNot high enough level! Required level: %i" % smeltBar[8])
                    go=input("\nPress enter to continue.")
                    smelt.prompt()
            else:
                x += 1
                smeltBar = barList[x - 1]
        else:
            print("\nInvalid action: %s " % barType)
            go=input("Press enter to continue.")
            smelt.prompt()
        print(len(oreList))
        print(barType)
        time.sleep(5)
    def help():
        print("Smithing help:\n")
        print("'ores' = Lists ores")
        print("'help' = Displays this interface")
        print("'exit = Exits back to crafting prompt'")
        go=input("\nPress enter to continue.")
        craft.smith()
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
        smith.prompt()

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
