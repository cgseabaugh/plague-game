

from machines.inventory import *
from machines.abilities import *

def merchOptions():
    print(str(" ________________________________________________________________________ ").center(140))
    print(str("|                                                                        |").center(140))
    print(str("|      __________________       ______________       ______________      |").center(140))
    print(str("|     | 1 |   Purchase   |     | 2 |   Sell   |     | 3 |   Back   |     |").center(140))
    print(str("|      ``````````````````       ``````````````       ``````````````      |").center(140))
    print(str("|________________________________________________________________________|").center(140))
    x = input(str(":  ").rjust(70))
    return int(x)

def ablMerchOptions():
    print(str(" ________________________________________________________________________ ").center(140))
    print(str("|                                                                        |").center(140))
    print(str("|           __________________________            ______________         |").center(140))
    print(str("|          | 1 |   Learn an Ability   |          | 2 |   Back   |        |").center(140))
    print(str("|           ``````````````````````````            ``````````````         |").center(140))
    print(str("|________________________________________________________________________|").center(140))
    x = input(str(":  ").rjust(70))
    return int(x)



def genMerchTable(player):
    location = player.location
    if location == 11 or location == 12 or location == 13 or location == 14 or location == 15:
        stock = [torch, lockpick, shovel, health_drop, stimulant_drop]
    elif location == 22 or location == 23 or location == 24 or location == 25:
        stock = [torch, lockpick, shovel, curing_tonic, health_drop, health_vial, stimulant_drop, stimulant_vial]
    elif location == 33 or location == 34 or location == 35:
        stock = [torch, lockpick, shovel, curing_tonic, holy_water, health_vial, health_syrum, stimulant_vial, stimulant_syrum]
    elif location == 44 or location == 45:
        stock = [torch, lockpick, shovel, curing_tonic, holy_water, health_syrum, health_elixir, stimulant_syrum, stimulant_elixir]
    elif location == 55:
        stock = [torch, lockpick, shovel, curing_tonic, holy_water, health_elixir, stimulant_elixir]
    print(str(" ______________________________________________________________________________________________________________ ").center(140))
    print(str("|    ______________________________________________________________________________________________________    |").center(140))
    print(str("|   |      Item Name     |                              Description                             |   Price  |   |").center(140))
    print(str("|   |````````````````````|``````````````````````````````````````````````````````````````````````|``````````|   |").center(140))
    for x in stock:
        print(str("|   |" + str(x.name).center(20) + "|" + str(x.desc).center(70) + "|" + str(x.price).center(10) + "|   |").center(140))
    print(str("|   |____________________|______________________________________________________________________|__________|   |").center(140))
    print(str("|                                                                                               |   Gold   |   |").center(140))
    print(str("|                                                  ______________                               |``````````|   |").center(140))
    print(str("|                                                 | 1 |   Back   |                              |  " + str(player.gold).center(5) + "   |   |").center(140))
    print(str("|                                                  ``````````````                               |__________|   |").center(140))
    print(str("|______________________________________________________________________________________________________________|").center(140))
    print("")
    itemX = input(str(" Type an Item to purchase: ").rjust(60))
    for item in stock:
        if item.name == itemX:
            print(str(" ________________________________________________________________________ ").center(140))
            print(str("|                                                                        |").center(140))
            print(str("|     Do you want to purchase a " + str(item.name).center(20) + " for " + str(item.price).center(5) + " gold?     |").center(140))
            print(str("|             __________________            ______________               |").center(140))
            print(str("|            | 1 |   Purchase   |          | 2 |   Back   |              |").center(140))
            print(str("|             ``````````````````            ``````````````               |").center(140))
            print(str("|________________________________________________________________________|").center(140))
            choice = input(str(": ").rjust(60))
            if choice == "1":
                if player.gold >= item.price:
                    addItem(player, item.name)
                    player.gold = player.gold - item.price
                else:
                    print(str(" _____________________________________ ").center(140))
                    print(str("|                                     |").center(140))
                    print(str("|     You can't afford that item.     |").center(140))
                    print(str("|_____________________________________|").center(140))

def wepMerchTable(player):
    location = player.location
    if location == 11 or location == 12 or location == 13 or location == 14 or location == 15:
        stock = [chipped_hatchet, rusted_shortsword, hand_crossbow, warped_wand]
    elif location == 22 or location == 23 or location == 24 or location == 25:
        stock = [flanged_mace, arming_sword, light_crossbow, brimming_cane]
    elif location == 33 or location == 34 or location == 35:
        stock = [morningstar, flamberge, heavy_crossbow, obsidian_cane]
    elif location == 44 or location == 45:
        stock = [halberd, zweihander, arbalest, scrying_staff]
    elif location == 55:
        stock = [granite_maul, terror_sword, foreign_rifle, trismegistus]
    print(str(" ______________________________________________________________________________________________________________ ").center(140))
    print(str("|    ______________________________________________________________________________________________________    |").center(140))
    print(str("|   |      Item Name     |                              Description                             |   Price  |   |").center(140))
    print(str("|   |````````````````````|``````````````````````````````````````````````````````````````````````|``````````|   |").center(140))
    for x in stock:
        print(str("|   |" + str(x.name).center(20) + "|" + str(x.desc).center(70) + "|" + str(x.price).center(10) + "|   |").center(140))
    print(str("|   |____________________|______________________________________________________________________|__________|   |").center(140))
    print(str("|                                                                                               |   Gold   |   |").center(140))
    print(str("|                                                  ______________                               |``````````|   |").center(140))
    print(str("|                                                 | 1 |   Back   |                              |  " + str(player.gold).center(5) + "   |   |").center(140))
    print(str("|                                                  ``````````````                               |__________|   |").center(140))
    print(str("|______________________________________________________________________________________________________________|").center(140))
    print("")
    itemX = input(str(" Type an Item to purchase: ").rjust(60))
    for item in stock:
        if item.name == itemX:
            print(str(" ________________________________________________________________________ ").center(140))
            print(str("|                                                                        |").center(140))
            print(str("|     Do you want to purchase a " + str(item.name).center(20) + " for " + str(item.price).center(5) + " gold?     |").center(140))
            print(str("|             __________________            ______________               |").center(140))
            print(str("|            | 1 |   Purchase   |          | 2 |   Back   |              |").center(140))
            print(str("|             ``````````````````            ``````````````               |").center(140))
            print(str("|________________________________________________________________________|").center(140))
            choice = input(str(": ").rjust(60))
            if choice == "1":
                if player.gold >= item.price:
                    addItem(player, item.name)
                    player.gold = player.gold - item.price
                else:
                    print(str(" _____________________________________ ").center(140))
                    print(str("|                                     |").center(140))
                    print(str("|     You can't afford that item.     |").center(140))
                    print(str("|_____________________________________|").center(140))

def armorMerchTable(player):
    location = player.location
    if location == 11 or location == 12 or location == 13 or location == 14 or location == 15:
        stock = [chain_hauberk, padded_jacket, cloth_garb]
    elif location == 22 or location == 23 or location == 24 or location == 25:
        stock = [reinforced_mail, rogues_coat, dashing_suit]
    elif location == 33 or location == 34 or location == 35:
        stock = [heavy_lamellar, brigandine, silk_robe]
    elif location == 44 or location == 45:
        stock = [steel_cuirass, threaded_coat, magus_suit]
    elif location == 55:
        stock = [kastenburst_suit, black_hide_jacket, warlock_regalia]
    print(str(" ______________________________________________________________________________________________________________ ").center(140))
    print(str("|    ______________________________________________________________________________________________________    |").center(140))
    print(str("|   |      Item Name     |                              Description                             |   Price  |   |").center(140))
    print(str("|   |````````````````````|``````````````````````````````````````````````````````````````````````|``````````|   |").center(140))
    for x in stock:
        print(str("|   |" + str(x.name).center(20) + "|" + str(x.desc).center(70) + "|" + str(x.price).center(10) + "|   |").center(140))
    print(str("|   |____________________|______________________________________________________________________|__________|   |").center(140))
    print(str("|                                                                                               |   Gold   |   |").center(140))
    print(str("|                                                  ______________                               |``````````|   |").center(140))
    print(str("|                                                 | 1 |   Back   |                              |  " + str(player.gold).center(5) + "   |   |").center(140))
    print(str("|                                                  ``````````````                               |__________|   |").center(140))
    print(str("|______________________________________________________________________________________________________________|").center(140))
    print("")
    itemX = input(str(" Type an Item to purchase: ").rjust(60))
    for item in stock:
        if item.name == itemX:
            print(str(" ________________________________________________________________________ ").center(140))
            print(str("|                                                                        |").center(140))
            print(str("|     Do you want to purchase a " + str(item.name).center(20) + " for " + str(item.price).center(5) + " gold?     |").center(140))
            print(str("|             __________________            ______________               |").center(140))
            print(str("|            | 1 |   Purchase   |          | 2 |   Back   |              |").center(140))
            print(str("|             ``````````````````            ``````````````               |").center(140))
            print(str("|________________________________________________________________________|").center(140))
            choice = input(str(": ").rjust(60))
            if choice == "1":
                if player.gold >= item.price:
                    addItem(player, item.name)
                    player.gold = player.gold - item.price
                else:
                    print(str(" _____________________________________ ").center(140))
                    print(str("|                                     |").center(140))
                    print(str("|     You can't afford that item.     |").center(140))
                    print(str("|_____________________________________|").center(140))

def abilityMerchTable(player):
    location = player.location
    if location == 11 or location == 12 or location == 13 or location == 14 or location == 15:
        stock = [vital_blow, black_powder, blast_bolt]
    elif location == 22 or location == 23 or location == 24 or location == 25:
        stock = [vital_blow, black_powder, blast_bolt, candlelight]
    elif location == 33 or location == 34 or location == 35:
        stock = [vital_blow, black_powder, blast_bolt, candlelight, shield_stance]
    elif location == 44 or location == 45:
        stock = [vital_blow, black_powder, blast_bolt, candlelight, shield_stance, bolas]
    elif location == 55:
        stock = [vital_blow, black_powder, blast_bolt, candlelight, shield_stance, bolas, immolate]
    print(str(" ______________________________________________________________________________________________________________ ").center(140))
    print(str("|    ______________________________________________________________________________________________________    |").center(140))
    print(str("|   |    Ability Name    |                              Description                             |   Price  |   |").center(140))
    print(str("|   |````````````````````|``````````````````````````````````````````````````````````````````````|``````````|   |").center(140))
    for x in stock:
        print(str("|   |" + str(x.name).center(20) + "|" + str(x.desc).center(70) + "|" + str(x.price).center(10) + "|   |").center(140))
    print(str("|   |____________________|______________________________________________________________________|__________|   |").center(140))
    print(str("|                                                                                               | Insight  |   |").center(140))
    print(str("|                                                  ______________                               |``````````|   |").center(140))
    print(str("|                                                 | 1 |   Back   |                              |  " + str(player.insight).center(5) + "   |   |").center(140))
    print(str("|                                                  ``````````````                               |__________|   |").center(140))
    print(str("|______________________________________________________________________________________________________________|").center(140))
    print("")
    abilityX = input(str(" Type an Ability to learn: ").rjust(60))
    for ability in stock:
        if ability.name == abilityX:
            print(str(" ________________________________________________________________________ ").center(140))
            print(str("|                                                                        |").center(140))
            print(str("|     Do you want to learn " + str(ability.name).center(20) + " for " + str(item.price).center(5) + " insight?     |").center(140))
            print(str("|             __________________            ______________               |").center(140))
            print(str("|            | 1 |   Purchase   |          | 2 |   Back   |              |").center(140))
            print(str("|             ``````````````````            ``````````````               |").center(140))
            print(str("|________________________________________________________________________|").center(140))
            choice = input(str(": ").rjust(60))
            if choice == "1":
                if player.insight >= ability.price:
                    learned = addAbility(player, ability.name)
                    if learned == 0:
                        player.insight = player.insight - ability.price
                else:
                    print(str(" _________________________________________________ ").center(140))
                    print(str("|                                                 |").center(140))
                    print(str("|     You can't learn that ability right now.     |").center(140))
                    print(str("|_________________________________________________|").center(140))

def sellItem(player):
    showInventory(player)
    print(str(" _____________________________________________________ ").center(140))
    print(str("|                                                     |").center(140))
    print(str("|     Select an Item from your inventory to sell.     |").center(140))
    print(str("|_____________________________________________________|").center(140))
    choice = input(str(":   ").rjust(60))
    if choice in player.inventory:
        for item in itemDB:
            if item.name == choice:
                print(str(" _______________________________________________________________________ ").center(140))
                print(str("|                                                                       |").center(140))
                print(str("|     Would you like to sell a " + str(item.name).center(20) + " for " + str(item.price / 2).center(5) + " gold?     |").center(140))
                print(str("|                ______________            ______________               |").center(140))
                print(str("|               | 1 |   Sell   |          | 2 |   Back   |              |").center(140))
                print(str("|                ``````````````            ``````````````               |").center(140))
                print(str("|_______________________________________________________________________|").center(140))
                final = input(str(":   ").rjust(60))
                if final == "1":
                    deleteItem(player, choice)
                    sold = item.price / 2
                    player.gold = player.gold + sold
    else:
        cantFindItem()

            
def notInStock():
    print(str(" _______________________________________________ ").center(140))
    print(str("|                                               |").center(140))
    print(str("|     That isn't an item that's for sale...     |").center(140))
    print(str("|_______________________________________________|").center(140))

