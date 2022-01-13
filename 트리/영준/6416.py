"""
Title : 트리인가?
Link : https://www.acmicpc.net/problem/6416
"""

import sys, collections
input = sys.stdin.readline

# 인풋을 전부 다 받고 시행
cmd = []
while True:
    try:
        tmp = list(map(int, input().split()))
        if tmp == [-1, -1]:
            break
        cmd.append(tmp)
    except:
        break

# 테스트 케이스 별로 분류
test_case = []
tmp = []
# 줄 마지막이 0 0 이면 빼고 추가
# -1 -1 이면 종료
# 아니라면 tmp에 추가
for line in cmd:
    if line[-2:] == [0, 0]:
        tmp += line[:-2]
        test_case.append(tmp)
        tmp = []
    else:
        tmp += line


for tc in range(len(test_case)):
    edges = test_case[tc]
    
    # 트리 생성
    parent = dict()
    child = dict()
    vertex = set()
    for i in range(len(edges) // 2):
        u, v = edges[i * 2], edges[i * 2 + 1]
        vertex.update((u, v))
        if u in child:
            child[u].append(v)
        else:
            child[u] = [v]
        if v in parent:
            parent[v].append(u)
        else:
            parent[v] = [u]
    
    # 루트 확인
    root = list(vertex - set(parent.keys()))
    
    # 루트가 유일하지 않으면 종료
    if not edges:
        print(f'Case {tc + 1} is a tree.')
    
    elif len(root) != 1:
        print(f'Case {tc + 1} is not a tree.')
    
    # 그렇지 않으면 트리인지 확인
    else:
        vertex = list(vertex)
        visited = {v: False for v in vertex}
        visited[root[0]] = True
        queue = collections.deque(root)
        is_tree = True
        while queue:
            p = queue.popleft()
            if p not in child:
                continue
            for q in child[p]:
                # 이미 방문한 점이면, 트리가 아니므로 종료
                if visited[q]:
                    is_tree = False
                    break
                visited[q] = True
                queue.append(q)
        
        # 한 점을 두 점 이상에서 방문 가능한 경우
        if not is_tree:
            print(f'Case {tc + 1} is not a tree.')
        
        # root로 시작하는 부분은 트리가 됨
        # 다른 조각이 있는지 확인
        # visited에 False가 있는지 확인
        else:
            visited_check = list(set(visited.values()))
            
            if len(visited_check) == 2:
                print(f'Case {tc + 1} is not a tree.')
            else:
                print(f'Case {tc + 1} is a tree.')


'''
def find_root(tree_in, max_point):
    global point
    root_prob = []
    for i in range(1, max_point + 1):
        if tree_in[i] == []:
            root_prob.append(i)
    cnt = 0
    root = -1
    for prob in root_prob:
        if prob in point:
            cnt += 1
            root = prob
    
    if cnt == 1:
        return root
    else:
        return -1


def check_tree(tree_out, max_point, root):
    visited = [False] * (max_point + 1)
    visited[root] = True
    queue = collections.deque([root])
    while queue:
        p = queue.popleft()
        for q in tree_out[p]:
            if visited[q]:
                return False
            else:
                visited[q] = True
                queue.append(q)
    return True


tc = 1

while True:
    point = []
    while True:
        tmp = list(map(int, input().split()))
        point += tmp
        if tmp[-1] == 0 and tmp[-2] == 0:
            break
    max_point = 0
    # 트리 구성
    tree_in = collections.defaultdict(list)
    tree_out = collections.defaultdict(list)
    for i in range(0, len(point) // 2 - 1):
        a, b = point[i * 2], point[i * 2 + 1]
        tree_in[b].append(a)
        tree_out[a].append(b)
        max_point = max(max_point, a, b)
    
    # 트리인지 확인
    # 1. 루트 찾기 : 들어오는 선분이 없는 점 찾기
    
    root = find_root(tree_in, max_point)
    
    if root == -1 or not check_tree(tree_out, max_point, root):
        print(f'Case {tc} is not a tree.')
    else:
        print(f'Case {tc} is a tree.')
    
    try:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
    except:
        tc += 1
        continue
'''
