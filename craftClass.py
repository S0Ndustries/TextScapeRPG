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

global craftLevel; craftLevel = 1
global craftEXP; craftEXP = 0

class game:
    def actionPrompt():
        print("Bye!")

class craft:
    def prompt():
        print(":: Crafting Station :: | Level: %i" % craftLevel)
        print("Enter type of crafting, or try 'help' / 'exit'")
        craftAction=input("Crafting action: ")
        if(craftAction.lower() == "help"):
            craft.help()
        if(craftAction.lower() == "exit"):
            game.actionPrompt()
        if(craftAction.lower() == "smith"):
            craft.smith()
        if(craftAction.lower() == "fletch"):
            craft.fletch()
        else:
            print("Invalid action!")
            go=input("Press enter to continue")
            craft.prompt()

    def help():
        print("Crafting help")
        print("'smith' = Opens smithing interface")
        print("'fletch' = Opens fletching interface")
        print("'help' = Displays this interface")
        print("'exit' = Exits back to the main prompt")
        print("\nMore to come soon!")
        print("\nOr enter an ore type to mine it.")
    def exit():
        game.actionPrompt()
    def smith():
        print("** Blacksmith Workshop **")
        print("Enter an item to smelt, or try 'help' / exit'")
        smithAction=input("Smithing action: ")
        if(smithAction == ("ores" or "list") ):
            x = 1
            while(x == 0):
                print("Hi")
        elif(smithAction.lower() == "help"):
            print("Smithing help:\n")
            print("'ores' = Lists ores")
            print("'help' = Displays this interface")
            print("'exit = Exits back to crafting prompt'")
            go=input("\nPress enter to continue.")
            craft.smith()
        elif(smithAction.lower() == "exit"):
            game.actionPrompt()

    def fletch():
        print("Fletch")

craft.prompt()
