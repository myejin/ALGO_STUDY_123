def card_count():
    global card_check
    for i in range(0, len(S), 3):
        shape = S[i]
        num = int(S[i+1:i+3])
        if card_check[shape_dic[shape]][num-1] == 1:
            card_check[shape_dic[shape]][num-1] = 0
        else:
            print('GRESKA')
            return
    print(f'{sum(card_check[0])} {sum(card_check[1])} {sum(card_check[2])} {sum(card_check[3])}')
    return
    

S = str(input())

shape_dic = {'P': 0, 'K': 1, 'H': 2, 'T': 3}
card_check = [[1] * 13 for _ in range(4)]  # 2차원 배열으로 카드 카운팅

card_count()