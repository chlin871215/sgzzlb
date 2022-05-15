from turtle import title, update
import random

title = "fightgame"

author = "barry"


class Role:  # 角色元素

    def __init__(self, name, level, hp, damage, speed):
        self.name = name
        self.level = level
        self.hp = hp
        self.damage = damage
        self.speed = speed


dad = Role("dad", 1, random.randint(5, 8),
           random.randint(1, 2), random.randint(1, 3))
mom = Role("mom", 1, random.randint(5, 8),
           random.randint(1, 2), random.randint(1, 3))

role = [dad, mom]


def damage(attacker, attacked):
    print(attacker.name, "對", attacked.name, "攻擊造成",
          attacker.damage, "傷害(", attacked.hp, ")")

# 造成傷害後要加


def killsecure(attacked):
    if attacked.hp <= 0:
        attacked.hp = 0


def attack(attacker, attacked):
    fireball(attacker, attacked)
    if attacked.hp > 0:
        attacked.hp = attacked.hp - attacker.damage
        killsecure(attacked)
        if attacked.hp <= 0:
            attacked.hp = 0
            damage(attacker, attacked)
            print(attacked.name, "is dead")
        else:
            damage(attacker, attacked)


def fireball(attacker, attacked):
    fireballdamage = 3
    if random.randint(1, 10) <= 5:
        attacked.hp = attacked.hp - fireballdamage
        killsecure(attacked)
        print(attacker.name, "對", attacked.name,
              "施放阿發的拳頭造成", fireballdamage, "傷害(", attacked.hp, ")")


def show(name):
    print(name.name, "的血量(", name.hp, ")", name.name, "的傷害(", name.damage, ")")


for j in range(2):
    show(role[j])


for i in range(8):
    print("第", i+1, "回合")
    if dad.speed >= mom.speed:
        attack(dad, mom)
        if mom.hp == 0:
            break
        attack(mom, dad)
        if dad.hp == 0:
            break
    else:
        attack(mom, dad)
        if dad.hp == 0:
            break
        attack(dad, mom)
        if mom.hp == 0:
            break
