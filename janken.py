import random
def janken_game():
    player_score = 0
    cpu_score = 0
    rounds = 3

    for i in range(rounds):
        print('1. グー  2. チョキ  3. パー')
        hand = int(input('あなたの手を入力してください: '))

        if hand == 1:
            print('あなたの手: グー')
        elif hand == 2:
            print('あなたの手: チョキ')
        elif hand == 3:
            print('あなたの手: パー')
        else:
            print('1, 2, 3 のどれかで入力してください')
            continue  

        CPU_hand = random.randint(1, 3)
        if CPU_hand == 1:
            print('CPUの手: グー')
        elif CPU_hand == 2:
            print('CPUの手: チョキ')
        else:
            print('CPUの手: パー')

        if hand == CPU_hand:
            print("あいこです。")
        elif (hand == 1 and CPU_hand == 2) or (hand == 2 and CPU_hand == 3) or (hand == 3 and CPU_hand == 1):
            print("<><><><><><><><>")
            print("あなたの勝ちです！")
            print("<><><><><><><><>")
            player_score += 1
        else:
            print("<><><><><><><><>")
            print("あなたの負けです！")
            print("<><><><><><><><>")
            cpu_score += 1

    if player_score > cpu_score:
        print("あなたの総合勝利です！")
    elif player_score < cpu_score:
        print("CPUの総合勝利です！")
    else:
        print("引き分けです！")

janken_game()