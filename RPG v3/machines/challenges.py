
import random
from machines.inventory import *

def challenge(player):
    location = player.location
    if location == 11 or location == 12 or location == 13 or location == 14 or location == 15:
        flip = random.randint(1, 2)
        if flip == 1:
            skillChallenge1(player)
        elif flip == 2:
            itemChallenge1(player)
    elif location == 22 or location == 23 or location == 24 or location == 25:
        flip = random.randint(1, 2)
        if flip == 1:
            skillChallenge1(player)
        elif flip == 2:
            itemChallenge1(player)
    elif location == 33 or location == 34 or location == 35:
        flip = random.randint(1, 2)
        if flip == 1:
            skillChallenge1(player)
        elif flip == 2:
            itemChallenge1(player)
    elif location == 44 or location == 45:
        flip = random.randint(1, 2)
        if flip == 1:
            skillChallenge1(player)
        elif flip == 2:
            itemChallenge1(player)
    elif location == 55:
        flip = random.randint(1, 2)
        if flip == 1:
            skillChallenge1(player)
        elif flip == 2:
            itemChallenge1(player)

def skillChallenge1(player):
    skillType = random.randint(1, 3)
    if skillType == 1:
        vigorChal1()
        roll1 = random.randint(1, 3)
        roll2 = random.randint(1, 3)
        check = 5 + roll1
        stat = player.vigor + roll2
        if check > stat:
            vigorChal1Fail()
            chalHpDmg(player, 1)
        elif check <= stat:
            vigorChal1Success()
    elif skillType == 2:
        reflexChal1()
        roll1 = random.randint(1, 3)
        roll2 = random.randint(1, 3)
        check = 5 + roll1
        stat = player.reflex + roll2
        if check > stat:
            reflexChal1Fail
            chalHpDmg(player, 1)
        elif check <= stat:
            reflexChal1Success()
    elif skillType == 3:
        wisdomChal1()
        roll1 = random.randint(1, 3)
        roll2 = random.randint(1, 3)
        check = 5 + roll1
        stat = player.wisdom + roll2
        if check > stat:
            wisdomChal1Fail()
            chalHpDmg(player, 1)
        elif check <= stat:
            wisdomChal1Success()
# def skillChallenge2(player):
# def skillChallenge3(player):
# def skillChallenge4(player):
# def skillChallenge5(player):

def itemChallenge1(player):
    itemType = random.randint(1, 2)
    if itemType == 1:
        torchChal1()
        check = checkItem(player, "Torch")
        if check == 0:
            choice = torchChal1OptA()
            if choice == "1":
                torchChal1Res1()
                chalEpDmg(player, 1)
            elif choice == "2":
                torchChal1Res2()
                chalHpDmg(player, 1)
            elif choice == "3":
                torchChal1Res3()
                deleteItem(player, "Torch")
        elif check == 1:
            choice = torchChal1OptB()
            if choice == "1":
                torchChal1Res1()
                chalEpDmg(player, 1)
            elif choice == "2":
                torchChal1Res2()
                chalHpDmg(player, 1)
    elif itemType == 2:
        shovelChal1()
        check = checkItem(player, "Shovel")
        if check == 0:
            choice = shovelChal1OptA()
            if choice == "1":
                shovelChal1Res1()
                chalEpDmg(player, 1)
            elif choice == "2":
                shovelChal1Res2()
                deleteItem(player, "Shovel")
        elif check == 1:
            choice = shovelChal1OptB()
            if choice == "1":
                shovelChal1Res1()
                chalEpDmg(player, 1)
# def itemChallenge2(player):
# def itemChallenge3(player):
# def itemChallenge4(player):
# def itemChallenge5(player):

def torchChal1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     Your path is blocked by a sprawling bush with vicious thorns. They     |").center(140))
    print(str("|     black and angry, and the cries of small creatures, struggling for      |").center(140))
    print(str("|     freedom, can be heard trapped within them.                             |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You might be able to find a way around the bushes, but there's no      |").center(140))
    print(str("|     telling how far they have grown or how arduous the journey around      |").center(140))
    print(str("|     them would be.                                                         |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     Or you could try to push through them. The thorns are razor sharp,     |").center(140))
    print(str("|     and you risk becoming one of the many other creatures who were         |").center(140))
    print(str("|     incapable of escaping.                                                 |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     Additionally, if you were carrying a torch you could simply burn       |").center(140))
    print(str("|     a path straight through the thorn bushes, saving youself a lot of      |").center(140))
    print(str("|     trouble and pain.                                                      |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def torchChal1OptA():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                      How would you like to proceed?                        |").center(140))
    print(str("|                ___________________________________________                 |").center(140))
    print(str("|               | 1 |     Find a way around the bushes.     |                |").center(140))
    print(str("|                ```````````````````````````````````````````                 |").center(140))
    print(str("|                  ______________________________________                    |").center(140))
    print(str("|                 | 2 |     Push through the bushes.     |                   |").center(140))
    print(str("|                  ``````````````````````````````````````                    |").center(140))
    print(str("|              _______________________________________________               |").center(140))
    print(str("|             | 3 |   Light a torch and burn a path through   |              |").center(140))
    print(str("|              ```````````````````````````````````````````````               |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":  ").center(140))
    return choice
def torchChal1OptB():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                      How would you like to proceed?                        |").center(140))
    print(str("|                ___________________________________________                 |").center(140))
    print(str("|               | 1 |     Find a way around the bushes.     |                |").center(140))
    print(str("|                ```````````````````````````````````````````                 |").center(140))
    print(str("|                  ______________________________________                    |").center(140))
    print(str("|                 | 2 |     Push through the bushes.     |                   |").center(140))
    print(str("|                  ``````````````````````````````````````                    |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":  ").center(140))
    return choice
def torchChal1Res1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You spend many hours hiking around the sprawling thickets. Your        |").center(140))
    print(str("|     exhausted, but at last, you manage to reach its end. You've gotten     |").center(140))
    print(str("|     past the thorn bushes, but doing so has drained you of energy.         |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def torchChal1Res2():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|    You decide to push through the bushes. As you do, the thorns dig deep   |").center(140))
    print(str("|    into your flesh and snag you by your clothing. You manage to squeeze    |").center(140))
    print(str("|    out the other end, but not without a number of nasty lacerations.       |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def torchChal1Res3():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You ignite a torch and press the flames against the bushes. They       |").center(140))
    print(str("|     catch instantly, and you advance through them as the vines burn away.  |").center(140))
    print(str("|     In no time at all, you have cleared a direct path through.             |").center(140))
    print(str("|____________________________________________________________________________|").center(140))

def shovelChal1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     Your path is blocked by a massive pile of rubble. The ground here,     |").center(140))
    print(str("|     fickle and often unsteady, must have shifted long ago, collapsing      |").center(140))
    print(str("|     the hillside.                                                          |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     There's no way to get around the mass of stone and earth, so you'll    |").center(140))
    print(str("|     have to clear a path through. It's a daunting task, and without        |").center(140))
    print(str("|     the proper tool it would prove grueling as well.                       |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     That being said, if you happened to have a shovel with you, you        |").center(140))
    print(str("|     could make short work of removing the debris.                          |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def shovelChal1OptA():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                      How would you like to proceed?                        |").center(140))
    print(str("|                  __________________________________________                |").center(140))
    print(str("|                 | 1 |     Dig through with your hands.     |               |").center(140))
    print(str("|                  ``````````````````````````````````````````                |").center(140))
    print(str("|             __________________________________________________             |").center(140))
    print(str("|            | 2 |     Use a shovel to easily clear a path!     |            |").center(140))
    print(str("|             ``````````````````````````````````````````````````             |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":  ").center(140))
    return choice
def shovelChal1OptB():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                      How would you like to proceed?                        |").center(140))
    print(str("|                  __________________________________________                |").center(140))
    print(str("|                 | 1 |     Dig through with your hands.     |               |").center(140))
    print(str("|                  ``````````````````````````````````````````                |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":  ").center(140))
    return choice
def shovelChal1Res1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     On your hands and knees, you begin the arduous task of digging. One    |").center(140))
    print(str("|     hand full at a time, you move the rock and dirt. It takes you all      |").center(140))
    print(str("|     day, and your hands bleed and ache, but you've cleared just enough of  |").center(140))
    print(str("|     the rubble to climb over the rest.                                     |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def shovelChal1Res2():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     Luckily, you have a shovel. It takes you a few hours of hard work,     |").center(140))
    print(str("|     but you are able to move enough of the rock and earth, allowing you    |").center(140))
    print(str("|     to climb over the rest. The shovel, however, breaks.                   |").center(140))
    print(str("|____________________________________________________________________________|").center(140))

def vigorChal1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     As you tread through the woods, you feel a tickle run up your leg.     |").center(140))
    print(str("|     You slap yourself in an attempt to catch it and you feel a sharp       |").center(140))
    print(str("|     pain shoot through your body. The throbbing is debilitating well       |").center(140))
    print(str("|     after you feel the tiny venemous creature escape from your clothing.   |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def vigorChal1Success():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|    You're thick-skinned and hearty. Though the bite stings, but the pain   |").center(140))
    print(str("|    is easily pushed into the back of your mind. You are able to continue   |").center(140))
    print(str("|    your quest without skipping a beat.                                     |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def vigorChal1Fail():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You try to stay focused, but the pain coursing through you is          |").center(140))
    print(str("|     unbearable. Your vision blurs and your balance wavers as you are       |").center(140))
    print(str("|     washed by the stinging venom. Your health and energy suffer from the   |").center(140))
    print(str("|     agony.                                                                 |").center(140))
    print(str("|____________________________________________________________________________|").center(140))

def reflexChal1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You hear the flapping of wings in the branches above your head.        |").center(140))
    print(str("|     The thin fingers of the petrified trees rattle aggressively, snapping  |").center(140))
    print(str("|     several loose. They fall sharply around you, impaling into the ground  |").center(140))
    print(str("|     like spears.                                                           |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def reflexChal1Success():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     As the stone spikes dig deep into the earth around you, your higher    |").center(140))
    print(str("|     reflexes kick in. You dodge and weave between the falling branches     |").center(140))
    print(str("|     and by the time the barrage ends, you find yourself unscathed.         |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def reflexChal1Fail():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You close your eyes, cover your head with your arms, and pray for      |").center(140))
    print(str("|     the best. You hear the stone branches patter into the ground around    |").center(140))
    print(str("|     you, and suddenly feel the white hot pain of impalement in your        |").center(140))
    print(str("|     shoulder.                                                              |").center(140))
    print(str("|____________________________________________________________________________|").center(140))

def wisdomChal1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     The path through the woods suddenly seems deliberately cleared of      |").center(140))
    print(str("|     foliage and debris. Though suspicious, you have no choice but to       |").center(140))
    print(str("|     carry on, taking care to note the disturbed patches of dirt you pass.  |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def wisdomChal1Success():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|   You recognize the distinct signs of man-made traps hidden in the earth   |").center(140))
    print(str("|   You throw a stone at one of them, and nasty, rusted teeth explode from   |").center(140))
    print(str("|   the dirt around it. You tread the rest of the path carefully.            |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def wisdomChal1Fail():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You make your way down the path, taking note of the odd ground, but    |").center(140))
    print(str("|     you aren't careful with your footing. You walk right into a patch of   |").center(140))
    print(str("|     disturbed earth, triggering something buried underneath. With the      |").center(140))
    print(str("|     clink of a mechanism, sharp teeth erupt and clamp onto your foot,      |").center(140))
    print(str("|     brutally impaling you.                                                 |").center(140))
    print(str("|____________________________________________________________________________|").center(140))


def chalHpDmg(player, severity):
    if severity == 1:
        dmg = random.randint(3, 6)
    elif severity == 2:
        dmg = random.randint(5, 8)
    elif severity == 3:
        dmg = random.randint(8, 12)
    elif severity == 4:
        dmg = random.randint(10, 15)
    elif severity == 5:
        dmg = random.randint(12, 18)
    player.healthPoints = player.healthPoints - dmg
    print(str(" ________________________________________ ").center(140))
    print(str("|                                        |").center(140))
    print(str("|     You lost" + str(dmg).center(3) + "points of health!     |").center(140))
    print(str("|________________________________________|").center(140))

def chalEpDmg(player, severity):
    if severity == 1:
        dmg = random.randint(3, 6)
    elif severity == 2:
        dmg = random.randint(5, 8)
    elif severity == 3:
        dmg = random.randint(8, 12)
    elif severity == 4:
        dmg = random.randint(10, 15)
    elif severity == 5:
        dmg = random.randint(12, 18)
    player.energyPoints = player.energyPoints - dmg
    if player.energyPoints < 0:
        player.energyPoints = 0
    print(str(" ________________________________________ ").center(140))
    print(str("|                                        |").center(140))
    print(str("|     You lost" + str(dmg).center(3) + "points of energy!     |").center(140))
    print(str("|________________________________________|").center(140))