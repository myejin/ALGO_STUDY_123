num_cards = {'P':13, 'K':13, 'H':13, 'T':13}
S = input()
card_set = set()

isSame = False
for idx in range(0, len(S), 3):
    if S[idx:idx+3] in card_set :
        isSame = True
        print('GRESKA')
        break
    card_set.add(S[idx:idx+3])
    num_cards[S[idx]] -= 1

if not isSame:
    print(*num_cards.values())
