import sys
input = sys.stdin.readline


# 이전 노드 정보를 갖고 있어야 하므로 while보다는 재귀 형태로 계속 이전노드를 넘겨주는 게 편리하다
def dfs(start: int, prev: int, visited: list):
    visited[start] = True
    for next_node in graph[start]:
        if next_node == prev: # 이전 노드와 다음 노드가 같으면 무시
            continue
        if visited[next_node] : #이미 방문한 노드(cycle이 생김)면 False
            return False
        # next_node로 dfs를 다시 돌렸을때 True가 아니면 False 반환
        if not dfs(next_node, start, visited):
            return False
    return True


tc = 0

while True:
    tc += 1
    n, m = map(int, input().split())
    if n == m == 0: #탈출
        break
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0]*(n+1)
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            if dfs(i, 0, visited):
                cnt += 1
    if cnt == 0 :
        print('Case {}: No trees.'.format(tc))
    elif cnt == 1 :
        print('Case {}: There is one tree.'.format(tc))
    else :
        print('Case {}: A forest of {} trees.'.format(tc, cnt))