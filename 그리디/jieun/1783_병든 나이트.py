N, M = map(int, input().split())

# 세로가 1이면 무조건 한칸밖에 못감
if N == 1:
    print(1)

# 세로가 2이면 갈수 있는 방법이 2가지밖에 없음 -> 이동횟수 4번이상이면 안됨 (3칸까지 방문 가능)
elif N == 2:
    print(min(4, (M+1)//2))

# 가로가 7이상이어야지만 이동횟수 4번이상 가능.
# 그 전에는 1칸씩 자기 길이만큼 이동하거나 어떻게든 3번이하로 이동하는 경우밖에 없음
elif M < 7:
    print(min(4, M))

# 이외에는 가로 길이 7까지는 모든 방법을 다 사용해서 방문하는 5칸 + 7 초과부터는 1칸씩 계속 방문 가능
else:
    print(M-7+5)