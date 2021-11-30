import sys
input = sys.stdin.readline

def binary_search(arr, h):
    l = 0
    r = len(arr) -1
    while l<=r: # 찾으려는 값 중 가장 앞에 있는 idx를 찾음
        mid = (l+r)//2
        if arr[mid] < h :
            l = mid+1
        else :
            r = mid-1
    return len(arr) - l #파괴하게 되는 장애물 수 return

N, H = map(int, input().split())
# %2 == 0 : 석순, %2 == 1: 종유석
jong = []
seok = []
for i in range(N):
    if i%2:
        jong.append(int(input()))
    else:
        seok.append(int(input()))

#이분 탐색은 정렬되어 있는 상태에서 가능
jong.sort()
seok.sort()

cnt = 0
min_obstacle = 200001
for i in range(1, H+1):
    broken_obstacle = binary_search(jong, i-0.5) + binary_search(seok,H-i+0.5) # 구간을 정해서 지나감
    if broken_obstacle < min_obstacle :
        min_obstacle = broken_obstacle
        cnt = 1
    elif broken_obstacle == min_obstacle :
        cnt += 1

print(min_obstacle, cnt)