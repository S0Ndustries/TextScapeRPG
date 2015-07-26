class game:
    def actionPrompt():
        print("Hi")


class mine:
    def prompt():
        print("")
        print("# The Quarry #\n")
        print("Enter an ore to mine, try 'help' or 'exit'")
        mineAction=("Mining action:")
        if(mineAction=="help"):
            mine.help()
        elif(mineAction=="ores"):
            mine.oreList()
        elif(mineAction=="exit"):
            game.actionPrompt()
        elif(mineAction in oreList):
            mine.mine()
        else:
            print("Invalid action!")
            go=input("Press enter to continue.")
            mine.prompt(mineAction)
    def help():
        print("Mining help")
        print("'ores' = Lists ores")
        print("'help' = Displays this interface")
        print("'exit' = Exits back to the main prompt")
        print("\nOr enter an ore type to mine it.")
    def oreList():

    def mine(ore):
