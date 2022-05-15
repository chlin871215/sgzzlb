import random
from turtle import speed, title, update

title = "fightgame0501"

author = "barry"


class Create_Role:  # 角色元素

    def __init__(self, name, hp, damage, speed, team):
        self.name = name
        self.hp = hp  # 10~20
        self.damage = damage  # 3~5
        self.speed = speed  # 10~99
        self.team = team  # AorB


# 創角加入Role array
dad = Create_Role("dad", random.randint(10, 20), random.randint(
    3, 5), random.randint(10, 99), "A")
bro = Create_Role("bro", random.randint(10, 20), random.randint(
    3, 5), random.randint(10, 99), "A")
doo = Create_Role("doo", random.randint(10, 20), random.randint(
    3, 5), random.randint(10, 99), "A")
mom = Create_Role("mom", random.randint(10, 20), random.randint(
    3, 5), random.randint(10, 99), "B")
moo = Create_Role("moo", random.randint(10, 20), random.randint(
    3, 5), random.randint(10, 99), "B")
sis = Create_Role("sis", random.randint(10, 20), random.randint(
    3, 5), random.randint(10, 99), "B")

# 分隊加入陣列
Role = [dad, mom, bro, doo, sis, moo]
teamA = []
teamB = []
teams = [teamA, teamB]

for i in range(len(Role)):
    if Role[i].team == 'A':
        teamA.append(Role[i])
    else:
        teamB.append(Role[i])

# for i in range(len(teamA)):
#    print('content of', teamA[i].__dict__)
#    print('content of', teamB[i].__dict__)

# 根據速度排序
Role.sort(key=lambda s: s.speed, reverse=True)

# for i in range(len(Role)):
#    print(Role[i].__dict__)

# 造成傷害敘述


def damage(attacker, attacked):
    print(attacker.name, "對", attacked.name, "攻擊造成",
          attacker.damage, "傷害(",  attacked.hp, ")")

# 死亡判定，每次造成傷害後都要確定血量並不低於0


def killsecure(attacked):
    if attacked.hp <= 0:
        attacked.hp = 0

# 輸贏判定


def Win_Lose(team):
    deaths = 0
    for i in range(len(team)):
        for j in range(len(team[i])):
            if team[i][j].hp == 0:
                deaths += 1
        if deaths == 1:
            print("team", team[i][0].team, "輸了")
            return True


# 戰鬥細節處理


def attack(attacker, attacked):
    if attacked.hp > 0 and attacker.hp > 0:  # 都活著才行
        fireball(attacker, attacked)
        if attacked.hp > 0:
            attacked.hp = attacked.hp - attacker.damage
            killsecure(attacked)
            if attacked.hp <= 0:
                damage(attacker, attacked)
                print(attacked.name, "is dead")
            else:
                damage(attacker, attacked)

# 技能範例


def fireball(attacker, attacked):
    fireballdamage = 3
    if random.randint(1, 10) <= 5:  # 技能施放機率
        attacked.hp = attacked.hp - fireballdamage
        killsecure(attacked)
        print(attacker.name, "對", attacked.name,
              "施放阿發的拳頭造成", fireballdamage, "傷害(", attacked.hp, ")")


# 展示角色資訊
def show(name):
    print(name.name, "的血量(", name.hp, ")", name.name,
          "的傷害(", name.damage, ")", name.name, "的速度(", name.speed, ")")


for teams_number in range(len(teams)):
    print("team", teams[teams_number][0].team)
    for teammembers in range(len(teamA)):
        show(teams[teams_number][teammembers])

# 選取攻擊對象(未完)


def choose_target():
    target = random.randint(1, 99) % 3
    pass


# 戰鬥回合
for i in range(8):
    print("第", i+1, "回合")
    for fight_order in range(1):  # 目前是每回合可以打1次來回，(未完)

        if dad.speed >= mom.speed:
            attack(dad, mom)
            attack(mom, dad)
        else:
            attack(mom, dad)
            attack(dad, mom)
    if Win_Lose(teams):
        break
    if i == 7 and not Win_Lose(teams):
        print("平手")
        break
