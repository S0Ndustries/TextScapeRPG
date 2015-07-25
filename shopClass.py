global playerBal
playerBal = 10000
global itemCasket; global itemOyster; global itemSeaweed; global itemFrogSpawn
global itemRAWMinnow; global itemRAWCrayfish; global itemRAWShrimp; global itemRAWSardine; global itemRAWKarambwanji; global itemRAWHerring; global itemRAWAnchovies; global itemRAWMackerel; global itemSeaweed; global itemRAWTrout; global itemRAWCod; global itemRAWPike; global itemRAWSlimyEel; global itemRAWSalmon; global itemFrogSpawn; global itemRAWTuna; global itemRAWCaveEel; global itemRAWRainbowFish; global itemRAWLobster; global itemRAWBass; global itemRAWSwordfish; global itemRAWLavaEel; global itemRAWMonkfish; global itemRAWKarambwan; global itemRAWShark; global itemRAWBaronShark; global itemRAWCavefish; global itemRAWRocktail
itemRAWMinnow = ["Raw Minnow", 111, 000, 111, 000, 0, 0]; itemRAWCrayfish = ["Raw Crayfish", 111, 000, 111, 000, 0, 74]; itemRAWShrimp = ["Raw Shrimp", 111, 000, 111, 000, 0, 18]; itemRAWSardine = ["Raw Sardine", 111, 000, 111, 000, 0, 24]; itemRAWKarambwanji = ["Raw Karambwanji", 111, 000, 111, 000, 0, 0]; itemRAWHerring = ["Raw Herring", 111, 000, 111, 000, 0, 35]; itemRAWAnchovies = ["Raw Anchovies", 111, 000, 111, 000, 0, 14]; itemRAWMackerel = ["Raw Mackerel", 111, 000, 111, 000, 0, 16]; itemSeaweed = ["Seaweed", 111, 000, 111, 000, 0, 32]; itemRAWTrout = ["Raw Trout", 111, 000, 111, 000, 0, 27]; itemRAWCod = ["Raw Cod", 111, 000, 111, 000, 0, 61]; itemRAWPike = ["Raw Pike", 111, 000, 111, 000, 0, 71]; itemRAWSlimyEel = ["Raw Slimy eel", 111, 000, 111, 000, 0, 851]; itemRAWSalmon = ["Raw Salmon", 111, 000, 111, 000, 0, 90]; itemFrogSpawn = ["Raw Frog spawn", 111, 000, 111, 000, 0, 0]; itemRAWTuna = ["Raw Tuna", 111, 000, 111, 000, 0, 109]; itemRAWCaveEel = ["Raw Cave eel", 111, 000, 111, 000, 0, 431]; itemRAWRainbowFish = ["Raw Rainbow fish", 111, 000, 111, 000, 0, 193]; itemRAWLobster = ["Raw Lobster", 111, 000, 111, 000, 0, 235]; itemRAWBass = ["Raw Bass", 111, 000, 111, 000, 0, 419]; itemRAWSwordfish = ["Raw Swordfish", 111, 000, 111, 000, 0, 510]; itemRAWLavaEel = ["Raw Lava eel", 111, 000, 111, 000, 0, 0]; itemRAWMonkfish = ["Raw Monkfish", 111, 000, 111, 000, 0, 555]; itemRAWKarambwan = ["Raw Karambwan", 111, 000, 111, 000, 0, 3356]; itemRAWShark = ["Raw Shark", 111, 000, 111, 000, 0, 816]; itemRAWBaronShark = ["Raw Baron shark", 111, 000, 111, 000, 0, 816]; itemRAWCavefish = ["Raw Cave fish", 111, 000, 111, 000, 0, 2036]; itemRAWRocktail = ["Raw Rocktail", 111, 000, 111, 000, 0, 2690]
global buyableItemList
    #Other fished items
    # Cooked items
global itemMinnow; global itemCrayfish; global itemShrimp; global itemSardine; global itemKarambwanji; global itemHerring; global itemAnchovies; global itemMackerel; global itemTrout; global itemCod; global itemPike; global itemSlimyEel; global itemSalmon; global itemTuna; global itemCaveEel; global itemRainbowFish; global itemLobster; global itemBass; global itemSwordfish; global itemLavaEel; global itemMonkfish; global itemKarambwan; global itemShark; global itemBaronShark; global itemCavefish; global itemRocktail
itemMinnow = ["Minnow", 000, 111, 111, 000, 0, 10, 150]; itemCrayfish = ["Crayfish", 000, 111, 111, 000, 0, 21, 200]; itemShrimp = ["Shrimp", 000, 111, 111, 000, 0, 14, 200]
itemSardine = ["Sardine", 000, 111, 111, 000, 0, 10, 108]; itemKarambwanji = ["Karambwanji", 000, 111, 111, 000, 0, 666, 200]; itemHerring = ["Herring", 000, 111, 111, 000, 0, 10, 200]; itemAnchovies = ["Anchovies", 000, 111, 111, 000, 0, 16, 200]; itemMackerel = ["Mackeral", 000, 111, 111, 000, 0, 5, 200]; itemTrout = ["Trout", 000, 111, 111, 000, 0, 37, 300]; itemCod = ["Cod", 000, 111, 111, 000, 0, 65, 450]; itemPike = ["Pike", 000, 111, 111, 000, 0, 42, 400]; itemSlimyEel = ["Slimy eel", 000, 111, 111, 000, 0, 233, 700]; itemSalmon = ["Salmon", 000, 111, 111, 000, 0, 101, 500]; itemTuna = ["Tuna", 000, 111, 111, 000, 0, 167, 750]; itemCaveEel = ["Cave eel", 000, 111, 111, 000, 0, 160, 950]; itemRainbowFish = ["Rainbow fish", 000, 111, 111, 000, 0, 176, 875]; itemLobster = ["Lobster", 000, 111, 111, 000, 0, 252, 1200]; itemBass = ["Bass", 000, 111, 111, 000, 0, 306, 1300]; itemSwordfish = ["Swordfish", 000, 111, 111, 000, 0, 379, 1400]; itemLavaEel = ["Lava eel", 000, 111, 111, 000, 0, 666, 1060]; itemMonkfish = ["Monkfish", 000, 111, 111, 000, 0, 441, 1600]; itemKarambwan = ["Karambwan", 000, 111, 111, 000, 0, 3347, 750]; itemShark = ["Shark", 000, 111, 111, 000, 0, 817, 2000]; itemBaronShark = ["Baron shark", 000, 111, 111, 000, 0, 1302, 2100]; itemCavefish = ["Cave fish", 000, 111, 111, 000, 0, 1827, 2000]; itemRocktail = ["Rocktail", 000, 111, 111, 000, 0, 2559, 2300]

itemCasket = ["Casket", 111, 111, 111, 000, 0]; itemOyster = ["Oyster", 111, 111, 111, 000, 0]; itemSeaweed = ["Seaweed", 111, 000, 111, 000, 0, 0, 0]; itemFrogSpawn = ["Frog spawn", 111, 000, 111, 000, 0, 0, 0];

buyableItemList = [itemRAWMinnow, itemRAWCrayfish, itemRAWShrimp, itemRAWSardine, itemRAWKarambwanji, itemRAWHerring, itemRAWAnchovies, itemRAWMackerel, itemSeaweed, itemRAWTrout, itemRAWCod, itemRAWPike, itemRAWSlimyEel, itemRAWSalmon, itemFrogSpawn, itemRAWTuna, itemRAWCaveEel, itemRAWRainbowFish, itemRAWLobster, itemRAWBass, itemRAWSwordfish, itemRAWLavaEel, itemRAWMonkfish, itemRAWKarambwan, itemRAWShark, itemRAWBaronShark, itemRAWCavefish, itemRAWRocktail, itemMinnow, itemCrayfish, itemShrimp, itemSardine, itemKarambwanji, itemHerring, itemAnchovies, itemMackerel, itemSeaweed, itemTrout, itemCod, itemPike, itemSlimyEel, itemSalmon, itemFrogSpawn, itemTuna, itemCaveEel, itemRainbowFish, itemLobster, itemBass, itemSwordfish, itemLavaEel, itemMonkfish, itemKarambwan, itemShark, itemBaronShark, itemCavefish, itemRocktail]

class game:
    def actionPrompt():
        print("Bye!")
        time.sleep(0.5)

class shop:
    def prompt():
        global playerBal
        print("Type 'buy', 'sell', or try 'help' / 'exit'")
        buyAction = input("Buy action:")
        if(buyAction == "help"):
            shop.help()
        elif(buyAction == "exit"):
            game.actionPrompt()
        elif(buyAction == "buy"):
            shop.buy()
        elif(buyAction == "sell"):
            shop.sell()
        else:
            print("Invalid comand!")
            go=input("Press enter to continue.")
            shop.prompt()

    def help():
        print("\n<-- Shop help menu -->\n")
        print("'help' = Displays this interface")
        print("'exit' = Exits back to the main action prompt")
        print("'buy' = Displayer buying interface")
        print("'sell' = Displays selling interface")
        go=input("\nPress enter to continue.")
        shop.prompt()

    def buy():
        global itemRAWMinnow; global itemRAWCrayfish; global itemRAWShrimp; global itemRAWSardine; global itemRAWKarambwanji; global itemRAWHerring; global itemRAWAnchovies; global itemRAWMackerel; global itemSeaweed; global itemRAWTrout; global itemRAWCod; global itemRAWPike; global itemRAWSlimyEel; global itemRAWSalmon; global itemFrogSpawn; global itemRAWTuna; global itemRAWCaveEel; global itemRAWRainbowFish; global itemRAWLobster; global itemRAWBass; global itemRAWSwordfish; global itemRAWLavaEel; global itemRAWMonkfish; global itemRAWKarambwan; global itemRAWShark; global itemRAWBaronShark; global itemRAWCavefish; global itemRAWRocktail
        global itemMinnow; global itemCrayfish; global itemShrimp; global itemSardine; global itemKarambwanji; global itemHerring; global itemAnchovies; global itemMackerel; global itemTrout; global itemCod; global itemPike; global itemSlimyEel; global itemSalmon; global itemTuna; global itemCaveEel; global itemRainbowFish; global itemLobster; global itemBass; global itemSwordfish; global itemLavaEel; global itemMonkfish; global itemKarambwan; global itemShark; global itemBaronShark; global itemCavefish; global itemRocktail
        global buyableItemList
        print("[+] Buying interface [+]")
        print("Enter item you'd like to buy, 'list' to display items, or 'exit'")
        buyItem = input("Buy action: ")
        x = 0
        if(buyItem == "list"):
            print("Buyable items: \n")
            y = 0
            while(y == 0):
                if(x < 56):
                    itemBuy = buyableItemList[x]
                    print("%s" % itemBuy[0])
                    x += 1
                else:
                    go=input("Press enter to continue.")
                    shop.buy()
        elif(buyItem == "exit"):
            shop.prompt()
        elif(buyItem == "test"):
            print("test")
    def sell():
        global itemRAWMinnow; global itemRAWCrayfish; global itemRAWShrimp; global itemRAWSardine; global itemRAWKarambwanji; global itemRAWHerring; global itemRAWAnchovies; global itemRAWMackerel; global itemSeaweed; global itemRAWTrout; global itemRAWCod; global itemRAWPike; global itemRAWSlimyEel; global itemRAWSalmon; global itemFrogSpawn; global itemRAWTuna; global itemRAWCaveEel; global itemRAWRainbowFish; global itemRAWLobster; global itemRAWBass; global itemRAWSwordfish; global itemRAWLavaEel; global itemRAWMonkfish; global itemRAWKarambwan; global itemRAWShark; global itemRAWBaronShark; global itemRAWCavefish; global itemRAWRocktail
        global itemMinnow; global itemCrayfish; global itemShrimp; global itemSardine; global itemKarambwanji; global itemHerring; global itemAnchovies; global itemMackerel; global itemTrout; global itemCod; global itemPike; global itemSlimyEel; global itemSalmon; global itemTuna; global itemCaveEel; global itemRainbowFish; global itemLobster; global itemBass; global itemSwordfish; global itemLavaEel; global itemMonkfish; global itemKarambwan; global itemShark; global itemBaronShark; global itemCavefish; global itemRocktail
        global buyableItemList
        print("[-] Selling interface [-]")
        print("Enter item you'd like to sell, 'list' to display items, or 'exit'")
        sellItem = ("Sell action: ")


shop.prompt()
