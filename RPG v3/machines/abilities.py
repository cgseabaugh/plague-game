

def checkAbility(player, ability):
    if ability in player.abilities:
        return 0
    else:
        return 1

def delAbility(player, ability):
    a = checkAbility(player, ability)
    if a == 0:
        player.abilities.remove(ability)
        print(str(" ____________________________________________________________ ").center(140))
        print(str("|                                                            |").center(140))
        print(str("|     You lost the knowledge to perform", str(ability).center(20), ".     |"))
        print(str("|____________________________________________________________|").center(140))
    else:
        print(str(" ___________________________________________________ ").center(140))
        print(str("|                                                   |").center(140))
        print(str("|     You don't know any abilities like that...     |").center(140))
        print(str("|___________________________________________________|").center(140))

def addAbility(player, ability):
    a = checkAbility(player, ability)
    if a == 0:
        player.abilities.append(ability)
        print(str(" ____________________________________________").center(140))
        print(str("|                                            |").center(140))
        print(str("|     You learned", str(ability).center(20), "!     |").center(140))
        print(str("|____________________________________________|").center(140))
        return 0
    elif a == 1:
        print(str(" ________________________________________ ").center(140))
        print(str("|                                        |").center(140))
        print(str("|     You already know that ability.     |").center(140))
        print(str("|________________________________________|").center(140))
        return 1

def showAbilities(player):
    abilities = player.abilities
    print(str(" ___________________________________ ").center(140))
    print(str("|                                   |").center(140))
    print(str("|              Abilities            |").center(140))
    print(str("|___________________________________|").center(140))
    print(str("|                                   |").center(140))
    for x in abilities:
        no = abilities.index(x) + 1
        print(str("|     ", str(x).center(20), "     |").center(140))
        print(str("|_____________________________________|").center(140))

def selectAbility(player):
    print(str(" ____________________________ ").center(140))
    print(str("|                            |").center(140))
    print(str("|     Select an Ability.     |").center(140))
    print(str("|____________________________|").center(140))
    print("")
    a = input(str(":  ").center(140))
    return a

def useAbilities(player):
    print(str(" ______________________________________________________________________ ").center(140))
    print(str("|      _____________       _________________       ______________      |").center(140))
    print(str("|     | 1 |   Use   |     | 2 |   Examine   |     | 3 |   Back   |     |").center(140))
    print(str("|      `````````````       `````````````````       ``````````````      |").center(140))
    print(str("|______________________________________________________________________|").center(140))
    print("")
    a = print(str(":  ").center(140))
    return a

def notEnoughEnergy():
    print(str(" ___________________________________________________________ ").center(140))
    print(str("|                                                           |").center(140))
    print(str("|     You don't have enough energy to use this ability.     |").center(140))
    print(str("|___________________________________________________________|").center(140))

def cantDoHere():
    print(str(" _________________________________ ").center(140))
    print(str("|                                 |").center(140))
    print(str("|     You can't do that here.     |").center(140))
    print(str("|_________________________________|").center(140))

def alreadyAffected():
    print(str(" ___________________________________________ ").center(140))
    print(str("|                                           |").center(140))
    print(str("|     You are already affected by this.     |").center(140))
    print(str("|___________________________________________|").center(140))

def cantFindAbility():
    print(str(" ___________________________________________________ ").center(140))
    print(str("|                                                   |").center(140))
    print(str("|     You don't know any abilities like that...     |").center(140))
    print(str("|___________________________________________________|").center(140))

def examVitalBlow():
    print(str(" _____________________________________________________________________ ").center(140))
    print(str("|                                                                     |").center(140))
    print(str("|     Aim your weapon at a weak spot and deliver a powerful blow!     |").center(140))
    print(str("|_____________________________________________________________________|").center(140))
def examBlackPowder():
    print(str(" ________________________________________________________________________________ ").center(140))
    print(str("|                                                                                |").center(140))
    print(str("|     Ignite a black powder bomb at your location, obscuring your movements!     |").center(140))
    print(str("|________________________________________________________________________________|").center(140))
def examImmolate():
    print(str(" ___________________________________________________________ ").center(140))
    print(str("|                                                           |").center(140))
    print(str("|     Invoke a plume of fire to erupt beneath your foe!     |").center(140))
    print(str("|___________________________________________________________|").center(140))
def examCandlelight():
    print(str(" ________________________________________________________________________________ ").center(140))
    print(str("|                                                                                |").center(140))
    print(str("|     Channel a soft light in your hands that radiates a restorative warmth.     |").center(140))
    print(str("|________________________________________________________________________________|").center(140))
def examShieldStance():
    print(str(" ________________________________________________________________________________ ").center(140))
    print(str("|                                                                                |").center(140))
    print(str("|     Take on a defensive posture, bracing yourself for whatever comes next.     |").center(140))
    print(str("|________________________________________________________________________________|").center(140))
def examBolas():
    print(str(" __________________________________________________________________________________________ ").center(140))
    print(str("|                                                                                          |").center(140))
    print(str("|     Sling a trick weapon at your foe, tangling them up and limiting their movements.     |").center(140))
    print(str("|__________________________________________________________________________________________|").center(140))
def examBlastBolt():
    print(str(" __________________________________________________________________________________ ").center(140))
    print(str("|                                                                                  |").center(140))
    print(str("|     Fire a simple bolt of raw energy. It's as powerful as it is inexpensive.     |").center(140))
    print(str("|__________________________________________________________________________________|").center(140))

class vital_blow (object):
    name = "Vital Blow"
    desc = "Aim your weapon at a weak spot and deliver a powerful blow!"
    price = 1
class black_powder (object):
    name = "Black Powder"
    desc = "Ignite a black powder bomb at your location, obscuring your movements!"
    price = 1
class blast_bolt (object):
    name = "Blast Bolt"
    desc = "Fire a simple bolt of raw energy. It's as powerful as it is inexpensive."
    price = 1
class candlelight (object):
    name = "Candlelight"
    desc = "Channel a soft light in your hands that radiates a restorative warmth."
    price = 2
class shield_stance (object):
    name = "Shield Stance"
    desc = "Take on a defensive posture, bracing yourself for whatever comes next."
    price = 2
class bolas (object):
    name = "Bolas"
    desc = "Sling a trick weapon at your foe, tangling them up and limiting their movements."
    price = 2
class immolate (object):
    name = "Immolate"
    desc = "Invoke a plume of fire to erupt beneath your foe!"
    price = 3


