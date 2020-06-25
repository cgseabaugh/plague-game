
import random

def roomMenu(player):
    print(str(" __________________________________________________________ ").center(140))
    print(str("|                                                          |").center(140))
    print(str("|              How would you like to proceed?              |").center(140))
    print(str("|__________________________________________________________|").center(140))
    print(str(" __________________________________________________________________________________________________ ").center(140))
    print(str("|      ________________________       ________________________       ______________|         |     |").center(140))
    print(str("|     | 1 |      Explore       |     | 2 |     Inventory      |     |   Progress   |   "+ str(player.progress).center(3) +"   |     |").center(140))
    print(str("|      ````````````````````````       ````````````````````````       ``````````````|         |     |").center(140))
    print(str("|                                                                                   `````````      |").center(140))
    print(str("|      ________________________       ________________________       ________________________      |").center(140))
    print(str("|     | 3 |     Abilities      |     | 4 |   View Character   |     | 5 |       Travel       |     |").center(140))
    print(str("|      ````````````````````````       ````````````````````````       ````````````````````````      |").center(140))
    print(str("|__________________________________________________________________________________________________|").center(140))
    print("")
    a = input(str(":  ").center(140))
    return a

def explore():
    outcome = random.randint(1, 100)
    if outcome <= 25:
        return 0 #battle
    elif outcome > 25 and outcome <= 50:
        return 1 #challenge
    elif outcome > 50 and outcome <= 70:
        return 2 #curiosity
    elif outcome > 70 and outcome <= 85:
        return 3 #npc
    elif outcome > 85:
        return 4 #quest



