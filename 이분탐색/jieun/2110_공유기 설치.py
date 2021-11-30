import sys
input = sys.stdin.readline
N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

l = 1
r = max(houses)
result = 0
while l <= r:
    mid = (l+r)//2
    old = houses[0] #무조건 첫 번째 집에 설치하고 시작
    cnt = 1 #첫 번째 집에 설치된 상태
    for house in houses:
        # 이전 집과의 거리가 최소거리 이상일 경우만 cnt + 후 이전집 갱신
        if house >= old + mid :
            cnt += 1
            old = house
    if cnt >= C :
        l = mid + 1
        result = mid
    else :
        r = mid - 1
print(result)