from engineja.classes import *
import random



# -------------------------materials------------------
# TODO: Anyagok kraftoláshoz

#alapok
"""
vas(common item craft)
copper(consumables)
arany(-||-,and common item craft)
gyémánt
kő
fa
rubint
emerald 
saphire
Adulár
Aktinolit
"""

# -------------------------poti craft material------------------
"""
gyógynövények (all kind)
"""
# ------------------------- speciale item craft material------------------
"""
adamantium
Aether(magic material)
ancient tablet (enchant)
platinum
meteorit chunks
cobalt

"""
# -------------------------receipts------------------
# TODO: Receptek anyagokból, kajátból

# -------------------------consum------------------

# -------------------------fruis and vegetable------------------
apple = Consumable(food_got=10, f_type="fruit", name="alma", hp_get=0, price=5)
banana = Consumable(food_got=10, f_type="fruit", name="banán", hp_get=0, price=5)
peach = Consumable(food_got=10, f_type="fruit", name="barack", hp_get=0, price=5)
pommengranade = Consumable(food_got=25, f_type="fruit", name="gránátalma", hp_get=10, price=30)
# -------------------------------flesh-------------------------
bat = Consumable(food_get=25, f_type="flesh", name="denevér", hp_get=0, price=0)
batwing = Consumable(food_get=35, f_type="flesh", name="denevér szárny", hp_get=0, price=50)
cooked_batwing = Consumable(food_get=45, f_type="flesh", name="sült denevér szárny", hp_get=0, price=60)
raw_beef = Consumable(food_got=40, f_type="flesh", name="nyers sertésszelet", hp_get=0, price=50)
cooked_beef = Consumable(food_got=60, f_type="flesh", name="steak", hp_get=0, price=60)
raw_chicken = Consumable(food_got=40, f_type="flesh", name="nyers csirke", hp_get=0, price=50)
cooked_chicken = Consumable(food_got=60, f_type="flesh", name="sült csirke", hp_get=0, price=60)
raw_pork = Consumable(food_got=40, f_type="flesh", name="nyers sertéshús", hp_get=0, price=50)
cooked_pork = Consumable(food_got=60, f_type="flesh", name="sült sertéshús", hp_get=0, price=60)




# ---------------------------------------weapons---------------------
# TODO: Még ez alá jön a többi fegyver
# Alap fegyverek(common)

# ----------------------------------------shield--------------------------------------------------
lower_arm = Weapon(damage=0, name="for_arm", durability=9999999999999, stamina_gain=25, w_type='shield', rarity="fist", defense=5)
shield = Weapon(damage=0, name="shield", durability=40, stamina_gain=25, w_type='shield', rarity="common", defense=34)
handcrossbow_oh = Weapon(damage=25, name="handcrossbow", durability=70, stamina_gain=10, w_type='shield', rarity="rare")

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
club = Weapon(damage=5, name="club", durability=15, stamina_gain=15, w_type="one_handed", rarity="common")

# ---------------------------------Icipicit keményebb ucccok(uncommon)---------------------------------
chained_mace = Weapon(damage=33, name="mace", durability=50, stamina_gain=30, w_type='one_handed_mace', rarity="uncommon")
battle_axe = Weapon(damage=40, name="battle_axe", durability=30, stamina_gain=35, w_type='one_handed_axe', rarity="uncommon")
pike = Weapon(damage=20, name="mace", durability=50, stamina_gain=60, w_type='two_handed_spear,mid_range', rarity="uncommon")
naginata_spear = Weapon(damage=33, name="naginata_spear", durability=38, stamina_gain=30, w_type='one/two_handed_spear', rarity="uncommon")
halberd = Weapon(damage=30, name="halberd", durability=30, stamina_gain=50, w_type='two_handed_axe', rarity="uncommon")
kodacsi = Weapon(damage=25, name="japanase_shortsword", durability=50, stamina_gain=24, w_type='one_handed_sword', rarity="uncommon")
katana = Weapon(damage=30, name="katana", durability=55, stamina_gain=21, w_type='one/two_handed_sword', rarity="uncommon")
warhammer = Weapon(damage=70, name="warhammer", durability=65, stamina_gain=50, w_type='two_handed_hammer ', rarity="uncommon")
rifle = Weapon(damage=50, name="rifle", durability=40, stamina_gain=100, w_type="two_handed", rarity="uncommon")



# ---------------------------------Ellenség orrszőrpiszkáló cuccok(rare)---------------------------------
zweihander= Weapon(damage=70, name="zweihander", durability=50, stamina_gain=60, w_type="two_handed_longsword", rarity="rare")
longsword = Weapon(damage=65, name="hosszúkard ", durability=45, stamina_gain=50, w_type='two_handed_longsword', rarity="rare")
handcrossbow = Weapon(damage=25, name="handcrossbow", durability=70, stamina_gain=10, w_type='one_handed_bow', rarity="rare")
bloodlust = Weapon(damage=20, name="bloodlust", durability=100, stamina_gain=30, w_type="one_handed", rarity="rare")#chancetobleed/dualwield
elementalcrossbow = Weapon(damage=100, name="ggsword", durability=150, stamina_gain=200, w_type="two_handed_longsword", rarity="rare")
#---------------------------------Chance to doubleshot------------------------------------------------------
revolver = Weapon(damage=40, name="revolver", durability=50, stamina_gain=20, w_type="one_handed", rarity="rare")#dualwield


# ---------------------------------Ezekkel már lehet belezni(epic)---------------------------------
zanbato = Weapon(damage=80, name="zanbato", durability=70, stamina_gain=55, w_type="two_handed_longsword", rarity="epic")
titanslayer =  Weapon(damage=85, name="titanslayer", durability=55, stamina_gain=55, w_type="two_handed_longsword", rarity="epic")
bowofronin= Weapon(damage=100, name="bowofronin", durability=70, stamina_gain=140, w_type="two_handed_longsword", rarity="epic")
darkmoondagger = Weapon(damage=25, name="darkmoondagger", durability=200, stamina_gain=5, w_type="one_handed", rarity="epic")#dualwield/faithdmg

# ---------------------------------Ez már valami(legendary)---------------------------------
big_fucking_sword = Weapon(damage=300, name="bfsword", durability=150, stamina_gain=101, w_type="BIG_two_handed_sword", rarity="legendary")
sunblade = Weapon(damage=250, name="sunblade", durability=200, stamina_gain=40, w_type="one_handed_sword", rarity="legendary")

# ---------------------------------Hallod ilyened ugyse lesz(mythic)----------------------
dragonborn_battleaxe = Weapon(damage=123, name="dragonborn_battleaxe", durability=400, stamina_gain=95, w_type="one_handed_axe", rarity="mythic")
ggsword =  Weapon(damage=350, name="ggsword", durability=200, stamina_gain=140, w_type="two_handed_longsword", rarity="mythic")
unveilerscrossbow = Weapon(damage=200, name="unveilerscrossbow", durability=400, stamina_gain=100, w_type="two_handed", rarity="mythic")
#----------------------------------Can be duel wielded ------------------------------------
devils_scythe = Weapon(damage=70, name="devils_scythe", durability=450, stamina_gain=60, w_type="one-handed-scythe", rarity="mythic")
#------------------------------------------------------------------------------------------

# the_curator
# the_sword_of_dex

# -----------------------------------------------secret_weapon-------------------------
#blades_of_chaos
# fehymasters_sword
# warhammer_of_kolos
# titancannon
# Finger (level uppal tovább fejlődik = Finger², Finger³, Finger⁴, Fist of Doom(belenyúl a belébe az ánuszán keresztül))

# -----------------------------------------------player_cuccai-------------------------
max_hp = 100
player_hungry = 0
player_stamina = 100
player = Player(hp=max_hp, power=fist.damage, stamina=player_stamina, hungry=player_hungry, food_db=Consumable.food_count, p_weapon=fist, defense=lower_arm.defense, p_shield=lower_arm)




# ----------------------monsters--------------------------------
#---------------Goblinok-------------------
goblin = Monster(name='Goblin', hp=50, power=20, type='basic', gold=2)
goblin_tank = Monster(name='Troll', hp=100, power=2, type='tank', weapon='Pajzs', gold=3)
goblin_warrior = Monster(name='Ork', hp=70, power=30, type='warrior', weapon='Kard', gold=3)
goblin_archer = Monster(name='Goblin íjász', hp=20, power=45, type='archer', weapon='Íj', gold=3 )
goblin_assasin = Monster(name='Gnóm', hp=40, power=50, type='assasin', weapon='Tőr', gold=7)
goblin_elite = Monster(name='Goblin sámán', hp=120, power=50, type='mini_boss', weapon='Zanbato', gold=13)
goblin_boss = Monster(name='Goblin király', hp=300, power=75, type='boss', weapon='Varázsbot', gold=50)

#---------------Secret boss------------------
titan = Monster(name='Immortal Titan', hp=100000, power=5000, type='secret_boss', waepon='2xZweihander', loot='Titán agya', gold=50000)
tomi = Monster(name='Laughing Demon', hp=1000, power=500, type='secret_boss', weapon='Halálos nevetés', loot='Röhögj amíg bírsz varázslat')
feri = Monster(name='Fehy, the imaginative', hp=2000, power=700, type='secret_boss', weapon="Fahy's Mastersword", loot="Fahy's Mastersword")


#---------------Csontvázak-------------------
skeleton = Monster(name='Csontváz', hp=60, power=30, type='basic', gold=2)
skeleton_tank = Monster(name='Csontváz fal', hp=130, power=1, type='tank', gold=3)
skeleton_warrior = Monster(name='Csontváz harcos', hp=80, power=40, type='warrior', gold=3)
skeleton_archer = Monster(name='Csontváz íjász', hp=40, power=65, type='archer', gold=3)
skeleton_assasin = Monster(name='Csontváz orgyilkos', hp=60, power=70, type='assasin', gold=7)
skeleton_elite = Monster(name='Csontóriás', hp=140, power=75, type='mini_boss', gold=13)
skeleton_boss = Monster(name='Nekromanciás', hp=400, power=100, type='boss', gold=50)

#--------------Zombik----------------------
zombie = Monster(name='Zombi', hp=60, power=30, type='basic', gold=2)
zombie_tank = Monster(name='Zombi védelmező', hp=130, power=1, type='tank', gold=3)
zombie_warrior = Monster(name='Zombi harcos', hp=80, power=40, type='warrior', gold=3)
zombie_archer = Monster(name='Zombi íjász', hp=40, power=65, type='archer', gold=3)
zombie_assasin = Monster(name='Zombi orgyilkos', hp=60, power=70, type='assasin', gold=7)
zombie_elite = Monster(name='Zombi óriás', hp=140, power=75, type='mini_boss', gold=13)
zombie_boss = Monster(name='Zombi Király', hp=400, power=100, type='boss', gold=50)

#--------------Démonok----------------------
demon = Monster(name='Imp', hp=120 , power=40, type='basic', gold=4)
demon_tank = Monster(name='Démoni tremor', hp=250, power=4,  type='tank', gold=6)
demon_warrior = Monster(name='Pokolkutya', hp=180 , power=60, type='warrior', gold=6)
demon_archer = Monster(name='Tiefling', hp=60 , power=100, type='archer', gold=6)
demon_assasin = Monster(name='Succubus', hp=100 , power=120, type='assasin', gold=14)
demon_elite = Monster(name='Lucifer', hp=140, power=150, type='mini_boss', gold=26)
demon_boss = Monster(name='Sátán', hp=800, power=300, type='boss', gold=100)

#--------------Angyalok----------------------
angel = Monster(name='Valkűr', hp=120 , power=40, type='basic', gold=4)
angel_tank = Monster(name='Őrangyal', hp=250, power=4,  type='tank', gold=6)
angel_warrior = Monster(name='Arkangyal', hp=180 , power=60, type='warrior', gold=6)
angel_archer = Monster(name='Hera', hp=60 , power=100, type='archer', gold=6)
angel_assasin = Monster(name='Trón', hp=100 , power=120, type='assasin', gold=14)
angel_elite = Monster(name='Kerúb', hp=140, power=150, type='mini_boss', gold=26)
angel_boss = Monster(name='Szeráf', hp=800, power=300, type='boss', gold=100)

#--------------------Egyéb ellenfelek-------------------------
spider = Monster(name='Pók', hp=50, power=20, type='basic', gold=2)
wolf = Monster(name='Farkas', hp=50, power=20, type='basic', gold=2)
bat = Monster(name='Denevér', hp=50, power=20, type='basic', gold=2)
golem = Monster(name='Kőgólem', hp=130, power=30, type='tank', gold=12)
centaur = Monster(name='Kentaúr', hp=170, power=200, type='mini_boss', gold=50)
ent = Monster(name='Szírszakáll', hp=1000, power=120, type='boss', gold=30)

#---------------Secret boss------------------
"""
titan = Monster(name='Immortal Titan', hp=100000, power=5000, m_type='secret_boss', m_weapon='2xZweihander', loot='Titán agya', gold=50000)

tomi = Monster(name='Laughing Demon', hp=1000, power=2000, m_type='secret_boss', m_weapon='Halálos nevetés', loot='Röhögj amíg bírsz varázslat', gold=4000)

peti = Monster(name='', hp=, power=, m_type='secret_boss', m_weapon='True Bankai', loot='', gold=5000)
feri = Monster(name='Fehy, the imaginative', hp=2000, power=700, m_type='secret_boss', m_weapon="Fahy's Mastersword", loot="Fehy's Mastersword", gold=6000)
szabadi = Monster(name='', hp=, power=, m_type='secret_boss', m_weapon='Fist of Doom', loot='', gold=7000)
"""
# ---------------------------------npc------------------------------------
jozsi = Npc(name="Józsi")

# --------------------------------------------kocka--------------------------------

def cuby(num):
    return random.randint(1, num)

# ------------------------------------------help------------------------------------

def help_ad(f_list):
    for word in f_list:
        print(f"|{word}|")

# -------------------------------------------változók--------------------------------

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
