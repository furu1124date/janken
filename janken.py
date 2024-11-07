import random

print('1.グー  2.チョキ  3.パー')
print(f'あなたの手を入力してください')
hand = int(input())
CPU = random.randint(1,3)
if hand == 1:
    print('あなたの手: グー')
elif hand == 2:
    print('あなたの手は: チョキ')
elif hand == 3:
    print('あなたの手は: パー')
if(hand == CPU):
    print("あいこです。")
elif(hand == 1 and CPU_hand == 2) or (hand == 2 and CPU_hand == 3) or (hand == 3 and CPU_hand == 1):
    print("<><><><><><><><>")
    print("あなたの勝ちです！")
    print("<><><><><><><><>")
else:
    print("<><><><><><><><>")
    print("あなたの負けです！")
    print("<><><><><><><><>")
else:
    print('1,2,3 のどれかで入力してください')
