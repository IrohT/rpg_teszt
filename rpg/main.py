from engineja.variables import *



# -------------------------------------------játék----------------------------------------
while game:
    question_time = True
    action_counter = 0


# ------------------------------------------------------élő-------------------------------

# ----------------------------------kérdés------------------------------------------------

    while question_time:
        if player.hp > 0:


            if action_counter < 3:
                if action_counter == 0:
                    print(f"\n {day}.Nap: {napszak[0]}")
                elif action_counter == 1:
                    print(f"\n {day}.Nap: {napszak[1]}")
                else:
                    print(f"\n {day}.Nap: {napszak[2]}")

                help_ad(actions)
                question = input("mit szeretnél csinálni?: ").lower()

                if question in actions:
                    if question == "exit":
                        question_time = False
                        game = False


# -----------------------------------------------------camping---------------------------

                    elif question == "camping":
                        while True:
                            help_ad(camp); question = input("Mit szeretnél csinálni?: ")
                            if question in camp:
                                if question == "exit":
                                    break
# -----------------------------------------------eat-------------------------------------
                                elif question == "eat":
                                    while True:
                                        print(Consumable.food_name); question = input("Mit szeretnél enni?: ")
                                        player.eat(ask_food=question, player_max=max_hp)
                                        action_counter += 1
                                        break


# TODO: valamennyi eséllyel elkerülni valahova álmodba: -------------------------------------------------sleep---------------------------------------
                                elif question == "sleep":
                                    print("Át aludtad a nap hátralévő részét!")
                                    question_time = False
                                    break
                           
                           else: print(f"Ilyen opció nincs: {question}")
# --------------------------------------------------inventory-----------------------------------

                    elif question == "inventory":
                        while True:
                            help_ad(inventory_things); question = input("Mit szeretnél csinálni: ")
                            if question in inventory_things:
# -------------------------------------------------------w_equip-------------------------------
                                if question == "weapon_equip":
                                    while True:
                                        print(Weapon.name_weapon, Weapon.shield_name); question = input("Mit szeretnél felszerelni?: ")
                                        if question in Weapon.name_weapon and if weapon_counter < 1::
                                            for wep in Weapon.weapons:
                                                if wep.name == question:
                                                    player.equip(new_weapon=wep, wep_name_list=Weapon.name_weapon, wep_list=Weapon.weapons)
                                                    weapon_counter += 1
                                                    break

                                            else:
                                                print("Egyszerre csak egy fegyver lehet nálad!")
                                                break

                                        elif question in Weapon.shield_name:
                                            if shield_counter < 1:
                                                if question in Weapon.shield_name:
                                                    for wep in Weapon.shield:
                                                        if wep.name == question:
                                                            player.equip(new_weapon=wep, wep_name_list=Weapon.shield_name, wep_list=Weapon.shield)
                                                            shield_counter += 1
                                                            equip_time = False

                                            else:
                                                print("Egyszerre csak egy pajzs lehet nálad!")
                                                equip_time = False

                                        else:
                                            print(f"Nincs iylen eszközöd: {question}")
# ------------------------------------------------weapon_deequip-----------------------------

                                elif question == "weapon_deequip":
                                    deequip_time = True
                                    while deequip_time:
                                        print(Player.name_equip)
                                        question = input("Mit szeretnél levenni: ")
                                        if question in Player.name_equip:
                                            for wep in Player.equipped:
                                                if wep.name == question:
                                                    if wep.w_type == "shield":
                                                        shield_counter -= 1
                                                        player.deequip(wep_name_list=Weapon.name_weapon, wep_list=Weapon.weapons, new_weapon=wep, shield_list=Weapon.shield, shield_list_name=Weapon.shield_name)
                                                        deequip_time = False
                                                    else:
                                                        weapon_counter -= 1
                                                        player.deequip(wep_name_list=Weapon.name_weapon, wep_list=Weapon.weapons, new_weapon=wep, shield_list=Weapon.shield, shield_list_name=Weapon.shield_name)
                                                        deequip_time = False

                                        else:
                                            print(f"Nincs ilyen fegyvered: {question}")
                                            equip_time = False

# -------------------------------------------------fullventory--------------------------------
                                elif question == "fullventory":
                                    print(inventory)
                                    continue

                                elif question == "exit":
                                    break
                            else:
                                print(f"Ilyen opció nincs: {question}")
# -------------------------------------------------------stat----------------------------------
                    elif question == "stat":
                        help_ad(stat)
                        continue
# ----------------------------------------------kalandoztál--------------------------------
                    elif question == "adventure":
                        adventure_time = True
                        while adventure_time:
                            help_ad(adventure)
                            question = input("Mit szeretnél csinálni?: ")
                            if question in adventure:
                                if question == "exit":
                                    break
#TODO: megcsinálni rendesen: ----------------------------------------------------looting---------------------------------
                                if question == "looting":
                                    sword.find_weapon()
                                    shield.find_weapon()
                                    Consumable.food_dropper("forest")
                                    action_counter += 1

                                    nyugis_tamadas_esely = cuby(5)
                                    if nyugis_tamadas_esely == 2:
                                        print('Belebotlottál egy agresszív lénybe, készülj a harcra!')
                                        break

                                    else:
                                        apple.get_consume()
                                        break


# TODO: több helyen vadászni:-------------------------------------------------hunting-------------------------------------
                                elif question == "hunting":
# ------------------------------------------------------hurting---------------------------------
                                    tamadas_esely = cuby(4)
                                    if tamadas_esely == 4 or tamadas_esely == 2:
                                        player.fight(counter=action_counter, wube=cuby, help_ja=help_ad, cmd=combat)
                                        action_counter += 1
                                    else:
                                        print("vadászol")
                                        action_counter += 1
                                        break
                                else:
                                    print(f"Ilyen opció nincs: {question}")

                else:
                    print(f"Ilyen opció nincs: {question}")
                    continue
# ----------------------------------------------------lejárt_akció_idő-----------------------
            else:
                print("Kifáradtál")
                question_time = False
# --------------------------------------------------------halott-----------------------------
        else:
            print("Meghaltál!")
            question_time = False
            game = False

    day += 1
    if player.hungry + 5 < 100:
        player.hungry += 5
    if player.hungry == 100:
        player.hp -= 15