
import random


def showInventory(player):
    inventory = player.inventory
    print(str(" _________________________________________________________ ").center(140))
    print(str("|                                                         |").center(140))
    print(str("|                    I N V E N T O R Y                    |").center(140))
    print(str("|_________________________________________________________|").center(140))
    print(str("|                   _________________                     |").center(140))
    print(str("|                  | Gold |" + str(player.gold).center(10) + "|                    |").center(140))
    print(str("|                   `````````````````                     |").center(140))
    print(str("|                _________________________                |").center(140))
    print(str("|               |                         |               |").center(140))
    for item in inventory:
        print(str("|               |" + str(item).center(25) + "|               |").center(140))
    print(str("|               |_________________________|               |").center(140))
    print(str("|_________________________________________________________|").center(140))

def useInventory(player):
    print(str(" ______________________________________________________________________________ ").center(140))
    print(str("|     __________________       ______________________       ______________     |").center(140))
    print(str("|    | 1 |   Use Item   |     | 2 |   Examine Item   |     | 3 |   Back   |    |").center(140))
    print(str("|     ``````````````````       ``````````````````````       ``````````````     |").center(140))
    print(str("|______________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":  ").center(140))
    if choice == "1":
        decisionY = selectItem(player)
        itemInv = checkItem(player, decisionY)
        if itemInv == 0:
            if decisionY == "Vial of Blood" or decisionY == "Bone Idol" or decisionY == "Pulsating Mass" or decisionY == "Violated SKull" or decisionY == "Drop of Ichor" or decisionY == "Sanguine Gem" or decisionY == "Bone Idol" or decisionY == "Porcelain Doll" or decisionY == "Sunlight Opal":
                cantUseItem()
            elif decisionY == "Torch" or decisionY == "Lockpick" or decisionY == "Shovel" or decisionY == "Curing Tonic" or decisionY == "Holy Water":
                cantUseItem()
            elif decisionY == "Health Drop":
                useHealthDrop(player)
            elif decisionY == "Stimulant Drop":
                useStimulantDrop(player)
            elif decisionY == "Health Vial":
                useHealthVial(player)
            elif decisionY == "Stimulant Vial":
                useStimulantVial(player)
            elif decisionY == "Health Syrum":
                useHealthSyrum(player)
            elif decisionY == "Stimulant Syrum":
                useStimulantSyrum(player)
            elif decisionY == "Health Elixir":
                useHealthElixir(player)
            elif decisionY == "Stimulant Elixir":
                useStimulantElixir(player)
            elif decisionY == "Chipped Hatchet":
                equipWeapon(player, decisionY)
            elif decisionY == "Rusted Shortsword":
                equipWeapon(player, decisionY)
            elif decisionY == "Hand Crossbow":
                equipWeapon(player, decisionY)
            elif decisionY == "Warped Wand":
                equipWeapon(player, decisionY)
            elif decisionY == "Flanged Mace":
                equipWeapon(player, decisionY)
            elif decisionY == "Arming Sword":
                equipWeapon(player, decisionY)
            elif decisionY == "Light Crossbow":
                equipWeapon(player, decisionY)
            elif decisionY == "Brimming Cane":
                equipWeapon(player, decisionY)
            elif decisionY == "Morningstar":
                equipWeapon(player, decisionY)
            elif decisionY == "Flamberge":
                equipWeapon(player, decisionY)
            elif decisionY == "Heavy Crossbow":
                equipWeapon(player, decisionY)
            elif decisionY == "Obsidian Cane":
                equipWeapon(player, decisionY)
            elif decisionY == "Halberd":
                equipWeapon(player, decisionY)
            elif decisionY == "Zweihander":
                equipWeapon(player, decisionY)
            elif decisionY == "Arbalest":
                equipWeapon(player, decisionY)
            elif decisionY == "Scrying Staff":
                equipWeapon(player, decisionY)
            elif decisionY == "Granite Maul":
                equipWeapon(player, decisionY)
            elif decisionY == "Terror Sword":
                equipWeapon(player, decisionY)
            elif decisionY == "Foreign Rifle":
                equipWeapon(player, decisionY)
            elif decisionY == "Trismegistus":
                equipWeapon(player, decisionY)
            elif decisionY == "Chain Hauberk":
                equipArmor(player, decisionY)
            elif decisionY == "Padded Jacket":
                equipArmor(player, decisionY)
            elif decisionY == "Cloth Garb":
                equipArmor(player, decisionY)
            elif decisionY == "Reinforced Mail":
                equipArmor(player, decisionY)
            elif decisionY == "Rogues Coat":
                equipArmor(player, decisionY)
            elif decisionY == "Dashing Suit":
                equipArmor(player, decisionY)
            elif decisionY == "Heavy Lamellar":
                equipArmor(player, decisionY)
            elif decisionY == "Brigandine":
                equipArmor(player, decisionY)
            elif decisionY == "Silk Robe":
                equipArmor(player, decisionY)
            elif decisionY == "Steel Cuirass":
                equipArmor(player, decisionY)
            elif decisionY == "Threaded Coat":
                equipArmor(player, decisionY)
            elif decisionY == "Magus Suit":
                equipArmor(player, decisionY)
            elif decisionY == "Krastenburst Suit":
                equipArmor(player, decisionY)
            elif decisionY == "Black Hide Jacket":
                equipArmor(player, decisionY)
            elif decisionY == "Warlock Regalia":
                equipArmor(player, decisionY)
        elif itemInv == 1:
            cantFindItem()
    elif choice == "2":
        decisionY = selectItem(player)
        itemInv = checkItem(player, decisionY)
        if itemInv == 0:
            if decisionY == "Torch":
                examItem(torch)
            elif decisionY == "Lockpick":
                examItem(lockpick)
            elif decisionY == "Shovel":
                examItem(shovel)
            elif decisionY == "Curing Tonic":
                examItem(curing_tonic)
            elif decisionY == "Holy Water":
                examItem(holy_water)
            elif decisionY == "Health Drop":
                examItem(health_drop)
            elif decisionY == "Stimulant Drop":
                examItem(stimulant_drop)
            elif decisionY == "Health Vial":
                examItem(health_vial)
            elif decisionY == "Stimulant Vial":
                examItem(stimulant_vial)
            elif decisionY == "Health Syrum":
                examItem(health_syrum)
            elif decisionY == "Stimulant Syrum":
                examItem(stimulant_syrum)
            elif decisionY == "Health Elixir":
                examItem(health_elixir)
            elif decisionY == "Stimulant Elixir":
                examItem(stimulant_elixir)
            elif decisionY == "Chipped Hatchet":
                examItem(chipped_hatchet)
            elif decisionY == "Rusted Shortsword":
                examItem(rusted_shortsword)
            elif decisionY == "Hand Crossbow":
                examItem(hand_crossbow)
            elif decisionY == "Warped Wand":
                examItem(warped_wand)
            elif decisionY == "Flanged Mace":
                examItem(flanged_mace)
            elif decisionY == "Arming Sword":
                examItem(arming_sword)
            elif decisionY == "Light Crossbow":
                examItem(light_crossbow)
            elif decisionY == "Brimming Cane":
                examItem(brimming_cane)
            elif decisionY == "Morningstar":
                examItem(morningstar)
            elif decisionY == "Flamberge":
                examItem(flamberge)
            elif decisionY == "Heavy Crossbow":
                examItem(heavy_crossbow)
            elif decisionY == "Obsidian Cane":
                examItem(obsidian_cane)
            elif decisionY == "Halberd":
                examItem(halberd)
            elif decisionY == "Zweihander":
                examItem(zweihander)
            elif decisionY == "Arbalest":
                examItem(arbalest)
            elif decisionY == "Scrying Staff":
                examItem(scrying_staff)
            elif decisionY == "Granite Maul":
                examItem(granite_maul)
            elif decisionY == "Terror Sword":
                examItem(terror_sword)
            elif decisionY == "Foreign Rifle":
                examItem(foreign_rifle)
            elif decisionY == "Trismegistus":
                examItem(trismegistus)
            elif decisionY == "Chain Hauberk":
                examItem(chain_hauberk)
            elif decisionY == "Padded Jacket":
                examItem(padded_jacket)
            elif decisionY == "Cloth Garb":
                examItem(cloth_garb)
            elif decisionY == "Reinforced Mail":
                examItem(reinforced_mail)
            elif decisionY == "Rogues Coat":
                examItem(rogues_coat)
            elif decisionY == "Dashing Suit":
                examItem(dashing_suit)
            elif decisionY == "Heavy Lamellar":
                examItem(heavy_lamellar)
            elif decisionY == "Brigandine":
                examItem(brigandine)
            elif decisionY == "Silk Robe":
                examItem(silk_robe)
            elif decisionY == "Steel Cuirass":
                examItem(steel_cuirass)
            elif decisionY == "Threaded Coat":
                examItem(threaded_coat)
            elif decisionY == "Magus Suit":
                examItem(magus_suit)
            elif decisionY == "Krastenburst Suit":
                examItem(kastenburst_suit)
            elif decisionY == "Black Hide Jacket":
                examItem(black_hide_jacket)
            elif decisionY == "Warlock Regalia":
                examItem(warlock_regalia)
        elif itemInv == 1:
            cantFindItem()

def checkItem(player, item):
    if item in player.inventory:
        return 0
    else:
        return 1

def addItem(player, item):
    if len(player.inventory) < 15:
        player.inventory.append(item)
        print(str(" _______________________________________________________________ ").center(140))
        print(str("|                                                               |").center(140))
        print(str("|          " + str(item).center(15) + "was added to your inventory!          |").center(140))
        print(str("|_______________________________________________________________|").center(140))
    else:
        delete = fullInventory(player)
        if delete == 0:
            player.inventory.appent(item)

def selectItem(player):
    print(str(" _______________________________________________________ ").center(140))
    print(str("|                                                       |").center(140))
    print(str("|          Select an Item from your Inventory.          |").center(140))
    print(str("|                     ________________                  |").center(140))
    print(str("|                    | 1 |   Cancel   |                 |").center(140))
    print(str("|                     ````````````````                  |").center(140))
    print(str("|_______________________________________________________|").center(140))
    print("")
    choice = input(str(":   ").rjust(60))
    if choice in player.inventory:
        return choice
    elif choice not in player.inventory:
        cantFindItem()

def cantFindItem():
    print(str(" ______________________________________________________________ ").center(140))
    print(str("|                                                              |").center(140))
    print(str("|          That item doesn't exist in your Inventory.          |").center(140))
    print(str("|______________________________________________________________|").center(140))

def deleteItem(player, item):
    player.inventory.remove(item)
    print(str(" ___________________________________________________________________").center(140))
    print(str("|                                                                   |").center(140))
    print(str("|          " + str(item).center(15) + "was removed from your inventory.          |").center(140))
    print(str("|___________________________________________________________________|").center(140))

def examItem(item):
    print(str(" _______________________________________________________________________________________________ ").center(100))
    print(str("|                                                                                               |").center(100))
    print(str("|   ", str(item.desc).center(90), "   |").center(100))
    print(str("|_______________________________________________________________________________________________|").center(100))

def fullInventory(player):
    print(str(" ________________________________________________________________________________ ").center(140))
    print(str("|                                                                                |").center(140))
    print(str("|     Your inventory is full. Would you like to delete an item to make room?     |").center(140))
    print(str("|              ____________________            _____________________             |").center(140))
    print(str("|             | 1 | Delete an Item |          | 2 | Keep your Items |            |").center(140))
    print(str("|              ````````````````````            `````````````````````             |").center(140))
    print(str("|________________________________________________________________________________|").center(140))
    print("")
    choice = input(str(":   ").center(140))
    if choice == "1":
        showInventory(player)
        itemX = selectItem(player)
        if itemX == 1:
            cantFindItem()
            selectItem(player)
        elif itemX == 0:
            deleteItem(player, itemX)
            return 0
    elif choice == "2":
        return 1

def cantUseItem():
    print(str(" ___________________________________ ").center(140))
    print(str("|                                   |").center(140))
    print(str("|     This item cannot be used.     |").center(140))
    print(str("|___________________________________|").center(140))

def lockedChest(player):
    check = checkItem(player, "Lockpick")
    if check == 0:
        print(str(" _________________________________________________________________________ ").center(140))
        print(str("|                                                                         |").center(140))
        print(str("|     The chest is locked up tightly. If you have a lockpick, you can     |").center(140))
        print(str("|     simply pick the lock. Or you can always try to break it open.       |").center(140))
        print(str("|                                                                         |").center(140))
        print(str("|                      What would you like to do?                         |").center(140))
        print(str("|                                                                         |").center(140))
        print(str("|                      _________________________                          |").center(140))
        print(str("|                     | 1 |   Use a lockpick.   |                         |").center(140))
        print(str("|                      `````````````````````````                          |").center(140))
        print(str("|                    ______________________________                       |").center(140))
        print(str("|                   | 2 |   Try to break it open   |                      |").center(140))
        print(str("|                    ``````````````````````````````                       |").center(140))
        print(str("|                    _____________________________                        |").center(140))
        print(str("|                   | 3 |   Leave the chest be.   |                       |").center(140))
        print(str("|                    `````````````````````````````                        |").center(140))
        print(str("|_________________________________________________________________________|").center(140))
        print("")
        choice = input(str(":   ").center(140))
    elif check == 1:
        print(str(" _________________________________________________________________________ ").center(140))
        print(str("|                                                                         |").center(140))
        print(str("|     The chest is locked up tightly. If you have a lockpick, you can     |").center(140))
        print(str("|     simply pick the lock. Or you can always try to break it open.       |").center(140))
        print(str("|                                                                         |").center(140))
        print(str("|                      What would you like to do?                         |").center(140))
        print(str("|                                                                         |").center(140))
        print(str("|                    ______________________________                       |").center(140))
        print(str("|                   | 1 |   Try to break it open   |                      |").center(140))
        print(str("|                    ``````````````````````````````                       |").center(140))
        print(str("|                    _____________________________                        |").center(140))
        print(str("|                   | 2 |   Leave the chest be.   |                       |").center(140))
        print(str("|                    `````````````````````````````                        |").center(140))
        print(str("|_________________________________________________________________________|").center(140))
        print("")
        choice = input(str(":   ").center(140))
        if choice == "1":
            choice = "2"
        elif choice == "2":
            choice = "3"
    if choice == "1":
        print(str(" ________________________________________________________________________ ").center(140))
        print(str("|                                                                        |").center(140))
        print(str("|     You use a lockpick and the chest clicks open. Its contents are     |").center(140))
        print(str("|     yours for the taking.                                              |").center(140))
        print(str("|________________________________________________________________________|").center(140))
        deleteItem(player, "Lockpick")
        return 1
    elif choice == "2":
        location = player.location

        if location == 11 or location == 12 or location == 13 or location == 14 or location == 15:
            strCheck = 4 + random.randint(1, 3)
            if player.strength >= strCheck:
                print(str(" ______________________________________________________________________ ").center(140))
                print(str("|                                                                      |").center(140))
                print(str("|     With a few well-placed blows, you smashed through the chest,     |").center(140))
                print(str("|     revealing to you its contents.                                   |").center(140))
                print(str("|______________________________________________________________________|").center(140))
                return 1
            else:
                print(str(" _______________________________________________________________________ ").center(140))
                print(str("|                                                                       |").center(140))
                print(str("|     You pound against the wood of the chest, but it holds sturdy.     |").center(140))
                print(str("|     You just aren't strong enough to break through.                   |").center(140))
                print(str("|_______________________________________________________________________|").center(140))
                return 0
        elif location == 22 or location == 23 or location == 24 or location == 25:
            strCheck = 5 + random.randint(1, 4)
            if player.strength >= strCheck:
                print(str(" ______________________________________________________________________ ").center(140))
                print(str("|                                                                      |").center(140))
                print(str("|     With a few well-placed blows, you smashed through the chest,     |").center(140))
                print(str("|     revealing to you its contents.                                   |").center(140))
                print(str("|______________________________________________________________________|").center(140))
                return 1
            else:
                print(str(" _______________________________________________________________________ ").center(140))
                print(str("|                                                                       |").center(140))
                print(str("|     You pound against the wood of the chest, but it holds sturdy.     |").center(140))
                print(str("|     You just aren't strong enough to break through.                   |").center(140))
                print(str("|_______________________________________________________________________|").center(140))
                return 0
        elif location == 33 or location == 34 or location == 35:
            strCheck = 6 + random.randint(1, 5)
            if player.strength >= strCheck:
                print(str(" ______________________________________________________________________ ").center(140))
                print(str("|                                                                      |").center(140))
                print(str("|     With a few well-placed blows, you smashed through the chest,     |").center(140))
                print(str("|     revealing to you its contents.                                   |").center(140))
                print(str("|______________________________________________________________________|").center(140))
                return 1
            else:
                print(str(" _______________________________________________________________________ ").center(140))
                print(str("|                                                                       |").center(140))
                print(str("|     You pound against the wood of the chest, but it holds sturdy.     |").center(140))
                print(str("|     You just aren't strong enough to break through.                   |").center(140))
                print(str("|_______________________________________________________________________|").center(140))
                return 0
        elif location == 44 or location == 45:
            strCheck = 7 + random.randint(1, 6)
            if player.strength >= strCheck:
                print(str(" ______________________________________________________________________ ").center(140))
                print(str("|                                                                      |").center(140))
                print(str("|     With a few well-placed blows, you smashed through the chest,     |").center(140))
                print(str("|     revealing to you its contents.                                   |").center(140))
                print(str("|______________________________________________________________________|").center(140))
                return 1
            else:
                print(str(" _______________________________________________________________________ ").center(140))
                print(str("|                                                                       |").center(140))
                print(str("|     You pound against the wood of the chest, but it holds sturdy.     |").center(140))
                print(str("|     You just aren't strong enough to break through.                   |").center(140))
                print(str("|_______________________________________________________________________|").center(140))
                return 0
        elif location == 55:
            strCheck = 8 + random.randint(1, 7)
            if player.strength >= strCheck:
                print(str(" ______________________________________________________________________ ").center(140))
                print(str("|                                                                      |").center(140))
                print(str("|     With a few well-placed blows, you smashed through the chest,     |").center(140))
                print(str("|     revealing to you its contents.                                   |").center(140))
                print(str("|______________________________________________________________________|").center(140))
                return 1
            else:
                print(str(" _______________________________________________________________________ ").center(140))
                print(str("|                                                                       |").center(140))
                print(str("|     You pound against the wood of the chest, but it holds sturdy.     |").center(140))
                print(str("|     You just aren't strong enough to break through.                   |").center(140))
                print(str("|_______________________________________________________________________|").center(140))
                return 0
    elif choice == "3":
        print(str(" _______________________________________________________________________ ").center(140))
        print(str("|                                                                       |").center(140))
        print(str("|     You decide that whatever is in the chest isn't worth the time     |").center(140))
        print(str("|     and effort of getting into it.                                    |").center(140))
        print(str("|_______________________________________________________________________|").center(140))
        return 0



#                                   Consumables
class torch (object):
    name = "Torch"
    desc = "A torch will provide both light and heat for a short time."
    price = 20
class lockpick (object):
    name = "Lockpick"
    desc = "A lockpick will get you through anything that's locked."
    price = 20
class shovel (object):
    name = "Shovel"
    desc = "An old, brittle shovel will let you dig through certain obstacles."
    price = 30
class curing_tonic (object):
    name = "Curing Tonic"
    desc = "A tincture that can cure disease and cleanse tainted things."
    price = 30
class holy_water (object):
    name = "Holy Water"
    desc = "A vial of water, blessed by the church, said to purify the unholy."
    price = 40
class health_drop (object):
    name = "Health Drop"
    desc = "When placed under the tonge, it restores some health."
    price = 100
class stimulant_drop (object):
    name = "Stimulant Drop"
    desc = "When placed under the tongue, it restores some energy."
    price = 250
class health_vial (object):
    name = "Health Vial"
    desc = "When ingested, it restores a moderate amount of health."
    price = 300
class stimulant_vial (object):
    name = "Stimulant Vial"
    desc = "When ingested, it restores a moderate amount of energy."
    price = 450
class health_syrum (object):
    name = "Health Syrum"
    desc = "When ingested, it restores a substantial amount of health."
    price = 500
class stimulant_syrum (object):
    name = "Stimulant Syrum"
    desc = "When ingested, it restores a substantial amount of energy."
    price = 700
class health_elixir (object):
    name = "Health Elixir"
    desc = "When ingested, it fully restores your health."
    price = 800
class stimulant_elixir (object):
    name = "Stimulant Elixir"
    desc = "When ingested, it fully restores your energy."
    price = 1000
#                                  Trophies
class vial_of_blood (object):
    name = "Vial of Blood"
    desc = "Blood of a mutant beast that may have... purpose."
    price = 100
class bone_idol (object):
    name = "Bone Idol"
    desc = "A profane idol to some foreign God carved from bone."
    price = 200
class pulsating_mass (object):
    name = "Pulsating Mass"
    desc = "A mass of flesh that seems to still be alive."
    price = 300
class violated_skull (object):
    name = "Violated Skull"
    desc = "A malformed skull with many holes drilled into it."
    price = 400
class drop_of_ichor (object):
    name = "Drop of Ichor"
    desc = "A sample of the black blood that flows through deep dark creatures."
    price = 500
class sanguine_gem (object):
    name = "Sanguine Gem"
    desc = "A scarlet-tinged gem that is quite valubale."
    price = 500
class porcelain_doll (object):
    name = "Porcelain Doll"
    desc = "A brittle doll, cracked and filthy, but an oddity of considerable value."
    price = 1000
class grimoire (object):
    name = "Grimoire"
    desc = "A tome containing lost knowledge of a bygone age that is highly valuable."
    price = 1500
class sunlight_opal (object):
    name = "Sunlight Opal"
    desc = "A white and gold gem that emits a strange warmth. It is eceptionally valuable."
    price = 2000
#                         Level 1 Weapons (3)
class chipped_hatchet (object):
    name = "Chipped Hatchet"
    patk = 4
    matk = 1
    acc = 1
    desc = "An aged hatchet that still packs a punch despite its dullness."
    price = 500
class rusted_shortsword (object):
    name = "Rusted Shortsword"
    patk = 3
    matk = 1
    acc = 2
    desc = "A short blade that has seen an abundence of use."
    price = 500
class hand_crossbow (object):
    name = "Hand Crossbow"
    patk = 2
    matk = 1
    acc = 3
    desc = "A hand-held crossbow, limited in strength, but deadly nonetheless."
    price = 500
class warped_wand (object):
    name = "Warped Wand"
    patk = 1
    matk = 4
    acc = 1
    desc = "A gnarled and twisted wand as crude as the magic it channels."
    price = 500
#                             Level 2 Weapons (6)
class flanged_mace (object):
    name = "Flanged Mace"
    patk = 7
    matk = 1
    acc = 1
    desc = "A heavy mace with many sharp edges."
    price = 1200
class arming_sword (object):
    name = "Arming Sword"
    patk = 5
    matk = 1
    acc = 3
    desc = "A sharpened straight-sword, commonly used by soldiers."
    price = 1200
class light_crossbow (object):
    name = "Light Crossbow"
    patk = 4
    matk = 1
    acc = 4
    desc = "A light-weight crossbow built for both accuracy and range."
    price = 1200
class brimming_cane (object):
    name = "Brimming Cane"
    patk = 2
    matk = 6
    acc = 1
    desc = "A sturdy cane that hums with magical energy."
    price = 1200
#                               Level 3 Weapons (10)
class morningstar (object):
    name = "Morningstar"
    patk = 10
    matk = 1
    acc = 2
    desc = "A vicious mace with many long spikes protruding on the end."
    price = 3000
class flamberge (object):
    name = "Flamberge"
    patk = 8
    matk = 1
    acc = 4
    desc = "A long, ungulating blade that leaves terrible wounds."
    price = 3000
class heavy_crossbow (object):
    name = "Heavy Crossbow"
    patk = 6
    matk = 1
    acc = 6
    desc = "A large-bodied crossbow that packs impressive power and accuracy."
    price = 3000
class obsidian_cane (object):
    name = "Obsidian Cane"
    patk = 2
    matk = 8
    acc = 2
    desc = "An elegently-crafted cane of obsidian that glows with a magical warmth."
    price = 3000
#                                Level 4 Weapons (15)
class halberd (object):
    name = "Halberd"
    patk = 14
    matk = 1
    acc = 3
    desc = "A large, heavy blade fixed to a polearm."
    price = 8000
class zweihander (object):
    name = "Zweihander"
    patk = 12
    matk = 1
    acc = 5
    desc = "A well-balanced sword that is unusually large in stature."
    price = 8000
class arbalest (object):
    name = "Arbalest"
    patk = 9
    matk = 1
    acc = 8
    desc = "A large crossbow that fires with masterful power and precision."
    price = 8000
class scrying_staff (object):
    name = "Scrying Staff"
    patk = 3
    matk = 12
    acc = 3
    desc = "A staff fixed with optical devices. It crackles with magical energy."
    price = 8000
#                                Level 5 Weapons (21)
class granite_maul (object):
    name = "Granite Maul"
    patk = 20
    matk = 1
    acc = 3
    desc = "A mighty hammer of rediculous size. The head is a solid block of granite."
    price = 12000
class terror_sword (object):
    name = "Terror Sword"
    patk = 15
    matk = 4
    acc = 5
    desc = "A wicked sword of grim origin. Its blade is jagged and black."
    price = 12000
class foreign_rifle (object):
    name = "Foreign Rifle"
    patk = 14
    matk = 1
    acc = 9
    desc = "A strange and foreign weapon that fires projectiles with frightening power."
    price = 12000
class trismegistus (object):
    name = "Trismegistus"
    patk = 5
    matk = 14
    acc = 5
    desc = "A mysterious staff marked with symbols of a strange and ancient deity."
    price = 12000
#                                Level 1 Armor (3)
class chain_hauberk (object):
    name = "Chain Hauberk"
    pdfn = 4
    mdfn = 1
    eva = 1
    desc = "A shirt of finely-linked chain."
    price = 800
class padded_jacket (object):
    name = "Padded Jacket"
    pdfn = 2
    mdfn = 1
    eva = 3
    desc = "A thick overcoat, padded with hardened leather."
    price = 800
class cloth_garb (object):
    name = "Cloth Garb"
    pdfn = 1
    mdfn = 3
    eva = 2
    desc = "A comfortable outfit of fine cloth."
    price = 800
#                                Level 2 Armor (6)
class reinforced_mail (object):
    name = "Reinforced Mail"
    pdfn = 7
    mdfn = 1
    eva =  1
    desc = "A suit of linked chains, reinforced by hardened leather."
    price = 1500
class rogues_coat (object):
    name = "Rogues Coat"
    pdfn = 4
    mdfn = 1
    eva = 4
    desc = "A chain shirt beneath a leather coat with many pockets."
    price = 1500
class dashing_suit (object):
    name = "Dashing Suit"
    pdfn = 2
    mdfn = 5
    eva = 2
    desc = "A fancy suit with odd symbols stiched into it."
    price = 1500
#                                Level 3 Armor (10)
class heavy_lamellar (object):
    name = "Heavy Lamellar"
    pdfn = 11
    mdfn = 1
    eva = 1
    desc = "A body composed of overlapping, horizontal rows of metal and leather."
    price = 4000
class brigandine (object):
    name = "Brigandine"
    pdfn = 7
    mdfn = 1
    eva = 5
    desc = "A leather garment lined with metal plates riveted to the fabric."
    price = 4000
class silk_robe (object):
    name = "Silk Robe"
    pdfn = 2
    mdfn = 8
    eva = 3
    desc = "A robe sewn of fine silk that buffers one from magic."
    price = 4000
#                                Level 4 Armor (15)
class steel_cuirass (object):
    name = "Steel Cuirass"
    pdfn = 16
    mdfn = 1
    eva = 1
    desc = "A breastplate of steel for ultimate protection."
    price = 7500
class threaded_coat (object):
    name = "Threaded Coat"
    pdfn = 7
    mdfn = 3
    eva = 8
    desc = "An exquisit coat with steel threads sewn throughout the fabric."
    price =7500
class magus_suit (object):
    name = "Magus Suit"
    pdfn = 3
    mdfn = 12
    eva = 3
    desc = "A regal suit crafted by the magi for the purpose of warding magic."
    price = 7500
#                                Level 5 Armor (21)
class kastenburst_suit (object):
    name = "Kastenbrust Suit"
    pdfn = 22
    mdfn = 1
    eva = 1
    desc = "A full suit of masterfully crafted armor worn by many a legendary knight."
    price = 10000
class black_hide_jacket (object):
    name = "Black Hide Jacket"
    pdfn = 10
    mdfn = 5
    eva = 8
    desc = "A unique jacket fashioned from the hide of the mythical black beast."
    price = 10000
class warlock_regalia (object):
    name = "Warlock Regalia"
    pdfn = 3
    mdfn = 16
    eva = 5
    desc = "A bizarre outfit fixed with trinkets and symbols of occult origins."
    price = 10000

def equipWeapon(player, item):
    player.weapon = item
    initEquipment(player)
    print(str(" _______________________________________________________ ").center(140))
    print(str("|                                                       |").center(140))
    print(str("|       You are now wielding a" + str(item).center(20) + "!     |").center(140))
    print(str("|_______________________________________________________|").center(140))
def equipArmor(player, item):
    player.armor = item
    initEquipment(player)
    print(str(" ______________________________________________________ ").center(140))
    print(str("|                                                      |").center(140))
    print(str("|       You are now wearing a" + str(item).center(20) + "!     |").center(140))
    print(str("|______________________________________________________|").center(140))

def initEquipment(player):
    while player.weapon == "Chipped Hatchet":
        wepBonus = [chipped_hatchet.patk, chipped_hatchet.matk, chipped_hatchet.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Rusted Shortsword":
        wepBonus = [rusted_shortsword.patk, rusted_shortsword.matk, rusted_shortsword.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Hand Crossbow":
        wepBonus = [hand_crossbow.patk, hand_crossbow.matk, hand_crossbow.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Warped Wand":
        wepBonus = [warped_wand.patk, warped_wand.matk, warped_wand.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Flanged Mace":
        wepBonus = [flanged_mace.patk, flanged_mace.matk, flanged_mace.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Arming Sword":
        wepBonus = [arming_sword.patk, arming_sword.matk, arming_sword.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Light Crossbow":
        wepBonus = [light_crossbow.patk, light_crossbow.matk, light_crossbow.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Brimming Cane":
        wepBonus = [brimming_cane.patk, brimming_cane.matk, brimming_cane.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Morningstar":
        wepBonus = [morningstar.patk, morningstar.matk, morningstar.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Flamberge":
        wepBonus = [flamberge.patk, flamberge.matk, flamberge.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Heavy Crossbow":
        wepBonus = [heavy_crossbow.patk, heavy_crossbow.matk, heavy_crossbow.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Obsidian Cane":
        wepBonus = [obsidian_cane.patk, obsidian_cane.matk, obsidian_cane.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Halberd":
        wepBonus = [halberd.patk, halberd.matk, halberd.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Zweihander":
        wepBonus = [zweihander.patk, zweihander.matk, zweihander.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Arbalest":
        wepBonus = [arbalest.patk, arbalest.matk, arbalest.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Scrying Staff":
        wepBonus = [scrying_staff.patk, scrying_staff.matk, scrying_staff.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Granite Maul":
        wepBonus = [granite_maul.patk, granite_maul.matk, granite_maul.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Terror Sword":
        wepBonus = [terror_sword.patk, terror_sword.matk, terror_sword.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Foreign Rifle":
        wepBonus = [foreign_rifle.patk, foreign_rifle.matk, foreign_rifle.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break
    while player.weapon == "Trismegistus":
        wepBonus = [trismegistus.patk, trismegistus.matk, trismegistus.acc]
        player.physicalAttack = wepBonus[0]
        player.magicAttack = wepBonus[1]
        player.accuracy = wepBonus[2]
        break

    while player.armor == "Chain Hauberk":
        armBonus = [chain_hauberk.pdfn, chain_hauberk.mdfn, chain_hauberk.eva]
        player.physicalDefense = armBonus[0]
        player.magicDefense = armBonus[1]
        player.evade = armBonus[2]
        break
    while player.armor == "Padded Jacket":
        armBonus = [padded_jacket.pdfn, padded_jacket.mdfn, padded_jacket.eva]
        player.physicalDefense = armBonus[0]
        player.magicDefense = armBonus[1]
        player.evade = armBonus[2]
        break
    while player.armor == "Cloth Garb":
        armBonus = [cloth_garb.pdfn, cloth_garb.mdfn, cloth_garb.eva]
        player.physicalDefense = armBonus[0]
        player.magicDefense = armBonus[1]
        player.evade = armBonus[2]
        break
    while player.armor == "Reinforced Mail":
        armBonus = [reinforced_mail.pdfn, reinforced_mail.mdfn, reinforced_mail.eva]
        player.physicalDefense = armBonus[0]
        player.magicDefense = armBonus[1]
        player.evade = armBonus[2]
        break
    while player.armor == "Rogues Coat":
        armBonus = [rogues_coat.pdfn, rogues_coat.mdfn, rogues_coat.eva]
        player.physicalDefense = armBonus[0]
        player.magicDefense = armBonus[1]
        player.evade = armBonus[2]
        break
    while player.armor == "Dashing Suit":
        armBonus = [dashing_suit.pdfn, dashing_suit.mdfn, dashing_suit.eva]
        player.physicalDefense = armBonus[0]
        player.magicDefense = armBonus[1]
        player.evade = armBonus[2]
        break
    while player.armor == "Heavy Lamellar":
        armBonus = [heavy_lamellar.pdfn, heavy_lamellar.mdfn, heavy_lamellar.eva]
        player.physicalDefense = armBonus[0]
        player.magicDefense = armBonus[1]
        player.evade = armBonus[2]
        break
    while player.armor == "Brigandine":
        armBonus = [brigandine.pdfn, brigandine.mdfn, brigandine.eva]
        player.physicalDefense = armBonus[0]
        player.magicDefense = armBonus[1]
        player.evade = armBonus[2]
        break
    while player.armor == "Silk Robe":
        armBonus = [silk_robe.pdfn, silk_robe.mdfn, silk_robe.eva]
        player.physicalDefense = armBonus[0]
        player.magicDefense = armBonus[1]
        player.evade = armBonus[2]
        break
    while player.armor == "Steel Cuirass":
        armBonus = [steel_cuirass.pdfn, steel_cuirass.mdfn, steel_cuirass.eva]
        player.physicalDefense = armBonus[0]
        player.magicDefense = armBonus[1]
        player.evade = armBonus[2]
        break
    while player.armor == "Black Hide Jacket":
        armBonus = [black_hide_jacket.pdfn, black_hide_jacket.mdfn, black_hide_jacket.eva]
        player.physicalDefense = armBonus[0]
        player.magicDefense = armBonus[1]
        player.evade = armBonus[2]
        break
    while player.armor == "Warlock Regalia":
        armBonus = [warlock_regalia.pdfn, warlock_regalia.mdfn, warlock_regalia.eva]
        player.physicalDefense = armBonus[0]
        player.magicDefense = armBonus[1]
        player.evade = armBonus[2]
        break

def useHealthDrop(player):
    heal = random.randint(2, 5) * 2
    newHealth = player.healthPoints + heal
    if newHealth > player.maxHealthPoints:
        newHealth = player.maxHealthPoints
    player.healthPoints = newHealth
    deleteItem(player, "Health Drop")
    print(str(" _______________________________________________________ ").center(140))
    print(str("|                                                       |").center(140))
    print(str("|     The Health Drop restores" + str(heal).center(2) + "points of health.     |").center(140))
    print(str("|_______________________________________________________|").center(140).center(140))
def useHealthVial(player):
    heal = random.randint(4, 10) * 2
    newHealth = player.healthPoints + heal
    if newHealth > player.maxHealthPoints:
        newHealth = player.maxHealthPoints
    player.healthPoints = newHealth
    deleteItem(player, "Health Vial")
    print(str(" _______________________________________________________ ").center(140))
    print(str("|                                                       |").center(140))
    print(str("|     The Health Vial restores" + str(heal).center(2) + "points of health.     |").center(140))
    print(str("|_______________________________________________________|").center(140).center(140))
def useHealthSyrum(player):
    heal = random.randint(8, 15) * 2
    newHealth = player.healthPoints + heal
    if newHealth > player.maxHealthPoints:
        newHealth = player.maxHealthPoints
    player.healthPoints = newHealth
    deleteItem(player, "Health Syrum")
    print(str(" ________________________________________________________ ").center(140))
    print(str("|                                                        |").center(140))
    print(str("|     The Health Syrum restores" + str(heal).center(2) + "points of health.     |").center(140))
    print(str("|________________________________________________________|").center(140).center(140))
def useHealthElixir(player):
    heal = random.randint(10, 20) * 2
    newHealth = player.healthPoints + heal
    if newHealth > player.maxHealthPoints:
        newHealth = player.maxHealthPoints
    player.healthPoints = newHealth
    deleteItem(player, "Health Elixir")
    print(str(" _________________________________________________________ ").center(140))
    print(str("|                                                         |").center(140))
    print(str("|     The Health Elixir restores" + str(heal).center(2) + "points of health.     |").center(140))
    print(str("|_________________________________________________________|").center(140).center(140))
def useStimulantDrop(player):
    heal = random.randint(2, 5)
    newEnergy = player.energyPoints + heal
    if newEnergy > player.maxEnergy:
        newEnergy = player.maxEnergy
    player.energyPoints = newEnergy
    deleteItem(player, "Stimulant Drop")
    print(str(" __________________________________________________________ ").center(140))
    print(str("|                                                          |").center(140))
    print(str("|     The Stimulant Drop restores" + str(heal).center(2) + "points of energy.     |").center(140))
    print(str("|__________________________________________________________|").center(140).center(140))
def useStimulantVial(player):
    heal = random.randint(4, 10)
    newEnergy = player.energyPoints + heal
    if newEnergy > player.maxEnergy:
        newEnergy = player.maxEnergy
    player.energyPoints = newEnergy
    deleteItem(player, "Stimulant Drop")
    print(str(" __________________________________________________________ ").center(140))
    print(str("|                                                          |").center(140))
    print(str("|     The Stimulant Drop restores" + str(heal).center(2) + "points of energy.     |").center(140))
    print(str("|__________________________________________________________|").center(140).center(140))
def useStimulantSyrum(player):
    heal = random.randint(8, 15)
    newEnergy = player.energyPoints + heal
    if newEnergy > player.maxEnergy:
        newEnergy = player.maxEnergy
    player.energyPoints = newEnergy
    deleteItem(player, "Stimulant Drop")
    print(str(" __________________________________________________________ ").center(140))
    print(str("|                                                          |").center(140))
    print(str("|     The Stimulant Drop restores" + str(heal).center(2) + "points of energy.     |").center(140))
    print(str("|__________________________________________________________|").center(140).center(140))
def useStimulantElixir(player):
    heal = random.randint(10, 20)
    newEnergy = player.energyPoints + heal
    if newEnergy > player.maxEnergy:
        newEnergy = player.maxEnergy
    player.energyPoints = newEnergy
    deleteItem(player, "Stimulant Drop")
    print(str(" __________________________________________________________ ").center(140))
    print(str("|                                                          |").center(140))
    print(str("|     The Stimulant Drop restores" + str(heal).center(2) + "points of energy.     |").center(140))
    print(str("|__________________________________________________________|").center(140).center(140))

def lootTable(player):
    sizeRoll = random.randint(1, 6)
    location = player.location
    if location == 11 or location == 12 or location == 13 or location == 14 or location == 15:
        consumables = [health_drop, stimulant_drop, torch, lockpick, shovel]
        valuables = [vial_of_blood, sanguine_gem]
        weapons = [chipped_hatchet, rusted_shortsword, hand_crossbow, warped_wand]
        armors = [chain_hauberk, padded_jacket, cloth_garb]
        if sizeRoll <= 5:
            typeRoll = random.randint(1, 3)
            if typeRoll == 1 or typeRoll == 2:
                itemRoll = random.randint(1, len(consumables)) - 1
                addItem(player, consumables[itemRoll].name)
            elif typeRoll == 3:
                itemRoll = random.randint(1, len(valuables)) - 1
                addItem(player, valuables[itemRoll].name)
        elif sizeRoll == 6 or sizeRoll == 7:
            typeRoll = random.randint(1, 7)
            if typeRoll == 1:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
            elif typeRoll == 2:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
            elif typeRoll == 3:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
            elif typeRoll == 4:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
            elif typeRoll == 5:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
            elif typeRoll == 6:
                itemRoll1 = random.randint(1, len(valuables)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                addItem(player, valuables[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
            elif typeRoll == 7:
                itemRoll1 = random.randint(1, len(valuables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, valuables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
        elif sizeRoll == 8:
            typeRoll = random.randint(1, 10)
            if typeRoll == 1:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(consumables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 2:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 3:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 4:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(consumables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 5:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 6:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 7:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(consumables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 8:
                itemRoll1 = random.randint(1, len(valuables)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, valuables[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 9:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(valuables))
                addItem(player, consumables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 10:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
    elif location == 22 or location == 23 or location == 24 or location == 25:
        consumables = [health_vial, stimulant_vial, torch, lockpick, shovel, curing_tonic]
        valuables = [vial_of_blood, sanguine_gem, bone_idol]
        weapons = [flanged_mace, arming_sword, light_crossbow, brimming_cane]
        armors = [reinforced_mail, rogues_coat, dashing_suit]
        if sizeRoll <= 3:
            typeRoll = random.randint(1, 2)
            if typeRoll == 1:
                itemRoll = random.randint(1, len(consumables)) - 1
                addItem(player, consumables[itemRoll].name)
            elif typeRoll == 2:
                itemRoll = random.randint(1, len(valuables)) - 1
                addItem(player, valuables[itemRoll].name)
        elif sizeRoll == 4 or sizeRoll == 5:
            typeRoll = random.randint(1, 7)
            if typeRoll == 1:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
            elif typeRoll == 2:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
            elif typeRoll == 3:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(consumables) - 1)
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
            elif typeRoll == 4:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
            elif typeRoll == 5:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
            elif typeRoll == 6:
                itemRoll1 = random.randint(1, len(valuables)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                addItem(player, valuables[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
            elif typeRoll == 7:
                itemRoll1 = random.randint(1, len(valuables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, valuables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
        elif sizeRoll == 6:
            typeRoll = random.randint(1, 10)
            if typeRoll == 1:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(consumables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 2:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 3:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 4:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(consumables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 5:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 6:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 7:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(consumables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 8:
                itemRoll1 = random.randint(1, len(valuables)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, valuables[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 9:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 10:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
    elif location == 33 or location == 34 or location == 35:
        consumables = [health_vial, stimulant_vial, torch, lockpick, shovel, curing_tonic, holy_water]
        valuables = [vial_of_blood, sanguine_gem, bone_idol, pulsating_mass, porcelain_doll]
        weapons = [morningstar, flamberge, heavy_crossbow, obsidian_cane]
        armors = [heavy_lamellar, brigandine, silk_robe]
        if sizeRoll <= 3:
            typeRoll = random.randint(1, 2)
            if typeRoll == 1:
                itemRoll = random.randint(1, len(consumables)) - 1
                addItem(player, consumables[itemRoll].name)
            elif typeRoll == 2:
                itemRoll = random.randint(1, len(valuables)) - 1
                addItem(player, valuables[itemRoll].name)
        elif sizeRoll == 4 or sizeRoll == 5:
            typeRoll = random.randint(1, 7)
            if typeRoll == 1:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
            elif typeRoll == 2:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
            elif typeRoll == 3:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
            elif typeRoll == 4:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
            elif typeRoll == 5:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
            elif typeRoll == 6:
                itemRoll1 = random.randint(1, len(valuables)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                addItem(player, valuables[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
            elif typeRoll == 7:
                itemRoll1 = random.randint(1, len(valuables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, valuables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
        elif sizeRoll == 6:
            typeRoll = random.randint(1, 10)
            if typeRoll == 1:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(consumables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 2:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 3:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 4:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(consumables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 5:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 6:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 7:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(consumables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 8:
                itemRoll1 = random.randint(1, len(valuables)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, valuables[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 9:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 10:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
    elif location == 44 or location == 45:
        consumables = [health_vial, stimulant_vial, torch, lockpick, shovel, curing_tonic, holy_water]
        valuables = [vial_of_blood, sanguine_gem, bone_idol, porcelain_doll, pulsating_mass, violated_skull, grimoire]
        weapons = [halberd, zweihander, arbalest, scrying_staff]
        armors = [steel_cuirass, threaded_coat, magus_suit]
        if sizeRoll <= 3:
            typeRoll = random.randint(1, 2)
            if typeRoll == 1:
                itemRoll = random.randint(1, len(consumables)) - 1
                addItem(player, consumables[itemRoll].name)
            elif typeRoll == 2:
                itemRoll = random.randint(1, len(valuables)) - 1
                addItem(player, valuables[itemRoll].name)
        elif sizeRoll == 4 or sizeRoll == 5:
            typeRoll = random.randint(1, 7)
            if typeRoll == 1:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
            elif typeRoll == 2:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
            elif typeRoll == 3:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
            elif typeRoll == 4:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
            elif typeRoll == 5:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
            elif typeRoll == 6:
                itemRoll1 = random.randint(1, len(valuables)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                addItem(player, valuables[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
            elif typeRoll == 7:
                itemRoll1 = random.randint(1, len(valuables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, valuables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
        elif sizeRoll == 6:
            typeRoll = random.randint(1, 10)
            if typeRoll == 1:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(consumables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 2:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 3:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 4:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(consumables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 5:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 6:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 7:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(consumables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 8:
                itemRoll1 = random.randint(1, len(valuables)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, valuables[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 9:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 10:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
    elif location == 55:
        consumables = [health_vial, stimulant_vial, torch, lockpick, shovel, curing_tonic, holy_water]
        valuables = [vial_of_blood, sanguine_gem, bone_idol, porcelain_doll, pulsating_mass, violated_skull, grimoire, drop_of_ichor, sunlight_opal]
        weapons = [granite_maul, terror_sword, foreign_rifle, trismegistus]
        armors = [kastenburst_suit, black_hide_jacket, warlock_regalia]
        if sizeRoll <= 3:
            typeRoll = random.randint(1, 2)
            if typeRoll == 1:
                itemRoll = random.randint(1, len(consumables)) - 1
                addItem(player, consumables[itemRoll].name)
            elif typeRoll == 2:
                itemRoll = random.randint(1, len(valuables)) - 1
                addItem(player, valuables[itemRoll].name)
        elif sizeRoll == 4 or sizeRoll == 5:
            typeRoll = random.randint(1, 7)
            if typeRoll == 1:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
            elif typeRoll == 2:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
            elif typeRoll == 3:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
            elif typeRoll == 4:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
            elif typeRoll == 5:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
            elif typeRoll == 6:
                itemRoll1 = random.randint(1, len(valuables)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                addItem(player, valuables[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
            elif typeRoll == 7:
                itemRoll1 = random.randint(1, len(valuables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                addItem(player, valuables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
        elif sizeRoll == 6:
            typeRoll = random.randint(1, 10)
            if typeRoll == 1:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(consumables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 2:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 3:
                itemRoll1 = random.randint(1, len(weapons)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, weapons[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 4:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(consumables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 5:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 6:
                itemRoll1 = random.randint(1, len(armors)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, armors[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 7:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(consumables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, consumables[itemRoll3].name)
            elif typeRoll == 8:
                itemRoll1 = random.randint(1, len(valuables)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, valuables[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 9:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(consumables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, consumables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)
            elif typeRoll == 10:
                itemRoll1 = random.randint(1, len(consumables)) - 1
                itemRoll2 = random.randint(1, len(valuables)) - 1
                itemRoll3 = random.randint(1, len(valuables)) - 1
                addItem(player, consumables[itemRoll1].name)
                addItem(player, valuables[itemRoll2].name)
                addItem(player, valuables[itemRoll3].name)

def findGold(player, size):
    if size == 1:
        roll = random.randint(10, 50)
    elif size == 2:
        roll = random.randint(50, 100)
    elif size == 3:
        roll = random.randint(100, 250)
    elif size == 4:
        roll = random.randint(250, 500)
    elif size == 5:
        roll = random.randint(500, 1000)
    print(str("|     You found" + str(roll).center(2) + "pieces of gold.     |").center(140))
    player.gold = player.gold + roll

def starterKit(player):
    print(str(" __________________________________________________________________________________ ").center(140))
    print(str("|                                                                                  |").center(140))
    print(str("|     You will face many trials along the way. You will need these to survive.     |").center(140))
    print(str("|__________________________________________________________________________________|").center(140))
    if player.name == "Knight":
        addItem(player, "Rusted Shortsword")
        addItem(player, "Health Drop")
        addItem(player, "Health Drop")
        addItem(player, "Health Drop")
        addItem(player, "Shovel")
    elif player.name == "Hunter":
        addItem(player, "Hand Crossbow")
        addItem(player, "Health Drop")
        addItem(player, "Health Drop")
        addItem(player, "Stimulant Drop")
        addItem(player, "Torch")
    elif player.name == "Scholar":
        addItem(player, "Warped Wand")
        addItem(player, "Health Drop")
        addItem(player, "Stimulant Drop")
        addItem(player, "Stimulant Drop")
        addItem(player, "Lockpick")
    player.gold = player.gold + 100

itemDB = [torch, lockpick, shovel, curing_tonic, holy_water, health_drop, stimulant_drop, health_vial, stimulant_vial, health_syrum, stimulant_syrum, health_elixir, stimulant_elixir, vial_of_blood, bone_idol, pulsating_mass, violated_skull, drop_of_ichor, sanguine_gem, porcelain_doll, grimoire, sunlight_opal, chipped_hatchet, rusted_shortsword, hand_crossbow, warped_wand, flanged_mace, arming_sword, light_crossbow, brimming_cane, morningstar, flamberge, heavy_crossbow, obsidian_cane, halberd, zweihander, arbalest, scrying_staff, granite_maul, terror_sword, foreign_rifle, trismegistus, chain_hauberk, padded_jacket, cloth_garb, reinforced_mail, rogues_coat, dashing_suit, heavy_lamellar, brigandine, silk_robe, steel_cuirass, threaded_coat, magus_suit, kastenburst_suit, black_hide_jacket, warlock_regalia]


