import sys
input = sys.stdin.readline


def find_p(x):
    if x != team[x]:
        team[x] = find_p(team[x])
        return team[x]
    else:
        return x


V, E = map(int, input().split())
team = [i for i in range(V+1)]
input_list = []
ans = 0
edge_cnt = 0

for _ in range(E):
    input_list.append(list(map(int, input().split())))

input_list.sort(key=lambda x: x[2])

for n1, n2, w in input_list:
    p1 = find_p(n1)
    p2 = find_p(n2)
    if p1 == p2:
        continue
    else:
        team[p1] = p2
        ans += w
        edge_cnt += 1
    if edge_cnt == V-1:
        break

print(ans)
