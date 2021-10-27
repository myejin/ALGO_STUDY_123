import sys
input = sys.stdin.readline


def find_p(x):
    if x != p[x]:
        p[x] = find_p(p[x])
        return p[x]
    else:
        return x


N, M = map(int, input().split())
university = list(input().split())
input_list = []
p = [i for i in range(N)]
for _ in range(M):
    u, v, d = map(int, input().split())
    input_list.append([u-1, v-1, d])

input_list.sort(key=lambda x:x[2])
ans = 0
edge_num = 0

for i in range(M):
    u, v, d = input_list[i]

    if university[u] == university[v]:
        continue
    else:
        p1 = find_p(u)
        p2 = find_p(v)
        if p1 == p2:
            continue
        else:
            p[p1] = p2
            ans += d
            edge_num += 1
    if edge_num == N - 1:
        break

if edge_num == N - 1:
    print(ans)
else:
    print(-1)