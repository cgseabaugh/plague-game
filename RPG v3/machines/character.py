from machines.display import *

class character:
    def __init__ (self, name, lv, xhp, hp, xep, ep, stre, dex, intl, vig, ref, wis, patk, matk, pdfn, mdfn, acc, eva, wep, arm, trnk, inv, abl, gold, ins, loc, prog, eff, mod):
        self.name = name
        self.level = lv
        self.maxHealthPoints = xhp
        self.healthPoints = hp
        self.maxEnergyPoints = xep
        self.energyPoints = ep
        self.strength = stre
        self.dexterity = dex
        self.intelligence = intl
        self.vigor = vig
        self.reflex = ref
        self.wisdom = wis
        self.physicalAttack = patk
        self.magicAttack = matk
        self.physicalDefense = pdfn
        self.magicDefense = mdfn
        self.accuracy = acc
        self.evade = eva
        self.weapon = wep
        self.armor = arm
        self.trinket = trnk
        self.inventory = inv
        self.abilities = abl
        self.gold = gold
        self.insight = ins
        self.location = loc
        self.progress = prog
        self.effects = eff
        self.modifiers = mod

def newPlayer():
    knightBio()
    hunterBio()
    scholarBio()
    print(str(" ______________________________ ").center(140))
    print(str("|                              |").center(140))
    print(str("|     Choose a profession.     |").center(140))
    print(str("|______________________________|").center(140))
    print("")
    choiceA = input(str(": ").rjust(80))
    if choiceA == "Knight" or choiceA == "knight":
        return 1
    elif choiceA == "Hunter" or choiceA == "hunter":
        return 2
    elif choiceA == "Scholar" or choiceA == "scholar":
        return 3
    


def showCharacter(player):
    if player.name == "Knight":
        print("                                  _,,,                    [ HP ]=[", player.healthPoints, "]      [ EP ]=[", player.energyPoints, "]")
        print("                                _|T|__                                                                                           ")
        print("            [ LV ]=[", str(player.level).center(3), "]     /((((( \         ===========================================================")
        print("                              /)||||/`(\  /|                                                                                     ")
        print("                             /) |===|  (\| |              [ STR ]=[", player.strength, "]        [ VIG ]=[", player.vigor, "]")
        print("                     <======)0- /\##\   0| |                                                                                 ")
        print("                               /#/|#|    | |              [ DEX ]=[", player.dexterity, "]        [ REF ]=[", player.reflex, "]")
        print("                              /#/ \#\    | |                                                                                   ")
        print("                              |#|  |#|   |/               [ INT ]=[", player.intelligence, "]        [ WIS ]=[", player.wisdom, "]")
        print("                              /_|  |_|                                                                                           ")
        print("")
        print("                     ======================================================================================")
        print("                               [ WEAPON ]=[", player.weapon, "]   [ PATK ]=[", player.physicalAttack, "]   [ MATK ]=[", player.magicAttack, "]   [ ACC ]=[", player.accuracy, "]")
        print("")
        print("                               [ ARMOR ]=[", player.armor, "]   [ PDFN ]=[", player.physicalDefense, "]   [ MDFN ]=[", player.magicDefense, "]   [ EVA ]=[", player.evade, "]")
        print("")
        print("                               [ TRINKET ]=[", player.trinket, "]")
        print("                     ======================================================================================")
    elif player.name == "Hunter":
        print("||                               __/`|_                     [ HP ]=[", player.healthPoints, "]      [ EP ]=[", player.energyPoints, "]")
        print("||                                _\`|__                    ")
        print("||            [ LV ]=[", str(player.level).center(3), "]     /(\/ ( \         ===========================================================")
        print("||                              /)||  /`(\                  ")
        print("||                             /) ||  |  (\_,               [ STR ]=[", player.strength, "]        [ VIG ]=[", player.vigor, "]")
        print("||                         <==]0- /\##|   0||               ")
        print("||                               /#/|#|  \ || /             [ DEX ]=[", player.dexterity, "]        [ REF ]=[", player.reflex, "]")
        print("||                              (#( |#|   \||/              ")
        print("||                               \#\|#|    ``               [ INT ]=[", player.intelligence, "]        [ WIS ]=[", player.wisdom, "]")
        print("||                                |/\_\                                                                                           ")
        print("||")
        print("||                     =================================================================================================")
        print("||                             [ WEAPON ]=[", player.weapon, "]   [ PATK ]=[", player.physicalAttack, "]   [ MATK ]=[", player.magicAttack, "]   [ ACC ]=[", player.accuracy, "]")
        print("||")
        print("||                             [ ARMOR ]=[", player.armor, "]   [ PDFN ]=[", player.physicalDefense, "]   [ MDFN ]=[", player.magicDefense, "]   [ EVA ]=[", player.evade, "]")
        print("")
        print("                               [ TRINKET ]=[", player.trinket, "]")
        print("||                     =================================================================================================")
    elif player.name == "Scholar":
        print("||                                 /`\    ,`,                [ HP ]=[", player.healthPoints, "]      [ EP ]=[", player.energyPoints, "]")
        print("||                                _\`/__ ( 0 )              ")
        print("||            [ LV ]=[", str(player.level).center(3), "]     /( \ ( \  |      ===========================================================")
        print("||                              /)| / |`(\ |                ")
        print("||                             /) |/ /\  (\|                 [ STR ]=[", player.strength, "]        [ VIG ]=[", player.vigor, "]")
        print("||                             0  / /  |   0                 ")
        print("||                               / |   |   |                 [ DEX ]=[", player.dexterity, "]        [ REF ]=[", player.reflex, "]")
        print("||                              /  |    \  |                 ")
        print("||                              |___\____| |                 [ INT ]=[", player.intelligence, "]        [ WIS ]=[", player.wisdom, "]")
        print("||                              /#|    |#| |                                                                                        ")
        print("||")
        print("||                     =================================================================================================")
        print("||                             [ WEAPON ]=[", player.weapon, "]   [ PATK ]=[", player.physicalAttack, "]   [ MATK ]=[", player.magicAttack, "]   [ ACC ]=[", player.accuracy, "]")
        print("||")
        print("||                             [ ARMOR ]=[", player.armor, "]   [ PDFN ]=[", player.physicalDefense, "]   [ MDFN ]=[", player.magicDefense, "]   [ EVA ]=[", player.evade, "]")
        print("")
        print("                               [ TRINKET ]=[", player.trinket, "]")
        print("||                     =================================================================================================")

def knightBio():
    print("||####################################################################################################################################")
    print("||++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("||....................................................................................................................................")
    print("||             _,,,           _   __  _    _   _____    ____    _   _   _____   _____________________________________________________ ")
    print("||           _|T|__          |@| /@/ |@\  |@| |/|@|\|  /@/\@\  |@| |@| |/|@|\| |                                                     |")
    print("||          /((((( \         |@|/@/  |@|\ |@|   |@|   |@| ___  |@|_|@|   |@|   |  The knight is hardy and strong. It has a lot of    |")
    print("||         /)||||/`(\  /|    |@|\@\  |@|`\|@|   |@|   |@| `\@| |@|`|@|   |@|   |                                                     |")
    print("||        /) |===|  (\| |    |@| \@\ |@| `\@| |\|@|/|  \@\_/@| |@| |@|   |@|   |  health and can endure great hits. Its a good       |")
    print("||<======)0- /\##\   0| |    ```  ``````   `` ```````   `````  ``` ```   ```   |                                                     |")
    print("||          /#/|#|    | |    [ BASE HEALTH ]=[ 20 ]  [ BASE ENERGY ]=[ 5 ]     |  choice for an easy playthrough.                    |")
    print("||         /#/ \#\    | |    [ STRENGTH ]=====[ 5 ]  [ VIGOR ]=======[ 7 ]     |                                                     |")
    print("||         |#|  |#|   |/     [ DEXTERITY ]====[ 3 ]  [ REFLEX ]======[ 3 ]     |                                                     |")
    print("||         /_|  |_|          [ INTELLIGENCE]==[ 1 ]  [ WISDOM ]======[ 1 ]     |_____________________________________________________|")
    print("||....................................................................................................................................")
    print("||++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
def hunterBio():
    print("||####################################################################################################################################")
    print("||++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("||....................................................................................................................................")
    print("||          __/`|_            _    _   _   _   _    _   _____  _____   ____     _____________________________________________________ ")
    print("||           _\`|__          |@|  |@| |@| |@| |@\  |@| |/|@|\| |@|`\| |@|`)@)  |                                                     |")
    print("||          /(\/ ( \         |@|__|@| |@| |@| |@|\ |@|   |@|   |@|__  |@|/@/   |   The hunter is quick and precise. It is well-      |")
    print("||         /)||  /`(\        |@|``|@| |@| |@| |@|`\|@|   |@|   |@|``  |@|\@\   |                                                     |")
    print("||        /) ||  |  (\_,     |@|  |@| \@\_/@/ |@| `\@|   |@|   |@|_/| |@| \@\  |   rounded offensively, though its defenses suffer.  |")
    print("||   <==]0-  /|##|   0||     ```  ```   ````  ```  ```   ```   `````` ```  ``` |                                                     |")
    print("||          /#/\#|  \ || /   [ BASE HEALTH ]=[ 17 ]   [ BASE ENERGY ]=[ 8 ]    |   Its a good  choice for a challenging playthrough. |")
    print("||         (#( |#|   \||/    [ STRENGTH ]=====[ 3 ]   [ VIGOR ]=======[ 1 ]    |                                                     |")
    print("||          \#\|#|    ``     [ DEXTERITY ]====[ 7 ]   [ REFLEX ]======[ 5 ]    |                                                     |")
    print("||           |/\_\           [ INTELLIGENCE ]=[ 3 ]   [ WISDOM ]======[ 1 ]    |_____________________________________________________|")
    print("||....................................................................................................................................")
    print("||++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
def scholarBio():
    print("||####################################################################################################################################")
    print("||++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("||....................................................................................................................................")
    print("||          /`\    ,`,     ____   ____  _    _   ____   _      ____     ______    ___________________________________________________ ")
    print("||         _\`/__ ( 0 )   /@/`\| /@/`\||@|  |@| /@/\@\ |@|    |@|\@\    |@|`\@\  |                                                   |")
    print("||        /( \ ( \  |     \@\__ |@|    |@|__|@||@|  |@||@|    |@|_\@\   |@|_/@/  |   The scholar is cunning and knowledgeable. It    |")
    print("||       /)| / |`(\ |      ``\@\|@|    |@|``|@||@|  |@||@|    |@|``\@\  |@|`\@\  |                                                   |")
    print("||      /) |/ /\  (\|     |\_/@/ \@\_/||@|  |@| \@\/@/ |@|__/||@|   \@\ |@|  \@\ |   is well-rounded defensively, but is weak        |")
    print("||     0  /  /  |   0     `````   ````````  ```  ````  ``````````   ```````   ```|                                                   |")
    print("||       /  |   |   |        [ BASE HEALTH ]=[ 14 ]   [ BASE ENERGY ]=[ 12 ]     |   offensively. Its a good choice for a difficult  |")
    print("||      /   |    \  |        [ STRENGTH ]=====[ 1 ]   [ VIGOR ]========[ 3 ]     |                                                   |")
    print("||      |____\___|  |        [ DEXTERITY ]====[ 1 ]   [ REFLEX ]=======[ 3 ]     |   playthrough.                                    |")
    print("||      /#|    |#|  |        [ INTELLIGENCE ]=[ 7 ]   [ WISDOM ]=======[ 5 ]     |___________________________________________________|")

