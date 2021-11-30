import sys
input = sys.stdin.readline


def check():
    for i in range(0, n):
        if origin[i] != change[i]:
            return False
    return True


def flip(i):
    origin[i] = 1 - origin[i]
    if i == 1:
        origin[i+1] = 1 - origin[i+1]
    elif i == n:
        origin[i-1] = 1 - origin[i-1]
    else :
        origin[i + 1] = 1 - origin[i + 1]
        origin[i - 1] = 1 - origin[i - 1]


n = int(input())
origin = [0] + list(map(int, list(input().rstrip())))
change = [0] + list(map(int, list(input().rstrip())))

cnt = 0
for i in range(1, n+1):
    if origin[i] != change[i]:
        flip(i)
        print(origin)


if check():
    print(cnt)

else:
    print(-1)