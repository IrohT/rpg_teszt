import random

# ------------------------------------monster----------------------------------


def cuby(num):
    return random.randint(1, num)

def help_ad(f_list):
    for word in f_list:
        print(f"|{word}|")



class Monster:
    standard = []
    tank = []
    warrior = []
    archer = []
    assassin = []
    mini_boss = []
    boss = []

    easy = [standard, archer]
    medium = [warrior, tank]
    hard = [assassin]
    very_hard = [mini_boss, boss]

    def __init__(self, name, hp, power, m_type, m_weapon, loot=None, gold=None):
        self.name = name
        self.loot = loot
        self.hp = hp
        self.m_weapon = m_weapon
        self.gold = gold
        self.m_type = m_type
        self.power = power + self.m_weapon.damage

        if self.m_type == "standard":
            Monster.standard.append(self)
        elif self.m_type == "tank":
            Monster.tank.append(self)
        elif self.m_type == "warrior":
            Monster.warrior.append(self)
        elif self.m_type == "archer":
            Monster.archer.append(self)
        elif self.m_type == "assassin":
            Monster.assassin.append(self)
        elif self.m_type == "mini_boss":
            Monster.mini_boss.append(self)
        elif self.m_type == "boss":
            Monster.boss.append(self)

    def hit(self, player_things):
        defend_hit = self.power - player_things.defense
        player_things.hp -= defend_hit
        print(f"A szörny ({self.name}) rádsebzett: {defend_hit}")

# ----------------------------------weapon-----------------------------------


class Weapon:
    shield = []
    shield_name = []
    name_weapon = []
    weapons = []
    fist = []
    common = []
    uncommon = []
    rare = []
    epic = []
    legendary = []
    mythic = []

    def __init__(self, name, durability, stamina_gain, w_type, rarity, defense=0, enchant=None, damage=0):
        self.damage = damage
        self.enchant = enchant
        self.name = name
        self.durability = durability
        self.stamina_gain = stamina_gain
        self.w_type = w_type
        self.rarity = rarity
        self.defense = defense

        if self.rarity == "common":
            Weapon.common.append(self)
        elif self.rarity == "fist":
            Weapon.fist.append(self)
        elif self.rarity == "uncommon":
            Weapon.uncommon.append(self)
        elif self.rarity == "rare":
            Weapon.rare.append(self)
        elif self.rarity == "epic":
            Weapon.epic.append(self)
        elif self.rarity == "legendary":
            Weapon.epic.append(self)
        elif self.rarity == "mythic":
            Weapon.mythic.append(self)

        if self.durability <= 0:
            Weapon.weapons.remove(self.name)
            print(f"eltört a fegyvered: {self.name}")

    def find_weapon(self):
        if self.w_type == "shield":
            Weapon.shield.append(self)
            Weapon.shield_name.append(self.name)
            if self.name in Weapon.shield_name:
                print(f"megtaláltál egy pajzsot: {self.name}")
            else:
                print(f"megtaláltál egy új pajzsot: {self.name}")

        else:
            Weapon.weapons.append(self)
            Weapon.name_weapon.append(self.name)
            if self.name in Weapon.name_weapon:
                print(f"megtaláltál egy fegyvert: {self.name}")
            else:
                print(f"megtaláltál egy új fegyvert: {self.name}")

    @staticmethod
    def weapon_dropper(monster):
        if monster.m_type == "standard" or "archer":
            len_list = len(Weapon.common)
            rand_weapon = Weapon.common[random.randint(0, len_list-1)]
            rand_weapon.find_weapon()
        elif monster.m_type == "warrior" or "tank":
            len_list = len(Weapon.uncommon)
            rand_weapon = Weapon.uncommon[random.randint(0, len_list-1)]
            rand_weapon.find_weapon()
        elif monster.m_type == "assassin":
            len_list = len(Weapon.rare)
            rand_weapon = Weapon.rare[random.randint(0, len_list-1)]
            rand_weapon.find_weapon()
        elif monster.m_type == "mini_boss":
            len_list = len(Weapon.epic)
            rand_weapon = Weapon.epic[random.randint(0, len_list-1)]
            rand_weapon.find_weapon()
        elif monster.m_type == "boss":
            len_list = len(Weapon.legendary)
            rand_weapon = Weapon.legendary[random.randint(0, len_list-1)]
            rand_weapon.find_weapon()

#TODO: potion -----------------------------------------------Food-------------------------------


class Consumable:
    food_name = []
    foods = []

    fruits = []
    flesh = []
    vegetables = []

    def __init__(self, food_got, name, f_type, price, hp_get=0, enchant=None):
        self.name = name
        self.hp_get = hp_get
        self.food_got = food_got
        self.f_type = f_type
        self.enchant = enchant
        self.price = price

        if self.f_type == "fruit":
            Consumable.fruits.append(self)
        elif self.f_type == "vegetable":
            Consumable.vegetables.append(self)
        elif self.f_type == "flesh":
            Consumable.flesh.append(self)

    def get_consume(self):
        Consumable.foods.append(self)
        Consumable.food_name.append(self.name)
        print(f"találtál kaját: {self.name}")


    @staticmethod
    def food_dropper(place):
        if place == "forest":

            len_list = len(Consumable.vegetables)
            forest_f_type = Consumable.vegetables[random.randint(0, len_list-1)]
            forest_f_type.get_consume()

        else:
            food_len = len(Consumable.flesh)
            food = Consumable.flesh[random.randint(0, food_len - 1)]
            food.get_consume()

# ------------------------------------------------------player------------------------------------------


class Player:
    equipped = []
    name_equip = []

    def __init__(self, hp, stamina, power, hungry, p_weapon, p_shield, defense, current_enemy=None, money=0):
        self.hp = hp
        self.stamina = stamina
        self.power = power
        self.hungry = hungry
        self.p_weapon = p_weapon
        self.money = money
        self.current_enemy = current_enemy
        self.defense = defense
        self.p_shield = p_shield

    def eat(self,ask_food, player_max):
        for food in Consumable.foods:
            
            if food.name == ask_food:
                
                if self.hp + food.hp_get > player_max:
                    self.hp = player_max
                else:
                    self.hp += food.hp_get

                if self.hungry - food.food_got < 0:
                    self.hungry -= self.hungry
                else:
                    self.hungry -= food.food_got

                Consumable.foods.remove(food)
                Consumable.food_name.remove(food.name)
                print(f"Megetted a(z) {food.name}")
                
            else:
                print(f"Nincs ilyen kajád: {ask_food}")

    def rand_enemy(self, difficulty):
        diff_len = len(difficulty)
        rand_dif = difficulty[random.randint(0, diff_len-1)]
        rand_len = len(rand_dif)
        rand_monster = rand_dif[random.randint(0, rand_len-1)]
        self.current_enemy = rand_monster

    def kill(self, name):
        print(f"Megölted a szörnyet: {name}")
        self.current_enemy = None

    def p_hit(self):
        if self.current_enemy.hp - self.p_weapon.damage > 0:
            if self.stamina > 0:
                self.stamina -= self.p_weapon.stamina_gain
                self.current_enemy.hp -= self.p_weapon.damage
                self.p_weapon.durability -= 1
                print(f'Rásebeztél a szörnyre: {self.current_enemy.name}\n Sebezés: {self.power}')
            else:
                print("Elfogyott a staminád!")
        else:
            Weapon.weapon_dropper(self.current_enemy)
            self.current_enemy.hp -= self.current_enemy.hp
            self.stamina -= self.p_weapon.stamina_gain
            self.p_weapon.durability -= 1

    def deflect(self, chance):
        if chance == 1:
            if self.current_enemy.hp - self.current_enemy.power > 0:
                self.current_enemy.hp -= self.current_enemy.power
                print(f"Sikeresen vissza ütütted a támadást, sebződött: {self.current_enemy.power}")
            else:
                print(f"Sikeresen vissza ütütted a támadást, sebződött: {self.current_enemy.power}")
                Weapon.weapon_dropper(self.current_enemy)
                self.current_enemy.hp -= self.current_enemy.hp

        else:
            self.hp -= self.current_enemy.power
            print(f"Nem sikerült vissza ütni a támadást")
            print(f"A szörny ({self.current_enemy.name}) rádsebzett: {self.current_enemy.power}")

    def fight(self, counter, wube, help_ja, cmd):
        player_harcol = True
        print('Megtámadtak, készülj a harcra!')
        self.rand_enemy(Monster.easy)
        m_stat = [f"{self.current_enemy.name} hp={self.current_enemy.hp}",
                  f"{self.current_enemy.name} power={self.current_enemy.power}",
                  f"{self.current_enemy.name} type={self.current_enemy.m_type}",
                  f"{self.current_enemy.name} weapon={self.current_enemy.m_weapon.name}"]
        while player_harcol:
            help_ja(cmd)
            question = input('Mit teszel?: ')
            if question in cmd:
                if question == 'fight':
                    self.p_hit()
                    if self.current_enemy.hp > 0:
                        self.current_enemy.hit(player_things=self)
                    if self.hp > 0:
                        if self.current_enemy.hp <= 0:
                            self.kill(name=self.current_enemy.name)
                            player_harcol = False
                    else:
                        player_harcol = False

                elif question == 'deflect':
                    deflect_cube = wube(2)
                    self.deflect(chance=deflect_cube)
                    if self.hp > 0:
                        if self.current_enemy.hp <= 0:
                            self.kill(name=self.current_enemy.name)
                            player_harcol = False
                    else:
                        player_harcol = False

                elif question == "flee":
                    flee_cube = wube(4)
                    if flee_cube == 2 or flee_cube == 4:
                        print(f"Sikerült elmenekülnöd egy karcolás nélkül!")
                        player_harcol = False

                    else:
                        print(f"Menekülés közben megsebeztek")
                        self.hp -= self.current_enemy.power
                        counter += 1
                        player_harcol = False

                elif question == "m_stat":
                    help_ja(f_list=m_stat)
                    continue

            else:
                print(f"Nincs ilyen opció: {question}")

    def equip(self,ask_weapon, new_weapon, wep_name_list, wep_list):
          for wep in Weapon.weapons:
                if wep.name == ask_weapon:
                    if wep.w_type == "shield":
                        Weapon.shield.remove(wep); Weapon.shield_name.remove(wep.name)
                        self.defense -= self.defense
                        self.p_shield = wep
                        self.defense += wep.defense
                    else:
                        wep_list.remove(new_weapon); wep_name_list.remove(new_weapon.name)
                        self.defense -= self.defense; self.power -= self.power
                        self.p_weapon = new_weapon
                        self.power += new_weapon.damage
                        self.defense += new_weapon.defense

                    print(f"felszerelted: {new_weapon.name}")

    def deequip(self, wep_name_list, wep_list, new_weapon, shield_list, shield_list_name):
        if new_weapon.w_type == "shield":
            shield_list.append(new_weapon)
            shield_list_name.append(new_weapon.name)
            self.defense = Weapon.fist[0].defense
            self.p_shield = Weapon.fist[0]

        else:
            wep_list.append(new_weapon)
            wep_name_list.append(new_weapon.name)
            self.power = Weapon.fist[1].damage
            self.p_weapon = Weapon.fist[1]

        print(f"leszerelted: {new_weapon.name}")

# ---------------------------------------npc---------------------------------------


class Npc:
    selling_things = {
        "sword": 100
    }

    def __init__(self, name):
        self.name = name

    def speak(self, say_thing):
        print(f"{self.name}: {say_thing}")

    def selling(self, somebody_money):
        for key, value in Npc.selling_things.items():
            if somebody_money >= value:
                print(f"{self.name} eldata neked: {key}")
            else:
                print("Nincs elég pénzed te ganéj")