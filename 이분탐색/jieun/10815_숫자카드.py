N = int(input())
cards = list(map(int, input().split()))
M = int(input())
finds = list(map(int, input().split()))

answer = []


def binary_search(l, r, f):
    if l > r :
        return 0
    mid = (l + r) // 2
    if cards[mid] == f:
        return 1
    if f > cards[mid]:
        return binary_search(mid+1, r,f)
    else:
        return binary_search(l, mid-1, f)



cards.sort()
for fc in finds:
    answer.append(binary_search(0, N-1, fc))
print(*answer)