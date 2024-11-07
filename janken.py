import random

print('1.グー  2.チョキ  3.パー')
print(f'あなたの手を入力してください')
hand = int(input())
if hand == 1:
    print('あなたの手: グー')
elif hand == 2:
    print('あなたの手は: チョキ')
elif hand == 3:
    print('あなたの手は: パー')
else:
    print('1,2,3 のどれかで入力してください')
CPU = random.randint(1,3)
print(CPU)