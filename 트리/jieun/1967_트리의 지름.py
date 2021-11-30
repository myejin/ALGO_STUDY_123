import sys
input = sys.stdin.readline

# 가장 긴 점 찾고 -> 이 점 기준으로 다시 탐색! -> 다시 풀기

def find_long(start):
    max_length, max_start = 0, 0
    visited = [0]*(N+1)
    q = [(start, 0)]
    visited[start] = 1
    end = 0
    my_max = 0
    while q:
        ct, cw = q[-1]
        if cw > my_max :
            end = ct
            my_max = cw
        for next, weight in tree[ct]:
            if not visited[next]:
                q.append((next, cw+weight))
                visited[next] = 1
                break
        else:
            q.pop()
    return end, my_max


N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, weight = map(int, input().split())
    tree[a].append([b, weight])
    tree[b].append([a, weight])

end, _ = find_long(1)
_, my_max = find_long(end)

print(my_max)
