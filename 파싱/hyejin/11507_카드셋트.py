S = input()
cards = {a:[1] * 13 for a in ['P', 'K', 'H', 'T']}
i = 0
while i < len(S):
    a, n = S[i], int(S[i + 1:i + 3])
    if cards[a][n - 1]:
        cards[a][n - 1] = 0
    else:
        print('GRESKA')
        break
    i += 3
else:
    for k, v in cards.items():
        print(13 - v.count(0), end=' ')
