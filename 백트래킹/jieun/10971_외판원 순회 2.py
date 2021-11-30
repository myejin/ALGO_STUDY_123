import sys
input = sys.stdin.readline
N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]

min_cost = 10**9
visited = [False]*(N+1)

def tsp(start, now, cnt, cost):
    global min_cost

    if cnt == N:
        if city[now][start] :
            min_cost = min(min_cost, cost+city[now][start])
        return

    for j in range(N):
        if j != start and city[now][j] != 0 and visited[j] == False:
            visited[j] = True
            tsp(start, j, cnt+1, cost+city[now][j])
            visited[j] = False

visited[0] = True
tsp(0, 0, 1, 0)
print(min_cost)