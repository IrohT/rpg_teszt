from engineja.variables import *



# -------------------------------------------játék----------------------------------------
while True:
    question_time = True
    action_counter = 0

    while question_time:
        if player.hp > 0:
            stat = [f"hp= {player.hp}", f"power= {player.power}", f"defense={player.p_shield.defense}",
                    f"stamina= {player.stamina}",
                    f"hungry= {player.hungry}", f"weapon= {player.p_weapon.name}", f"shield= {player.p_shield.name}"]


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

# *********************************************************stat*********************************************
                    elif question == "stat":
                        help_ad(stat)
# *********************************************************camping***************************************************

                    elif question == "camping":
                        while True:
                            help_ad(camp); question = input("Mit szeretnél csinálni?: ")
                            if question in camp:
                                if question == "eat":
                                    while True:
                                        print(Consumable.food_name); question = input("Mit szeretnél enni?: ")
                                        player.eat(ask_food=question, player_max=max_hp)
                                        action_counter += 1
                                        break

                                elif question == "sleep":
                                    print("Át aludtad a nap hátralévő részét!")
                                    question_time = False

                                if question == "exit":
                                    break

                            else: print(f"Ilyen opció nincs: {question}")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++inventory+++++++++++++++++++++++++++++++++++++++++++++++++++
                    elif question == "inventory":
                        while True:
                            help_ad(inventory_things); question = input("Mit szeretnél csinálni: ")
                            if question in inventory_things:
# -------------------------------------------------------w_equip-------------------------------
                                if question == "weapon_equip":
                                    while True:
                                        print(Weapon.equipment_name); question = input("Mit szeretnél felszerelni?: ")
                                        if question in Weapon.equipment_name:
                                            player.equip(ask_weapon=question)
                                            break
                                        else:
                                            print(f"Nincs iylen eszközöd: {question}")
                                            break
# ------------------------------------------------weapon_deequip-----------------------------

                                elif question == "weapon_deequip":
                                    while True:
                                        print(Player.equip_name); question = input("Mit szeretnél levenni: ")
                                        if question in Player.equip_name:
                                            player.deequip(ask_wep=question)
                                            break
                                        else:
                                            print(f"Nincs ilyen fegyvered: {question}")
                                            break

# -------------------------------------------------fullventory--------------------------------
                                elif question == "fullventory":
                                    print(inventory)
                                    continue
# -------------------------------------------------exit_inventory--------------------------------
                                elif question == "exit":
                                    break
                            else:
                                print(f"Ilyen opció nincs: {question}")

# **************************************************kalandozás************************************************
                    elif question == "adventure":
                        adventure_time = True
                        while adventure_time:
                            help_ad(adventure)
                            question = input("Mit szeretnél csinálni?: ")
                            if question in adventure:
                                if question == "exit":
                                    break
#TODO: megcsinálni rendesen: **********************************looting****************************************
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
            break

    day += 1
    if player.hungry + 5 < 100:
        player.hungry += 5
    if player.hungry == 100:
        player.hp -= 15