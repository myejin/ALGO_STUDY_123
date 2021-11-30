n = int(input())
arr = list(map(int,input().split()))
remove = int(input())
tree = {}
for i in range(n): # 트리 생성
    if i == remove or arr[i] == remove : # 없애야 될 서브트리는 생성하지 않음
        continue
    if arr[i] in tree.keys(): # 자식이 있으면 key 추가
        tree[arr[i]].append(i)
    else:
        tree[arr[i]]=[i]

check = []
if -1 in tree.keys(): # 루트가 남아 있는지 확인
    check.append(-1)

answer = 0
while check: # 트리를 타고 들어가면서 자식이 없으면(key가 없으면) answer +
    now = check.pop()
    if now not in tree.keys():
        answer +=1
    else:
        check.extend(tree[now])
print(answer)