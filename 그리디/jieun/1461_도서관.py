N, M = map(int, input().split())
data = list(map(int, input().split()))
pos = []
neg = []
max_value = 0
for d in data:
    if d > 0:
        pos.append(d)
    else:
        neg.append(d)
    if max_value < abs(d):
        max_value = abs(d)

pos.sort(reverse=True)
neg.sort()


answer = 0
for i in range(0, len(pos), M):
    if pos[i] != max_value:
        answer += pos[i] * 2
for i in range(0, len(neg), M):
    if neg[i] != - max_value:
        answer += abs(neg[i] * 2)

print(answer+max_value)