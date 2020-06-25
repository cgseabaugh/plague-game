from machines.enemies import *
from machines.inventory import *
from machines.abilities import *
import random

def battle(player, state):

    battlestate = state

    location = player.location
    turnNo = 0
    baseStr = player.strength
    baseDex = player.dexterity
    baseInt = player.intelligence
    baseVig = player.vigor
    baseRef = player.reflex
    baseWis = player.wisdom
    baseAcc = player.accuracy
    baseEva = player.evade
    basePAtk = player.physicalAttack
    baseMAtk = player.magicAttack
    basePDfn = player.physicalDefense
    baseMDfn = player.magicDefense


    def resetPlayer(player, baseStr, baseDex, baseInt, baseVig, baseRef, baseWis, baseAcc, baseEva, basePatk, baseMatk, basePdfn, baseMdfn):
        player.strength = baseStr
        player.dexterity = baseDex
        player.intelligence = baseInt
        player.vigor = baseVig
        player.reflex = baseRef
        player.wisdom = baseWis
        player.accuracy = baseAcc
        player.evasion = baseEva

    def resetEnemy(enemy):
        enemy.health = enemy.maxHealth

    def playerMissChance(player):
        print(str(" ________________________________ ").center(140))
        print(str("|                                |").center(140))
        print(str("|     You attack your foe...     |").center(140))
        print(str("|________________________________|").center(140))
        playerDex = player.dexterity / 2
        if playerDex > 1:
            playerDex = 1
        baseAcc = player.accuracy * playerDex
        hitChance = baseAcc + random.randint(1, 5)
        enemyRef = enemySquad[enemyNo].reflex / 2
        baseEva = enemySquad[enemyNo].evade * enemyRef
        evadeChance = baseEva + random.randint(1, 5)
        if hitChance > evadeChance:
            return 0
        elif hitChance < evadeChance:
            return 1
        elif hitChance == evadeChance:
            return 2
        elif hitChance == evadeChance * 2:
            return 3

    def enemyMissChance(player):
        print(str(" ____________________________ ").center(140))
        print(str("|                            |").center(140))
        print(str("|     Your enemy attacks...  |").center(140))
        print(str("|____________________________|").center(140))
        enemyDex = enemySquad[enemyNo].dexterity / 2
        if enemyDex < 1:
            enemyDex = 1
        baseAcc = enemySquad[enemyNo].accuracy * enemyDex
        hitChance = baseAcc + random.randint(1, 5)
        playerRef = player.reflex / 2
        if playerRef < 1:
            playerRef = 1
        baseRef = player.evade * playerRef
        evadeChance = baseRef + random.randint(1, 5)
        if hitChance > evadeChance:
            return 0
        elif hitChance < evadeChance:
            return 1
        elif hitChance == evadeChance:
            return 2
        elif hitChance == evadeChance * 2:
            return 3

    def enemyDmg(dmg):
        newHealth = enemySquad[enemyNo].health - dmg
        enemySquad[enemyNo].health = newHealth

    def playerDmg(dmg):
        newHealth = player.healthPoints - dmg
        player.healthPoints = newHealth

    def  playerAttackP(hit):
        playerStr = player.strength / 2
        if playerStr < 1:
            playerStr = 1
        baseAttack = player.physicalAttack * playerStr
        attack = baseAttack + random.randint(1, 5)
        enemyVig = enemySquad[enemyNo].vigor / 2
        if enemyVig < 1:
            enemyVig = 1
        baseDefense = enemySquad[enemyNo].physDefense * enemyVig
        defense = baseDefense + random.randint(1, 5)
        damage = attack - defense
        if damage < 0:
            damage = 0
        if hit == 0:
            print(str(" __________________________________________________ ").center(140))
            print(str("|                                                  |").center(140))
            print(str("|     You struck your enemy, dealing " + str(damage).center(3) + " damage!    |").center(140))
            print(str("|__________________________________________________|").center(140))
        if hit == 2:
            damage = damage / 2
            print(str(" ____________________________________________________________________________ ").center(140))
            print(str("|                                                                            |").center(140))
            print(str("|     You struck a glancing blow against your enemy, dealing " + str(damage).center(3) + " damage.    |").center(140))
            print(str("|____________________________________________________________________________|").center(140))
        elif hit == 3:
            damage = damage * 2
            print(str(" ____________________________________________________________________________"))
            print(str("|                                                                            |").center(140))
            print(str("|     You struck a critical blow against your enemy, dealing " + str(damage).center(3) + " damage!    |").center(140))
            print(str("|____________________________________________________________________________|").center(140))
        enemyDmg(damage)

    def  playerAttackM():
        playerInt = player.intelligence / 2
        if playerInt < 1:
            playerInt = 1
        baseAttack = player.magicAttack * playerInt
        attack = baseAttack + random.randint(1, 5)
        enemyWis = enemySquad[enemyNo].wisdom / 2
        if enemyWis < 1:
            enemyWis = 1
        baseDefense = enemySquad[enemyNo].magDefense * enemyWis
        defense = baseDefense + random.randint(1, 5)
        damage = attack - defense
        if damage < 0:
            damage = 0
        print(str(" __________________________________________________ ").center(140))
        print(str("|                                                  |").center(140))
        print(str("|     You struck your enemy, dealing " + str(damage).center(3) + " damage!    |").center(140))
        print(str("|__________________________________________________|").center(140))
        enemyDmg(damage)

    def enemyAttackP(hit):
        enemyStr = enemySquad[enemyNo].strength / 2
        if enemyStr < 1:
            enemyStr = 1
        baseAttack = enemySquad[enemyNo].physAttack * enemyStr
        attack = baseAttack + random.randint(1, 5)
        playerVig = player.vigor / 2
        if playerVig < 1:
            playerVig = 1
        baseDefense = player.physicalDefense * playerVig
        defense = baseDefense + random.randint(1, 5)
        damage = attack - defense
        if damage < 0:
            damage = 0
        if hit == 0:
            print(str(" __________________________________________________ ").center(140))
            print(str("|                                                  |").center(140))
            print(str("|     Your enemy struck you, dealing " + str(damage).center(3) + " damage!    |").center(140))
            print(str("|__________________________________________________|").center(140))
        elif hit == 2:
            damage = damage / 2
            print(str(" ____________________________________________________________________________ ").center(140))
            print(str("|                                                                            |").center(140))
            print(str("|     Your enemy struck a glancing blow against you, dealing " + str(damage).center(3) + " damage.   |").center(140))
            print(str("|____________________________________________________________________________|").center(140))
        elif hit == 3:
            damage = damage * 2
            print(str(" ____________________________________________________________________________"))
            print(str("|                                                                            |").center(140))
            print(str("|     Your enemy struck a critical blow against you, dealing " + str(damage).center(3) + " damage!   |").center(140))
            print(str("|____________________________________________________________________________|").center(140))
        playerDmg(damage)

    def enemyAttackM():
        enemyInt = enemySquad[enemyNo].intelligence / 2
        if enemyInt < 1:
            enemyInt = 1
        baseAttack = enemySquad[enemyNo].magAttack * enemyInt
        attack = baseAttack + random.randint(1, 5)
        playerWis = player.wisdom / 2
        if playerWis < 1:
            playerWis = 1
        baseDefense = player.magicDefense * playerWis
        defense = baseDefense + random.randint(1, 5)
        damage = attack - defense
        if damage < 0:
            damage = 0
        print(str(" __________________________________________________ ").center(140))
        print(str("|                                                  |").center(140))
        print(str("|     Your enemy struck you, dealing " + str(damage).center(3) + " damage!   |").center(140))
        print(str("|__________________________________________________|").center(140))
        playerDmg(damage)

    def healthBar(turnNo, hp, ep, ename, ehp):
        print(str(" ____________________________________________________________________________").center(140))
        print(str("|      ________   ____                      ____________________   ____      |").center(140))
        print(str("|     | Health |=|" + str(hp).center(4) + "|                    |" + str(ename).center(20) + "|=|" + str(ehp).center(4) + "|     |").center(140))
        print(str("|      ````````   ````                      ````````````````````   ````      |").center(140))
        print(str("|      ________   ____                      ______   _____                   |").center(140))
        print(str("|     | Energy |=|" + str(ep).center(4) + "|                    | Turn |=| " + str(turnNo).center(3) + " |                  |").center(140))
        print(str("|      ````````   ````                      ``````   `````                   |").center(140))
        print(str("|____________________________________________________________________________|").center(140))

    def combatMenu():
        print(str(" ________________________________________________________ ").center(140))
        print(str("|                                                        |").center(140))
        print(str("|                    Select An Action                    |").center(140))
        print(str("|________________________________________________________|").center(140))
        print(str("|      ___________________       __________________      |").center(140))
        print(str("|     | 1 |    Attack     |     | 2 |   Ability    |     |").center(140))
        print(str("|      ```````````````````       ``````````````````      |").center(140))
        print(str("|      ___________________       __________________      |").center(140))
        print(str("|     | 3 |   Inventory   |     | 4 |   Run Away   |     |").center(140))
        print(str("|      ```````````````````       ``````````````````      |").center(140))
        print(str("|________________________________________________________|").center(140))
        print("")
        action = input(str(":  ").center(140))
        return action

    def playerMiss():
        print(str(" ____________________________________ ").center(140))
        print(str("|                                    |").center(140))
        print(str("|     ...But your attack missed!     |").center(140))
        print(str("|____________________________________|").center(140))

    def enemyMiss():
        print(str(" _____________________________ ").center(140))
        print(str("|                             |").center(140))
        print(str("|     ...But they missed!     |").center(140))
        print(str("|_____________________________|").center(140))

    def flee(player, enemy):
        print(str(" __________________________________ ").center(140))
        print(str("|                                  |").center(140))
        print(str("|     You attempt to escape...     |").center(140))
        print(str("|__________________________________|").center(140))
        escape = player.reflex + random.randint(1, 5)
        catch = enemy.reflex + random.randint(1, 5)
        if escape > catch:
            print(str(" __________________________________ ").center(140))
            print(str("|                                  |").center(140))
            print(str("|     You managed to get away!     |").center(140))
            print(str("|__________________________________|").center(140))
            return 0
        elif escape == catch:
            print(str(" __________________________________________________________").center(140))
            print(str("|                                                          |").center(140))
            print(str("|     You managed to escape, but not without injury...     |").center(140))
            print(str("|__________________________________________________________|").center(140))
            enemyAttackP(2)
            return 1
        elif escape < catch:
            print(str(" _________________________________________________________________________ ").center(140))
            print(str("|                                                                         |").center(140))
            print(str("|     You failed to escape your enemy, and were injured while trying!     |").center(140))
            print(str("|_________________________________________________________________________|").center(140))
            enemyAttackP(2)
            return 1

    def useVitalBlow(player):
        if battlestate == 1:
            if player.energyPoints >= 2:
                roll = random.randint(2, 3)
                baseAttack = player.strength * roll
                attack = baseAttack + random.randint(1, 5)
                enemyVig = enemySquad[enemyNo].vigor / 2
                if enemyVig < 1:
                    enemyVig = 1
                baseDefense = enemySquad[enemyNo].physDefense * enemyVig
                defense = baseDefense + random.randint(1, 5)
                damage = attack - defense
                if damage < 1:
                    damage = 0
                print(str(" ________________________________________________________________________________ ").center(140))
                print(str("|                                                                                |").center(140))
                print(str("|     You aimed your attack carefully, targeting your enemy's weakest point!     |").center(140))
                print(str("|     Vital Blow dealt " + str(damage).center(3) + " damage to your enemy!                                |").center(140))
                print(str("|________________________________________________________________________________|").center(140))
                enemyDmg(damage)
                player.energyPoints = player.energyPoints - 2
            else:
                notEnoughEnergy()
        else:
            cantDoHere()
    def useBlackPowder(player):
        if battlestate == 1:
            if player.energy >= 2:
                if "Black Powder" in player.effects:
                    alreadyAffected()
                else:
                    player.effects.append("Black Powder")
                    player.evade = player.evade + 5
                    player.energyPoints = player.energyPoints - 2
            else:
                notEnoughEnergy()
        else:
            cantDoHere()
    def useBlastBolt(player):
        if battlestate == 1:
            if player.energyPoints >= 1:
                print(str(" ________________________________________________________________________________ ").center(140))
                print(str("|                                                                                |").center(140))
                print(str("|     You fire an arc of light from your finger that collides into your foe!     |").center(140))
                print(str("|________________________________________________________________________________|").center(140))
                playerAttackM()
                player.energyPoints = player.energyPoints - 1
            else:
                notEnoughEnergy()
        else:
            cantDoHere()
    def useCandlelight(player):
        if player.energyPoints >= 3:
            baseInt = player.intelligence / 2
            if baseInt < 1:
                baseInt = 1
            heal = baseInt + random.randint(1, 5)
            print(str(" ________________________________________________________________________ ").center(140))
            print(str("|                                                                        |").center(140))
            print(str("|     A gentle light radiates from your hand and sooths your wounds.     |").center(140))
            print(str("|     You are healed for " + str(heal).center(3) + " points of health!                      |").center(140))
            print(str("|________________________________________________________________________|").center(140))
            player.healthPoints = player.healthPoints + heal
            player.energyPoints = player.energyPoints - 3
        else:
            notEnoughEnergy()
    def useShieldStance(player):
        if battlestate == 1:
            if player.energyPoints >= 2:
                if "Shield Stance" in player.effects:
                    alreadyAffected()
                else:
                    player.effects.append("Shield Stance")
                    player.physicalDefense = player.physicalDefense + 5
                    player.energyPoints = player.energyPoints - 2
                    print(str(" ___________________________________________________________________________________________ ").center(140))
                    print(str("|                                                                                           |").center(140))
                    print(str("|     You've taken a highly defensive stance, bracing you against any physical attacks.     |").center(140))
                    print(str("|___________________________________________________________________________________________|").center(140))
            else:
                notEnoughEnergy()
        else:
            cantDoHere()
    def useBolas(player):
        if battlestate == 1:
            if player.energyPoints >= 3:
                enemySquad[enemyNo].reflex = 0
                enemySquad[enemyNo].evade = 0
                player.energyPoints = player.energyPoints - 3
                print(str(" _________________________________________________________________________________________ ").center(140))
                print(str("|                                                                                         |").center(140))
                print(str("|     You toss a bolas at your foe, entangling their legs and halting their movement!     |").center(140))
                print(str("|_________________________________________________________________________________________|").center(140))
            else:
                notEnoughEnergy()
        else:
            cantDoHere()
    def useImmolate(player):
        if battlestate == 1:
            if player.energyPoints >= 4:
                attack = player.intelligence * random.randint(1, 3)
                enemyWis = enemySquad[enemyNo].wisdom / 2
                if enemyWis < 1:
                    enemyWis = 1
                baseDefense = enemySquad[enemyNo].magicDefense * enemyWis
                defense = baseDefense + random.randint(1, 5)
                damage = attack - defense
                enemyDmg(damage)
                player.energyPoints = player.energyPoints - 4
                print(str(" __________________________________________________________________________________________ ").center(100))
                print(str("|                                                                                          |").center(100))
                print(str("|     You focus your mind on your foe and a plume of fire erupts from underneath them!     |").center(100))
                print(str("|     The inferno deals " + str(damage).center(3) + " damage to your enemy!                                      |").center(100))
                print(str("|__________________________________________________________________________________________|").center(140))
            else:
                notEnoughEnergy()
        else:
            cantDoHere()

    def cast(player, ability):
        if ability == "Vital Blow":
            useVitalBlow(player)
        elif ability == "Black Powder":
            useBlackPowder(player)
        elif ability == "Blast Bolt":
            useBlastBolt(player)
        elif ability == "Candlelight":
            useCandlelight(player)
        elif ability == "Shield Stance":
            useShieldStance(player)
        elif ability == "Bolas":
            useBolas(player)
        elif ability == "Immolate":
            useImmolate(player)

    def examine(player, ability):
        if ability == "Vital Blow":
            examVitalBlow()
        elif ability == "Black Powder":
            examBlackPowder()
        elif ability == "Blast Bolt":
            examBlastBolt()
        elif ability == "Candlelight":
            examCandlelight()
        elif ability == "Shield Stance":
            examShieldStance()
        elif ability == "Bolas":
            examBolas()
        elif ability == "Immolate":
            examImmolate()

    def playerTurn(player, turnNo):
        turnNo = turnNo + 1
        hp = player.healthPoints
        ep = player.energyPoints
        ename = enemySquad[enemyNo].name
        ehp = enemySquad[enemyNo].health
        healthBar(turnNo, hp, ep, ename, ehp)
        action = combatMenu()
        if action == "1":
            hit = playerMissChance(player)
            if hit == 1:
                playerMiss()
            else:
                playerAttackP(hit)
        elif action == "2":
            showAbilities(player)
            a = useAbilities(player)
            if a == 1:
                choice = selectAbility(player)
                use = checkAbility(player, choice)
                if use == 0:
                    cast(player, choice)
                elif use == 1:
                    cantFindAbility()
            elif a == 2:
                choice = selectAbility(player)
                exam = checkAbility(player, choice)
                if exam == 0:
                    examine(player, choice)
                elif exam == 1:
                    cantFindAbility()
        elif action == "3":
            showInventory(player)
            useInventory(player)
        elif action == "4":
            result = flee(player, enemySquad[enemyNo])
            

    def enemyTurn(player):
        a = enemySquad[enemyNo].strength
        b = enemySquad[enemyNo].intelligence
        if a >= b:
            hit = enemyMissChance(player)
            if hit == 1:
                enemyMiss()
            else:
                enemyAttackP(hit)
        else:
            hit = enemyMissChance(player)
            if hit == 1:
                enemyMiss()
            else:
                enemyAttackM()





    

    if location == 11 or location == 12 or location == 13 or location == 14 or location == 15:
        enemySquad = [carrion_crow, frothing_hound, vagabond]
    elif location == 22 or location == 23 or location == 24 or location == 25:
        enemySquad = [frothing_hound, rat_king, vagabond, mad_heretic, festering_pilgrim]
    elif location == 33 or location == 34 or location == 35:
        enemySquad = [mad_heretic, cutthroat, festering_pilgrim, pus_of_man, corpse_collector]
    elif location == 44 or location == 45:
        enemySquad = [graverobber, corpse_collector, sin_eater, infant_deep_one]
    elif location == 55:
        enemySquad = [vile_surgeon, pus_of_man, bile_beast, infant_deep_one, deep_seated_beast]

    enemyNo = random.randint(1, len(enemySquad)) -1



    print(str(" ___________________________________________________________________________ ").center(140))
    print(str("|                                                                           |").center(140))
    print(str("|     " + str(enemySquad[enemyNo].intro1).center(65) + "     |").center(140))
    print(str("|     " + str(enemySquad[enemyNo].intro2).center(65) + "     |").center(140))
    print(str("|     " + str(enemySquad[enemyNo].intro3).center(65) + "     |").center(140))
    print(str("|___________________________________________________________________________|").center(140))
    print(str(" ________________________________________________ ").center(140))
    print(str("|                                                |").center(140))
    print(str("|   You are attacked by a" + str(enemySquad[enemyNo].name).center(20) + "!   |").center(140))
    print(str("|________________________________________________|").center(140))

    while player.healthPoints > 0 and enemySquad[enemyNo].health > 0:
        playerInit = player.dexterity + random.randint(1, 5)
        enemyInit = enemySquad[enemyNo].dexterity + random.randint(1, 5)
        if playerInit >= enemyInit:
            playerTurn(player, turnNo)
            if enemySquad[enemyNo].health <= 0:
                print(str(" _______________________________________________________________________ ").center(140))
                print(str("|                                                                       |").center(140))
                print(str("|     You struck a fatal blow, defeating the" + str(enemySquad[enemyNo].name).center(20) + "!     |").center(140))
                print(str("|_______________________________________________________________________|").center(140))
                lootTable(player)
                resetEnemy(enemySquad[enemyNo])
                return 0
            else:
                enemyTurn(player)
                if player.healthPoints <= 0:
                    print(str(" ____________________________________________________________________ ").center(140))
                    print(str("|                                                                    |").center(140))
                    print(str("|     The" + str(enemySquad[enemyNo].name).center(20) + "struck a deadly blow against you.     |").center(140))
                    print(str("|                                                                    |").center(140))
                    print(str("|                        You have perished...                        |").center(140))
                    print(str("|____________________________________________________________________|").center(140))
                    return 1
        elif playerInit < enemyInit:
            enemyTurn(player)
            if player.healthPoints <= 0:
                print(str(" ____________________________________________________________________ ").center(140))
                print(str("|                                                                    |").center(140))
                print(str("|     The" + str(enemySquad[enemyNo].name).center(20) + "struck a deadly blow against you.     |").center(140))
                print(str("|                                                                    |").center(140))
                print(str("|                        You have perished...                        |").center(140))
                print(str("|____________________________________________________________________|").center(140))
                return 1
            else:
                playerTurn(player, turnNo)
                if enemySquad[enemyNo].health <= 0:
                    print(str(" _______________________________________________________________________ ").center(140))
                    print(str("|                                                                       |").center(140))
                    print(str("|     You struck a fatal blow, defeating the" + str(enemySquad[enemyNo].name).center(20) + "!     |").center(140))
                    print(str("|_______________________________________________________________________|").center(140))
                    lootTable(player)
                    resetEnemy(enemySquad[enemyNo])
                    return 0


