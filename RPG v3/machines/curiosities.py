


import random
from machines.inventory import *

def curiosity(player):
    location = player.location
    if location == 11 or location == 12 or location == 13 or location == 14 or location == 15:
        flip = random.randint(1, 2)
        if flip == 1:
            skillCuriosity1(player)
        elif flip == 2:
            conflict = itemCuriosity1(player)
            if conflict == 1:
                return 1
    elif location == 22 or location == 23 or location == 24 or location == 25:
        flip = random.randint(1, 2)
        if flip == 1:
            skillCuriosity1(player)
        elif flip == 2:
            itemCuriosity1(player)
    elif location == 33 or location == 34 or location == 35:
        flip = random.randint(1, 2)
        if flip == 1:
            skillCuriosity1(player)
        elif flip == 2:
            itemCuriosity1(player)
    elif location == 44 or location == 45:
        flip = random.randint(1, 2)
        if flip == 1:
            skillCuriosity1(player)
        elif flip == 2:
            itemCuriosity1(player)
    elif location == 55:
        flip = random.randint(1, 2)
        if flip == 1:
            skillCuriosity1(player)
        elif flip == 2:
            itemCuriosity1(player)

def skillCuriosity1(player):
    skillType = random.randint(1, 3)
    if skillType == 1:
        strCur1()
        choice = strCur1Opt()
        if choice == 1:
            strCheck = 4 + random.randint(1, 3)
            if player.strength >= strCheck:
                strCur1Res1()
                flip = random.randint(1, 2)
                if flip == 1:
                    strCur1Chest()
                    lootTable(player)
                    findGold(player, 1)
                elif flip == 2:
                    result = lockedChest(player)
                    if result == 1:
                        lootTable(player)
                        findGold(player, 1)
            else:
                strCur1Res2()
        elif choice == 2:
            strCur1Res3()
    elif skillType == 2:
        dexCur1()
        choice = dexCur1Opt()
        if choice == 1:
            dexCheck = 4 + random.randint(1, 3)
            if player.dexterity >= dexCheck:
                dexCur1Res1()
                findGold(player, 3)
            else:
                dexCur1Res2()
                curHpDmg(player, 1)
        elif choice == 2:
            dexCur1Res3()
    elif skillType == 3:
        intCur1()
        choice = intCur1Opt()
        if choice == 1:
            intCheck = 4 + random.randint(1, 3)
            if player.intelligence >= intCheck:
                intCur1Res1()
                curEpHeal(player, 2)
            else:
                intCur1Res2()
                curEpDmg(player, 2)
        elif choice == 2:
            intCur1Res3()
# def skillChallenge2(player):
# def skillChallenge3(player):
# def skillChallenge4(player):
# def skillChallenge5(player):

def strCur1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     A strange tree catches your eye. Split down the middle, there is a     |").center(140))
    print(str("|     hollow crevasse that has grown around something foreign. Perhaps it    |").center(140))
    print(str("|     was placed there long ago, before the tree grew and petrified.         |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     If you're strong enough, you may be able to bust through the stone     |").center(140))
    print(str("|     bark and retrieve what ever is stuck inside.                           |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def strCur1Opt():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                         What would you like to do?                         |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                   ________________________________________                 |").center(140))
    print(str("|                  | 1 |   Attempt to pry the object out.   |                |").center(140))
    print(str("|                   ````````````````````````````````````````                 |").center(140))
    print(str("|                      _________________________________                     |").center(140))
    print(str("|                     | 2 |   Leave the object alone.   |                    |").center(140))
    print(str("|                      `````````````````````````````````                     |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":  ").center(140))
    return int(choice)
def strCur1Res1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|    In an impressive display of strength, you are able to crack the stone   |").center(140))
    print(str("|    bark enough to free the object trapped inside. It's a small chest!      |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def strCur1Res2():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     Try all you might, the stone bark is far to dense for you to chip it   |").center(140))
    print(str("|     away. What ever is trapped inside will likely stay that way forever.   |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def strCur1Res3():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You can't even be sure that what ever is in there is worth the time    |").center(140))
    print(str("|     or energy needed to get it out. You decide to leave it alone.          |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def strCur1Chest():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     The chest was unlocked. Its contents are yours for the taking.         |").center(140))
    print(str("|____________________________________________________________________________|").center(140))

def dexCur1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You hear the suffering whimpers of some animal behind the thickets.    |").center(140))
    print(str("|     Upon invenstigation, you discover a small, fox-like creature with its  |").center(140))
    print(str("|     leg caught in the metal teeth of a trap. When it spots you, it emits   |").center(140))
    print(str("|     a low growl, unsure of your intentions.                                |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     Emissaries of an old trickster God, these creatures have been known    |").center(140))
    print(str("|     to lead some to treasures, and lead others to certain death.           |").center(140))
    print(str("|     If you are quick, you might be able to release it from the trap. But   |").center(140))
    print(str("|     you risk suffering its nasty bite.                                     |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def dexCur1Opt():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                         What would you like to do?                         |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                    _____________________________________                   |").center(140))
    print(str("|                   | 1 |   Attempt to free the animal.   |                  |").center(140))
    print(str("|                    `````````````````````````````````````                   |").center(140))
    print(str("|                       ______________________________                       |").center(140))
    print(str("|                      | 2 |   Leave the animal be.   |                      |").center(140))
    print(str("|                       ``````````````````````````````                       |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":  ").center(140))
    return int(choice)
def dexCur1Res1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You approach the trapped animal, careful not to make any sudden        |").center(140))
    print(str("|     movements. It eyes you suspiciously as you work quickly to disarm the  |").center(140))
    print(str("|     trap. Just as the creature begins to lose patience, the teeth of the   |").center(140))
    print(str("|     trap unclench and the animal bolts away.                               |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You begin to think that's the last you'll see of it, but after a few   |").center(140))
    print(str("|     minutes it returns, clutching a bag of gold coins in its mouth. It     |").center(140))
    print(str("|     drops them at your feet before disappearing once again.                |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def dexCur1Res2():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You try to approach carefully and calmly. The creatures lets you near  |").center(140))
    print(str("|     the trap, but grows agitated the longer you take to disarm it.         |").center(140))
    print(str("|     Something you do actually tightens the trap's teeth. The animal        |").center(140))
    print(str("|     screeches in pain and snaps at you, leaving you with a viscious wound. |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     It's unwilling to let you anywhere near it anymore, forcing you to     |").center(140))
    print(str("|     leave the creature to its fate.                                        |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def dexCur1Res3():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You have neither the time nor the energy to rescue every woodland      |").center(140))
    print(str("|     creature you come across. You decide to leave it be.                   |").center(140))
    print(str("|____________________________________________________________________________|").center(140))

def intCur1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You come across a macabre spectacle: a stone obelisk inscribed with    |").center(140))
    print(str("|     esoteric texts. From the trees around, headless skeletons hang from    |").center(140))
    print(str("|     their bound feet. Their skulls, made porous by numerous drilled        |").center(140))
    print(str("|     holes, lay stacked at the base of the obelisk.                         |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     This is the work of a furtive cult; the worshippers of a dark and old  |").center(140))
    print(str("|     God. The air hums with strange magic, and interacting with the         |").center(140))
    print(str("|     obelisk could prove disasterous. However, if you know what you're      |").center(140))
    print(str("|     doing, you may be able to harness the energies for yourself.           |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def intCur1Opt():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                         What would you like to do?                         |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                    ___________________________________                     |").center(140))
    print(str("|                   | 1 |   Lay hands on the obelisk.   |                    |").center(140))
    print(str("|                    ```````````````````````````````````                     |").center(140))
    print(str("|                    __________________________________                      |").center(140))
    print(str("|                   | 2 |   Leave the obelisk alone.   |                     |").center(140))
    print(str("|                    ``````````````````````````````````                      |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":  ").center(140))
    return int(choice)
def intCur1Res1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     The obelisk grows warm under your hand, and the strange symbols        |").center(140))
    print(str("|     seem to swirl around in your head. You've seen them before, perhaps    |").center(140))
    print(str("|     in a book? You can't remember, but you chant them as they come to you  |").center(140))
    print(str("|     and you are washed by a wave of benevolent energy.                     |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def intCur1Res2():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     The obelisk grows warm under your hand, and strange symbols begin to   |").center(140))
    print(str("|     cloud your vision and fill your head. They are foreign and             |").center(140))
    print(str("|     undecipherable. As they collect in your mind, a sickening feeling      |").center(140))
    print(str("|     comes over from you. As though your energy was being siphoned, you     |").center(140))
    print(str("|     feel weaker by the second. You recoil from the obelisk.                |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def intCur1Res3():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You know enough about the cult worship in these lands to know that     |").center(140))
    print(str("|     their magics are not to be trifled with. You decide its best to leave  |").center(140))
    print(str("|     the obelisk alone.                                                     |").center(140))
    print(str("|____________________________________________________________________________|").center(140))



def itemCuriosity1(player):
    itemType = random.randint(1, 2)
    if itemType == 1:
        torchCur1()
        check = checkItem(player, "Torch")
        if check == 0:
            choice = torchCur1OptA()
            if choice == 1:
                flip = random.randint(1, 2)
                if flip == 1:
                    torchCur1Res1()
                    curHpDmg(player, 1)
                    return 1
                elif flip == 2:
                    torchCur1Res2()
                    findGold(player, 1)
            elif choice == 2:
                torchCur1Res3()
                flip = random.randint(1, 2)
                if flip == 1:
                    torchCur1Res3A()
                    lootTable(player)
                    findGold(player, 1)
                elif flip == 2:
                    torchCur1Res3B()
                    result = lockedChest(player)
                    if result == 1:
                        lootTable(player)
                        findGold(player, 1)
            elif choice == 3:
                torchCur1Leave()
        elif check == 1:
            choice = torchCur1OptB()
            if choice == 1:
                flip = random.randint(1, 2)
                if flip == 1:
                    curHpDmg(player, 1)
                    torchCur1Res1()
                    return 1
                elif flip == 2:
                    torchCur1Res2()
                    findGold(player, 1)
            elif choice == 2:
                torchCur1Leave() 
    elif itemType == 2:
        shovelCur1()
        check = checkItem(player, "Shovel")
        if check == 0:
            choice = shovelCur1OptA()
            if choice == 1:
                deleteItem(player, "Shovel")
                shovelCur1ResA()
                flip = random.randint(1, 2)
                if flip == 1:
                    shovelCur1Unlocked()
                    lootTable(player)
                    findGold(player, 1)
                elif flip == 2:
                    result = lockedChest(player)
                    if result == 1:
                        lootTable(player)
                        findGold(player, 1)
            elif choice == 2:
                flip = random.randint(1, 2)
                if flip == 1:
                    shovelCur1ResB()
                    curEpDmg(player, 1)
                    flip2 = random.randint(1, 2)
                    if flip2 == 1:
                        shovelCur1Unlocked()
                        lootTable(player)
                        findGold(player, 1)
                    elif flip2 == 2:
                        result = lockedChest(player)
                        if result == 1:
                            lootTable(player)
                            findGold(player, 1)
                elif flip == 2:
                    shovelCur1ResC()
                    curHpDmg(player, 1)
                    curEpDmg(player, 1)
            elif choice == 3:
                shovelCur1Leave()
        elif check == 1:
            choice = shovelCur1OptB()
            if choice == 1:
                flip2 = random.randint(1, 2)
                if flip2 == 1:
                    shovelCur1ResB()
                    curEpDmg(player, 1)
                    flip3 = random.randint(1, 2)
                    if flip3 == 1:
                        shovelCur1Unlocked()
                        lootTable(player)
                        findGold(player, 1)
                    elif flip3 == 2:
                        result = lockedChest(player)
                        if result == 1:
                            lootTable(player)
                            findGold(player, 1)
                elif flip2 == 2:
                    shovelCur1ResC()
                    curHpDmg(player, 1)
                    curEpDmg(player, 1)
            elif choice == 2:
                shovelCur1Leave()
            
# def itemChallenge2(player):
# def itemChallenge3(player):
# def itemChallenge4(player):
# def itemChallenge5(player):

def torchCur1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     Along your path, you spot a dark cave retreating deep into the hill    |").center(140))
    print(str("|     side. An ominous draft howls from within. A cave like this may be      |").center(140))
    print(str("|     home to danger, but it may also be hiding something valuable...        |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     But the darkness hums. There's no telling what you might run into,     |").center(140))
    print(str("|     and doing so without a source of light could prove deadly. If you      |").center(140))
    print(str("|     had a torch, you could face the unknown in the light. Or, you could    |").center(140))
    print(str("|     try your luck without the luxury of sight.                             |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     Of course, you could ignore the cave entirely. Who knows if it's even  |").center(140))
    print(str("|     worth your time?                                                       |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def torchCur1OptA():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                      How would you like to proceed?                        |").center(140))
    print(str("|            ___________________________________________________             |").center(140))
    print(str("|           | 1 |     Stumble through the cave in the dark.     |            |").center(140))
    print(str("|            ```````````````````````````````````````````````````             |").center(140))
    print(str("|            ____________________________________________________            |").center(140))
    print(str("|           | 2 |     Light a torch and delve into the cave.     |           |").center(140))
    print(str("|            ````````````````````````````````````````````````````            |").center(140))
    print(str("|          _______________________________________________________           |").center(140))
    print(str("|         | 3 |   Ignore the cave and carry on with your quest.   |          |").center(140))
    print(str("|          ```````````````````````````````````````````````````````           |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":  ").center(140))
    return int(choice)
def torchCur1OptB():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                      How would you like to proceed?                        |").center(140))
    print(str("|            ___________________________________________________             |").center(140))
    print(str("|           | 1 |     Stumble through the cave in the dark.     |            |").center(140))
    print(str("|            ```````````````````````````````````````````````````             |").center(140))
    print(str("|          _______________________________________________________           |").center(140))
    print(str("|         | 2 |   Ignore the cave and carry on with your quest.   |          |").center(140))
    print(str("|          ```````````````````````````````````````````````````````           |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":  ").center(140))
    return int(choice)
def torchCur1Res1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You begin your descent into the dark cave, placing each foot           |").center(140))
    print(str("|      carefully in front of the other. But you aren't carefull enough,      |").center(140))
    print(str("|     and you lose your footing, stumbling hard onto the sharp rocks.        |").center(140))
    print(str("|     Your clattering to the ground echoes down the cave corridors, and      |").center(140))
    print(str("|     as you listen, you hear strange noises echoing back.                   |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def torchCur1Res2():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|    You press on into the darkness, running your hand along the walls as    |").center(140))
    print(str("|    you go. Your foot kicks something soft and heavy, and you stumble       |").center(140))
    print(str("|    over it. You feel the strange object, and to your disgust, you realize  |").center(140))
    print(str("|    it is the aged corpse of some unfortunate traveler. Still, you          |").center(140))
    print(str("|    rummage through the corpse's pockets and find some gold pieces.         |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def torchCur1Res3():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     Your torch illuminates the dark cave as you explore its innards.       |").center(140))
    print(str("|     Before long, your eye catches the glint of metal trim on a wooden      |").center(140))
    print(str("|     chest.                                                                 |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def torchCur1Leave():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|   You ignore the cave, and carry on with your quest without distraction.   |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def torchCur1Res3A():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     The chest lifts open and reveals a number of useful items, all for     |").center(140))
    print(str("|     for your taking.                                                       |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def torchCur1Res3B():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You try to lift the heavy lid of the chest, but it is locked up        |").center(140))
    print(str("|     tightly. If you happened to have a lockpick, you could easily pop it   |").center(140))
    print(str("|     open. If not, you could always try to break it open, assuming you're   |").center(140))
    print(str("|     strong enough to do so. Or you could leave it be.                      |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def torchCur1Res3BOpt1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                        What would you like to do?                          |").center(140))
    print(str("|                      _____________________________                         |").center(140))
    print(str("|                     | 1 |     Use a lockpick.     |                        |").center(140))
    print(str("|                      `````````````````````````````                         |").center(140))
    print(str("|                   ___________________________________                      |").center(140))
    print(str("|                  | 2 |     Break the chest open.     |                     |").center(140))
    print(str("|                   ```````````````````````````````````                      |").center(140))
    print(str("|                  ____________________________________                      |").center(140))
    print(str("|                 | 3 |     Leave the chest alone.     |                     |").center(140))
    print(str("|                  ````````````````````````````````````                      |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":   ").center(140))
    return int(choice)
def torchCur1Res3BOpt2():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                        What would you like to do?                          |").center(140))
    print(str("|                  ___________________________________                       |").center(140))
    print(str("|                 | 1 |     Break the chest open.     |                      |").center(140))
    print(str("|                  ```````````````````````````````````                       |").center(140))
    print(str("|                  ____________________________________                      |").center(140))
    print(str("|                 | 2 |     Leave the chest alone.     |                     |").center(140))
    print(str("|                  ````````````````````````````````````                      |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":   ").center(140))
    return int(choice)
def torchCur1Res3BLockpick():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You use a lockpick to fiddle with the locking mechanism. Soon, an      |").center(140))
    print(str("|     an audible 'Click' tells you that you've gained access. Inside the     |").center(140))
    print(str("|     chest you find a number of useful items.                               |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def torchCur1Res3BBreakSuc():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You pound against the sides of the chest, and manage to bust it        |").center(140))
    print(str("|     open. You pull out a number of useful items.                           |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def torchCur1Res3BBreakFail():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You pound against the sides of the chest, but the wood is sturdy and   |").center(140))
    print(str("|     doesn't budge for you.                                                 |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def torchCur1Res3BLeave():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|    You decide that what ever is in the chest isn't worth the aggrevation.  |").center(140))
    print(str("|____________________________________________________________________________|").center(140))

def shovelCur1():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     Along the path you notice a mound of disturbed earth. The likelihood   |").center(140))
    print(str("|     that something is buried below seems high, though there's no telling   |").center(140))
    print(str("|     how deep you'd have to dig.                                            |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     If you had a shovel, it would be a simple task to dig up what ever     |").center(140))
    print(str("|     was buried here. You could also use your hands, but it would be hard   |").center(140))
    print(str("|     labor. There might not even be anything underneath, so you might       |").center(140))
    print(str("|     consider leaving it be.                                                |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def shovelCur1OptA():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                        What would you like to do?                          |").center(140))
    print(str("|                      ______________________________                        |").center(140))
    print(str("|                     | 1 |   Use a shovel to dig.   |                       |").center(140))
    print(str("|                      ``````````````````````````````                        |").center(140))
    print(str("|                      ______________________________                        |").center(140))
    print(str("|                     | 2 |   Dig with your hands.   |                       |").center(140))
    print(str("|                      ``````````````````````````````                        |").center(140))
    print(str("|                       ___________________________                          |").center(140))
    print(str("|                      | 3 |   Ignore the mound.   |                         |").center(140))
    print(str("|                       ```````````````````````````                          |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":  ").center(140))
    return int(choice)
def shovelCur1OptB():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                        What would you like to do?                          |").center(140))
    print(str("|                      ______________________________                        |").center(140))
    print(str("|                     | 1 |   Dig with your hands.   |                       |").center(140))
    print(str("|                      ``````````````````````````````                        |").center(140))
    print(str("|                       ___________________________                          |").center(140))
    print(str("|                      | 2 |   Ignore the mound.   |                         |").center(140))
    print(str("|                       ```````````````````````````                          |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":  ").center(140))
    return int(choice)
def shovelCur1ResA():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     With your shovel in hand, you dig deep into the earth until you hit    |").center(140))
    print(str("|     something hard. You dust it off and reveal a wooden chest!             |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def shovelCur1ResB():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     On your hands and knees, you begin to scoop the dirt out. You have to  |").center(140))
    print(str("|     do this for quite some time, and though you are exhausted, you find    |").center(140))
    print(str("|     a wooden chest wedged inside.                                          |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def shovelCur1ResC():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You begin the arduous task of shoveling handfulls of dirt and rock.    |").center(140))
    print(str("|     Deeper and deeper you dig until your hands are blistered and raw,      |").center(140))
    print(str("|    but you find nothing but more sharp stones.                             |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def shovelCur1Unlocked():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You open the old chest up, revealing a number of useful items.         |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def shovelCur1Locked():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     The chest you've discovered is locked up tight. If you have a          |").center(140))
    print(str("|     lockpick, you could easily pop it open. If not, you could always try   |").center(140))
    print(str("|     to break it open. Or, you could leave it alone completely.             |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def shovelCur1LockedOptA():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                        What would you like to do?                          |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                  ________________________________________                  |").center(140))
    print(str("|                 | 1 |   Use a lockpick to get it open.   |                 |").center(140))
    print(str("|                  ````````````````````````````````````````                  |").center(140))
    print(str("|                     _______________________________                        |").center(140))
    print(str("|                    | 2 |   Try to break it open.   |                       |").center(140))
    print(str("|                     ```````````````````````````````                        |").center(140))
    print(str("|                     ________________________________                       |").center(140))
    print(str("|                    | 3 |   Leave the chest alone.   |                      |").center(140))
    print(str("|                     ````````````````````````````````                       |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":  ").center(140))
    return int(choice)
def shovelCur1LockedOptB():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                        What would you like to do?                          |").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|                     _______________________________                        |").center(140))
    print(str("|                    | 1 |   Try to break it open.   |                       |").center(140))
    print(str("|                     ```````````````````````````````                        |").center(140))
    print(str("|                     ________________________________                       |").center(140))
    print(str("|                    | 2 |   Leave the chest alone.   |                      |").center(140))
    print(str("|                     ````````````````````````````````                       |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":  ").center(140))
    return int(choice)
def shovelCur1LockedResA():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You use a lockpick to pop the lock open. You lift the lid of the       |").center(140))
    print(str("|     chest to reveal a number of useful items.                              |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def shovelCur1LockedResB():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You pound against the aged wood of the chest, and after a few good     |").center(140))
    print(str("|     blows the wood breaks apart. You pull a number of useful items from    |").center(140))
    print(str("|     the splintered chest.                                                  |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def shovelCur1LockedResC():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You pound against the sides of the old wooden chest,  but it holds     |").center(140))
    print(str("|     firmly no matter how many times you smack it.                          |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def shovelCur1LockedLeave():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|     You decide that the contents of the chest are more than likely not     |").center(140))
    print(str("|     worth the time and effort it would take to get them out.               |").center(140))
    print(str("|____________________________________________________________________________|").center(140))
def shovelCur1Leave():
    print(str(" ____________________________________________________________________________ ").center(140))
    print(str("|                                                                            |").center(140))
    print(str("|   You decide that even if there is anything buried here, it is certainly   |").center(140))
    print(str("|   not worth the time and effort to dig it up.                              |").center(140))
    print(str("|____________________________________________________________________________|").center(140))



def curHpDmg(player, severity):
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

def curEpDmg(player, severity):
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
    print(str("|      You lost" + str(dmg).center(3) + "points of energy!      |").center(140))
    print(str("|________________________________________|").center(140))

def curHpHeal(player, severity):
    if severity == 1:
        heal = random.randint(3, 6)
    elif severity == 2:
        heal = random.randint(5, 8)
    elif severity == 3:
        heal = random.randint(8, 12)
    elif severity == 4:
        heal = random.randint(10, 15)
    elif severity == 5:
        heal = random.randint(12, 18)
    player.healthPoints = player.healthPoints + heal
    print(str(" _____________________________________________ ").center(140))
    print(str("|                                             |").center(140))
    print(str("|     You recovered" + str(heal).center(3) + "points of health!     |").center(140))
    print(str("|_____________________________________________|").center(140))

def curEpHeal(player, severity):
    if severity == 1:
        heal = random.randint(3, 6)
    elif severity == 2:
        heal = random.randint(5, 8)
    elif severity == 3:
        heal = random.randint(8, 12)
    elif severity == 4:
        heal = random.randint(10, 15)
    elif severity == 5:
        heal = random.randint(12, 18)
    player.energyPoints = player.energyPoints + heal
    print(str(" ________________________________________ ").center(140))
    print(str("|                                        |").center(140))
    print(str("|     You recovered" + str(heal).center(3) + "points of energy!     |").center(140))
    print(str("|________________________________________|").center(140))
