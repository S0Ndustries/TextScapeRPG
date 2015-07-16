def fishAdv():
   "You are now fishing!"
   time.sleep(5)
   #run loadingBar

#

def levellingSystem():
    points = 0
    for level in range(1,100):
    diff = int(level + 300 * math.pow(2, float(level)/7) )
    points += diff
    str = "Level %d = %d" % (level + 1, points / 4)
    print str

def cookAdv():
   "What would you like to cool? List cookable items in inventoryList"

#

def healAdv():
   "What would you like to use to heal? List items in inventoryList"

def heal():
   print ("Healed %i HP" % 10)
   playerHP += 10
#

#
