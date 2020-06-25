

import random
from machines.merchants import *
from machines.storyteller import *
from machines.abilities import *
from machines.storyteller import *

shopstate = 0

def ally(player):
    rollAlly = random.randint(1, 10)
    if rollAlly == 1 or rollAlly == 2:
        genMerch(player)
    elif rollAlly == 3:
        armorMerch(player)
    elif rollAlly == 4:
        wepMerch(player)
    elif rollAlly == 5 or rollAlly == 6 or rollAlly == 7:
        fountain(player)
    elif rollAlly == 8 or rollAlly == 9:
        tellerLoc(player)
    elif rollAlly == 10:
        abilityMerch(player)

def genMerch(player):
    shopstate = 1
    while shopstate == 1:
        print(str(" ___________________________________________________________________________________ ").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|     You are met by a strangely-dressed man, weighed down with an overly large     |").center(140))
        print(str("|     pack strapped to his back.                                                    |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|   '' Ho, traveler. You have quite the road set before you. Be sure you have ''    |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|   '' everything you need. Your journey will be fraught with tribulation, and ''   |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|                  '' death comes quickly to the unprepared. ''                     |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|___________________________________________________________________________________|").center(140))
        x = merchOptions()
        if x == 1:
            genMerchTable(player)
        elif x == 2:
            sellItem(player)
        elif x == 3:
            shopstate = 0

def wepMerch(player):
    shopstate = 1
    while shopstate == 1:
        print(str(" ___________________________________________________________________________________ ").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|     You encounter an unscrupulous man, armed to the teeth. He waves you over,     |").center(140))
        print(str("|     and draws your attention to an assortment of weapons placed on the ground     |").center(140))
        print(str("|     before him.                                                                   |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|   '' You have a dangerous look about you. Perhaps you are in need of a new ''     |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("| '' instrument of violence? I'm sure I have something to suit your... talents. ''  |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|___________________________________________________________________________________|").center(140))
        x = merchOptions()
        if x == 1:
            wepMerchTable(player)
        elif x == 2:
            sellItem(player)
        elif x == 3:
            shopstate = 0

def armorMerch(player):
    shopstate = 1
    while shopstate == 1:
        print(str(" ___________________________________________________________________________________ ").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|     A jovial man of substantial stature bellows a harty laugh at the sight        |").center(140))
        print(str("|     of you. Upon the back of his pack-animal hangs several garbs of armor.        |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|   '' A child has strayed into these dead lands. Have you the stuff to meet  ''    |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|        '' the dangers of this place? You won't make it far without proper ''      |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|                      '' protection. Have a look at my wares! ''                   |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|___________________________________________________________________________________|").center(140))
        x = merchOptions()
        if x == 1:
            armorMerchTable(player)
        elif x == 2:
            sellItem(player)
        elif x == 3:
            shopstate = 0

def abilityMerch(player):
    shopstate = 1
    while shopstate == 1:
        print(str(" ___________________________________________________________________________________ ").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|     An aged and well-travelled man sees you coming, and raises a hand to stop     |").center(140))
        print(str("|     you. He carries books and scrolls, and though his ragged cloths are humble,   |").center(140))
        print(str("|     he glows with experience.                                                     |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|   '' You do not appear prepared for what lies ahead of you. I am a teacher  ''    |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|   '' of many secret arts. If you are prepared to sacrifice and study, then ''     |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|                  '' perhaps I can teach you something useful. ''                  |").center(140))
        print(str("|                                                                                   |").center(140))
        print(str("|___________________________________________________________________________________|").center(140))
        x = ablMerchOptions()
        if x == 1:
            abilityMerchTable(player)
        elif x == 2:
            shopstate = 0

def fountain(player):
    loc = player.location
    if loc == 11 or loc == 12 or loc == 13 or loc == 14 or loc == 15:
        print(str(" _____________________________________________________________________________________________ ").center(140))
        print(str("|                                                                                             |").center(140))
        print(str("|     Buried under branches and dead foliage is a fountain of stone. Engraved are strange     |").center(140))
        print(str("|     symbols and depictions of men and of monsters. They tell a story you aren't familiar    |").center(140))
        print(str("|     with. Inside bubbles a crisp water, impossibly clear and cool, and beneath the          |").center(140))
        print(str("|     brilliant waters rest innumerable coins of different metals, engraved with the emblems  |").center(140))
        print(str("|     antiquated kingdoms, long extinct.                                                      |").center(140))
        print(str("|_____________________________________________________________________________________________|").center(140))
    elif loc == 22 or loc == 23 or loc == 24 or loc == 25:
        print("Fountain")
    elif loc == 33 or loc == 34 or loc == 35:
        print("Fountain")
    elif loc == 44 or loc == 45:
        print("Fountain")
    elif loc == 55:
        print("Fountain")
    print(str(" ____________________________________________________________________________________ ").center(140))
    print(str("|                                                                                    |").center(140))
    print(str("|        Would you like to leave gold in the fountain in exchange for power?         |").center(140))
    print(str("|              __________________            ____________________________            |").center(140))
    print(str("|             | 1 |   Level Up   |          | 2 |   Leave the Fountain   |           |").center(140))
    print(str("|              ``````````````````            ````````````````````````````            |").center(140))
    print(str("|____________________________________________________________________________________|").center(140))
    x = input(str(":  ").rjust(60))
    if x == "1":
        fountain = 1
        while fountain == 1:
            cost = player.level * 50
            print(str(" ________________________________________________________________________ ").center(140))
            print(str("|                                                                        |").center(140))
            print(str("|                    Select an Attribute to Increase:                    |").center(140))
            print(str("|________________________________________________________________________|").center(140))
            print(str("|                                                                        |").center(140))
            print(str("|             ____________________       ________________                |").center(140))
            print(str("|            | Current Level | " + str(player.level).ljust(2) + " |     | Cost | " + str(cost).center(7) + " |               |").center(140))
            print(str("|             ````````````````````       ````````````````                |").center(140))
            print(str("|                     __________________       ____                      |").center(140))
            print(str("|                    | 1 | Strength     |=====| " + str(player.strength).ljust(2) + " |                     |").center(140))
            print(str("|                     ``````````````````       ````                      |").center(140))
            print(str("|                     __________________       ____                      |").center(140))
            print(str("|                    | 2 | Dexterity    |=====| " + str(player.dexterity).ljust(2) + " |                     |").center(140))
            print(str("|                     ``````````````````       ````                      |").center(140))
            print(str("|                     __________________       ____                      |").center(140))
            print(str("|                    | 3 | Intelligence |=====| " + str(player.intelligence).ljust(2) + " |                     |").center(140))
            print(str("|                     ``````````````````       ````                      |").center(140))
            print(str("|                     __________________       ____                      |").center(140))
            print(str("|                    | 4 | Vigor        |=====| " + str(player.vigor).ljust(2) + " |                     |").center(140))
            print(str("|                     ``````````````````       ````                      |").center(140))
            print(str("|                     __________________       ____                      |").center(140))
            print(str("|                    | 5 | Reflex       |=====| " + str(player.reflex).ljust(2) + " |                     |").center(140))
            print(str("|                     ``````````````````       ````                      |").center(140))
            print(str("|                     __________________       ____                      |").center(140))
            print(str("|                    | 6 | Wisdom       |=====| " + str(player.wisdom).ljust(2) + " |                     |").center(140))
            print(str("|                     ``````````````````       ````                      |").center(140))
            print(str("|                                                                        |").center(140))
            print(str("|                               ________________                         |").center(140))
            print(str("|                              | 7 |   Cancel   |                        |").center(140))
            print(str("|                               ````````````````                         |").center(140))
            print(str("|________________________________________________________________________|").center(140))
            y = input(str(":  ").rjust(60))
            if y == "1":
                if player.gold >= cost:
                    player.gold = player.gold - cost
                    player.strength = player.strength + 1
                    player.maxHealthPoints = player.maxHealthPoints + 5
                    player.healthPoints = player.maxHealthPoints
                    player.level = player.level + 1
                    print(str(" __________________________________________________ ").center(140))
                    print(str("|                                                  |").center(140))
                    print(str("|     Your Strength and Health have increased.     |").center(140))
                    print(str("|__________________________________________________|").center(140))
                else:
                    cantAffordLevel()
            elif y == "2":
                if player.gold >= cost:
                    player.gold = player.gold - cost
                    player.dexterity = player.dexterity + 1
                    player.maxHealthPoints = player.maxHealthPoints + 5
                    player.healthPoints = player.maxHealthPoints
                    player.level = player.level + 1
                    print(str(" ___________________________________________________ ").center(140))
                    print(str("|                                                   |").center(140))
                    print(str("|     Your Dexterity and Health have increased.     |").center(140))
                    print(str("|___________________________________________________|").center(140))
                else:
                    cantAffordLevel()
            elif y == "3":
                if player.gold >= cost:
                    player.gold = player.gold - cost
                    player.intelligence = player.intelligence + 1
                    player.maxHealthPoints = player.maxHealthPoints + 5
                    player.healthPoints = player.maxHealthPoints
                    player.level = player.level + 1
                    print(str(" ______________________________________________________ ").center(140))
                    print(str("|                                                      |").center(140))
                    print(str("|     Your Intelligence and Health have increased.     |").center(140))
                    print(str("|______________________________________________________|").center(140))
                else:
                    cantAffordLevel()
            elif y == "4":
                if player.gold >= cost:
                    player.gold = player.gold - cost
                    player.vigor = player.vigor + 1
                    player.maxHealthPoints = player.maxHealthPoints + 5
                    player.healthPoints = player.maxHealthPoints
                    player.level = player.level + 1
                    print(str(" _______________________________________________ ").center(140))
                    print(str("|                                               |").center(140))
                    print(str("|     Your Vigor and Health have increased.     |").center(140))
                    print(str("|_______________________________________________|").center(140))
                else:
                    cantAffordLevel()
            elif y == "5":
                if player.gold >= cost:
                    player.gold = player.gold - cost
                    player.reflex = player.reflex + 1
                    player.maxHealthPoints = player.maxHealthPoints + 5
                    player.healthPoints = player.maxHealthPoints
                    player.level = player.level + 1
                    print(str(" ________________________________________________ ").center(140))
                    print(str("|                                                |").center(140))
                    print(str("|     Your Reflex and Health have increased.     |").center(140))
                    print(str("|________________________________________________|").center(140))
                else:
                    cantAffordLevel()
            elif y == "6":
                if player.gold >= cost:
                    player.gold = player.gold - cost
                    player.wisdom = player.wisdom + 1
                    player.maxHealthPoints = player.maxHealthPoints + 5
                    player.healthPoints = player.maxHealthPoints
                    player.level = player.level + 1
                    print(str(" ________________________________________________ ").center(140))
                    print(str("|                                                |").center(140))
                    print(str("|     Your Wisdom and Health have increased.     |").center(140))
                    print(str("|________________________________________________|").center(140))
                else:
                    cantAffordLevel()
                    fountain = 0
            elif y == "7":
                fountain = 0

def cantAffordLevel():
    print(str(" _______________________________________ ").center(140))
    print(str("|                                       |").center(140))
    print(str("|     You can't afford to level up.     |").center(140))
    print(str("|_______________________________________|").center(140))





