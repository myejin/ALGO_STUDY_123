# S5 11507 카드셋트
# https://www.acmicpc.net/problem/11507

card = input()

# dictionary로 card_set을 만들어서 각 카드 모양을 키로 둔다.
card_set = {'P': [], 'K': [], 'H': [], 'T': []}
i, flag = 0, 0
while i < len(card):
    word = card[i:i+3]          # 3개씩 잘라서 word로 저장한다.

    # word[0]은 카드모양, card_set의 키의 value에 숫자가 없으면 저장
    if word[1:] not in card_set[word[0]]:
        card_set[word[0]].append(word[1:])
    else:   # 숫자가 있으면 break
        print('GRESKA')
        flag = 1
        break
    i += 3

# 2개의 같은 카드가 존재하지 않았다면 해당 value의 길이를 재서 13에서 빼면 몇개의 카드를 잃어버렸는지 알 수 있다.
if not flag:
    for value in card_set.values():
        print(13 - len(value), end=' ')

