# User skillsEXP
global attackEXP
global attackLevel
attackEXP = 0
attackLevel = 0
global strengthEXP
global strengthLevel
strengthEXP = 0
strengthLevel = 0
global defenceEXP
global defenceLevel
defenceEXP = 0
defenceLevel = 0
global healthEXP
global healthLevel
healthEXP = 0
healthLevel = 0
global fishingEXP
global fishingLevel
fishingEXP = 0
fishingLevel = 0
global cookingEXP
global cookingLevel
cookingEXP = 0
cookingLevel = 0
global cookingEXP
global cookingLevel
otherSkills = 0
otherLevels = 0

import math

points = 0
for level in range(1,99):
    diff = int(level + 300 * math.pow(2, float(level)/7) )
    points += diff
    str = "Level %d = %d" % (level + 1, points / 4)
    print(str)


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

global exp
global level
fishEXP = 18275
myEXP(fishEXP)
fishLevel = level
print("Your level is %i" % fishLevel)
