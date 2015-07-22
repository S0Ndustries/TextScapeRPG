# FIX THIS

global fishXP
fishXP = 0

def tBaits(fType):
    global fishXP
    if(fType[2] == 0):
        print("You cast your line into the water.")
        print("Your line is hooked!")
        print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3])
    elif(fType[2] == 1):
        print("You thrust your cage into the water.")
        print("You pull it back out!")
        print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3])
    elif(fType[2] == 2):
        print("You dip your small net into the water.")
        print("You pull it back out!")
        print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3])
    elif(fType[2] == 3):
        print("You cast your large net into the water.")
        print("You pull it back out!")
        print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3])
    elif(fType[2] == 4):
        print("You cast your line into the water.")
        print("You reel it in!")
        print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3])
    elif(fType[2] == 5):
        print("You stab your harpoon into the water.")
        print("You pull it back out!")
        print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3])
    elif(fType[2] == 6):
        print("You place your lobster pot into the water.")
        print("You pull it back out!")
        print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3])
    elif(fType[2] == 7):
        print("You cast your line into the water.")
        print("You reel it in!")
        print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3])
    elif(fType[2] == 6):
        print("You mysteriously use your karambwanvessel.")
        print("You feel a bite!")
        print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3])
    elif(fType[2] == 7):
        print("You mysteriously use your living minerals.")
        print("You feel a bite!")
        print("You have caught: %s! & gained %i XP!" % (fType[0], fType[3])
