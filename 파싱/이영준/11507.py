"""
Title : 카드셋트
Link : https://www.acmicpc.net/problem/11507
"""

s = input().strip()

cards = {
    'P': [0] * 14,
    'K': [0] * 14,
    'H': [0] * 14,
    'T': [0] * 14,
}

for i in range(len(s) // 3):
    type = s[i * 3]
    num = int(s[i * 3 + 1:i * 3 + 3])
    if cards[type][num]:
        print('GRESKA')
        break
    else:
        cards[type][num] = 1
else:
    print(13 - sum(cards['P']))
    print(13 - sum(cards['K']))
    print(13 - sum(cards['H']))
    print(13 - sum(cards['T']))
