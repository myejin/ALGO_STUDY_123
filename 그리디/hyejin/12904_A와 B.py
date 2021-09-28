S = list(input())
T = list(input())

while len(T) >= len(S):
    if T == S:
        print(1)
        break
    p = T.pop()
    if p == 'B':
        T.reverse()
else:
    print(0)
