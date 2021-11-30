from itertools import permutations

n, k = int(input()), int(input())
cards = [input() for i in range(n)]
ans = set()

for per in permutations(cards, k):
    ans.add(''.join(per))

print(len(ans))