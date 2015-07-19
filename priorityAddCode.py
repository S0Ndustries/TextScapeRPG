# User skillsEXP
attackEXP = 0
strengthEXP = 0
defenceEXP = 0
healthEXP = 0
fishingEXP = 0
cookingEXP = 0
otherSkills = 0


points = 0
for level in range(1,100):
    diff = int(level + 300 * math.pow(2, float(level)/7) )
    points += diff
    str = "Level %d = %d" % (level + 1, points / 4)
    print str
