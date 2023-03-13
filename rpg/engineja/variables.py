import random
from engineja.classes import *


# -------------------------consum------------------
apple = Consumable(food_got=10, f_type="fruit", name="alma", hp_get=0, price=5)
banana = Consumable(food_got=30, f_type="fruit", name="banana", hp_get=0, price=10)
pommengranade = Consumable(food_got=30, f_type="vegetable", name="granade", hp_get=10, price=25)
# -------------------------------flesh-------------------------
meat = Consumable(food_got=60, f_type="flesh", name="matata", hp_get=0, price=60)


# ---------------------------------------weapons---------------------
# TODO: Még ez alá jön a többi fegyver
# Alap fegyverek(common)

# ----------------------------------------shield--------------------------------------------------
lower_arm = Weapon(damage=0, name="for_arm", durability=9999999999999, stamina_gain=25, w_type='shield', rarity="fist", defense=5)
shield = Weapon(damage=0, name="shield", durability=40, stamina_gain=25, w_type='shield', rarity="common", defense=34)
# ---------------------------------------weapons---------------------
sword = Weapon(damage=34, name="sword", durability=40, stamina_gain=25, w_type='one_handed', rarity="common")
fist = Weapon(damage=9, name="fist", durability=9999999999999, stamina_gain=6, w_type='beater', rarity="fist")
two_handed_sword = Weapon(damage=60, name="longsword", durability=80, stamina_gain=38, w_type='two_handed_sword', rarity="common")
dagger = Weapon(damage=15, name="dagger", durability=32, stamina_gain=10, w_type='one_handed', rarity="common")
bow = Weapon(damage=10, name="bow", durability=20, stamina_gain=14, w_type='low_range, one_handed', rarity="common")
spear = Weapon(damage=24, name="spear", durability=30, stamina_gain=40, w_type='one_handed/two_handed,low_range,spear ', rarity="common")
berserker_axe = Weapon(damage=20, name="berserker_axe", durability=50, stamina_gain=30, w_type='one_handed', rarity="common")
two_handed_axe = Weapon(damage=65, name="two handed_axe", durability=90, stamina_gain=60, w_type='two_handed', rarity="common")
crossbow = Weapon(damage=19, name="crossbow", durability=30, stamina_gain=9, w_type='long_range,two_handed', rarity="common")
knife = Weapon(damage=12, name="knife", durability=14, stamina_gain=10, w_type='one_handed_dagger', rarity="common")
falchion= Weapon(damage=37, name="falchion", durability=60, stamina_gain=35, w_type='one_handed_sword', rarity="common")
mace = Weapon(damage=30, name="mace", durability=35, stamina_gain=29, w_type='one_handed_mace', rarity="common")
hatchet = Weapon(damage=23, name="hatchet", durability=35, stamina_gain=15, w_type='one_handed_sword', rarity="common")
shortsword = Weapon(damage=18, name="shortsword", durability=20, stamina_gain=19, w_type='one_handed_sword', rarity="common")




# Icipicit keményebb ucccok(uncommon)
chained_mace = Weapon(damage=33, name="mace", durability=50, stamina_gain=30, w_type='one_handed_mace', rarity="uncommon")
battle_axe = Weapon(damage=40, name="battle_axe", durability=30, stamina_gain=35, w_type='one_handed_axe', rarity="uncommon")
pike = Weapon(damage=20, name="mace", durability=50, stamina_gain=60, w_type='two_handed_spear,mid_range', rarity="uncommon")
naginata_spear = Weapon(damage=33, name="naginata_spear", durability=38, stamina_gain=30, w_type='one/two_handed_spear', rarity="uncommon")
halberd = Weapon(damage=30, name="halberd", durability=30, stamina_gain=50, w_type='two_handed_axe', rarity="uncommon")
kodacsi = Weapon(damage=25, name="japanase_shortsword", durability=50, stamina_gain=24, w_type='one_handed_sword', rarity="uncommon")
katana = Weapon(damage=30, name="katana", durability=55, stamina_gain=21, w_type='one/two_handed_sword', rarity="uncommon")



# Ellenség orrszőrpiszkáló cuccok(rare)
zweihander= Weapon(damage=70, name="zweihander", durability=50, stamina_gain=60, w_type="two_handed_longsword", rarity="rare")
# Ezekkel már lehet belezni(epic)
zanbato = Weapon(damage=80, name="zanbato", durability=70, stamina_gain=55, w_type="two_handed_longsword", rarity="epic")
# Ez már valami(legendary)
big_fucking_sword = Weapon(damage=300, name="bfsword", durability=150, stamina_gain=101, w_type="BIG_two_handed_sword", rarity="legendary")

# Hallod ilyened ugyse lesz(mythic)
dragonborn_battleaxe = Weapon(damage=123, name="dragonborn_battleaxe", durability=400, stamina_gain=95, w_type="one_handed_axe", rarity="mythic")
# the_curator
# the_sword_of_dex
#
# #secret weapon
# sword of dalmasters
# fehymasters_sword
# warhammer_of_kolos
# titancannon


# -----------------------------------------------player_cuccai-------------------------
max_hp = 100
player_hungry = 0
player_stamina = 100
player = Player(hp=max_hp, power=fist.damage, stamina=player_stamina, hungry=player_hungry, p_weapon=fist, defense=lower_arm.defense, p_shield=lower_arm)





# ----------------------monsters--------------------------------


# -----------------goblins--------------------------------------
goblin_standard = Monster(name='Goblin', hp=50, power=20, m_type='standard', m_weapon=fist, gold=2)
goblin_tank = Monster(name='Goblin_tank', hp=100, power=2, m_type='tank', m_weapon=spear, gold=11)
goblin_warrior = Monster(name='Goblin_warrior', hp=70, power=30, m_type='warrior', m_weapon=sword, gold=7)
goblin_archer = Monster(name='Goblin_archer', hp=20, power=45, m_type='archer', m_weapon=bow, gold=5)
goblin_assassin = Monster(name='Goblin_assassin', hp=40, power=50, m_type='assassin', m_weapon=dagger, gold=10)
goblin_captain = Monster(name='Goblin_captain', hp=120, power=50, m_type='mini_boss', m_weapon=two_handed_sword, gold=27)
goblin_boss = Monster(name='Goblin_king', hp=300, power=75, m_type='boss', m_weapon=two_handed_axe, gold=50)


#---------------Secret boss------------------
# titan = Monster(name='Immortal Titan', hp=100000, power=5000, m_type='secret_boss', m_weapon='2xZweihander', loot='Titán agya', gold=50000)
# tomi = Monster(name='Laughing Demon', hp=1000, power=500, m_type='secret_boss', m_weapon='Halálos nevetés', loot='Röhögj amíg bírsz varázslat')
# peti
# feri = Monster(name='Fehy, the imaginative', hp=2000, power=700, m_type='secret_boss', m_weapon="Fahy's Mastersword", loot="Fehy's Mastersword")



# ---------------------------------npc------------------------------------
jozsi = Npc(name="Józsi")

# --------------------------------------------kocka--------------------------------



# ------------------------------------------help------------------------------------


# -------------------------------------------változók--------------------------------


stat = [f"hp= {player.hp}", f"power= {player.power}", f"defense={player.p_shield.defense}", f"stamina= {player.stamina}",
                    f"hungry= {player.hungry}", f"weapon= {player.p_weapon.name}", f"shield= {player.p_shield.name}"]

day = 1
cube = cuby(10)
actions = ["adventure", "camping", "inventory", "stat", "exit"]
inventory = [Weapon.name_weapon, Weapon.shield_name, Consumable.food_name]
inventory_things = ["weapon_equip", "weapon_deequip", "fullventory", "exit"]
camp = ["eat", "sleep", "exit"]
adventure = ["looting", "hunting", "exit"]
combat = ["m_stat", "fight", "deflect", "flee" ]
game = True
napszak = ["Reggel", "Dél-Délután", "Este"]
weapon_counter = 0
shield_counter = 0
