from turtle import speed, title, update
import random

title = "fightgame0501"

author = "berlin"


class Create_Role:  # 角色元素

    def __init__(self, name, hp, damage, speed, team):
        self.name = name
        self.hp = hp  # 10~20
        self.damage = damage  # 3~5
        self.speed = speed  # 10~99
        self.team = team  # AorB


# 創角加入Role array
AA = Create_Role("AA", random.randint(10, 20), random.randint(
    3, 5), random.randint(10, 99), "A")
BB = Create_Role("BB", random.randint(10, 20), random.randint(
    3, 5), random.randint(10, 99), "A")
CC = Create_Role("CC", random.randint(10, 20), random.randint(
    3, 5), random.randint(10, 99), "A")
DD = Create_Role("DD", random.randint(10, 20), random.randint(
    3, 5), random.randint(10, 99), "B")
EE = Create_Role("EE", random.randint(10, 20), random.randint(
    3, 5), random.randint(10, 99), "B")
FF = Create_Role("FF", random.randint(10, 20), random.randint(
    3, 5), random.randint(10, 99), "B")

# 分隊加入陣列
Role = [AA, DD, BB, CC, FF, EE]
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
    if random.randint(1, 10) <= 0:  # 技能施放機率
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

# 判斷勝負


def win_lose(turn):
    if not teamA:
        print("teamA輸了")
    if not teamB:
        print("teamB輸了")
    if turn == 7 and teamA and teamB:
        print("平手")


# 戰鬥回合
for turn in range(8):
    print("第", turn+1, "回合")
    for fight_order in range(len(Role)):
        if Role[fight_order].team == "A":
            for i in range(len(teamB)):
                target = random.randint(i, len(teamB)+2) % len(teamB)
                if teamB[target].hp > 0:
                    attack(Role[fight_order], teamB[target])
                    # 如果目標hp=0將目標從team刪除
                    if teamB[target].hp == 0:
                        del teamB[target]
                        # for a in range(len(teamB)):
                        # print(teamB[a].__dict__)
                    break
        else:
            for i in range(len(teamA)):
                # 原先設置randint(i+1, len(team)),但會有(2,2)的頭尾相同情況發生，因此將範圍擴張至2倍可解決
                # %len(team)用以選取目標並僅限於陣列剩餘的數量
                target = random.randint(i, len(teamA)+2) % len(teamA)
                if teamA[target].hp > 0:
                    attack(Role[fight_order], teamA[target])
                    # 如果目標hp=0將目標從team刪除
                    if teamA[target].hp == 0:
                        del teamA[target]
                        # for a in range(len(teamA)):
                        # print(teamA[a].__dict__)
                    break

    win_lose(turn)

    if not teamA or not teamB:
        break
