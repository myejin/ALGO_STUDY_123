from collections import deque
n = int(input())
q = deque(map(str, range(n,0,-1)))
answer = deque()
met = list(map(int, input().split()))

for i in met[::-1]:
    if i == 1:
        answer.append(q.pop())

    elif i==2:
        temp = answer.pop()
        answer.append(q.pop())
        answer.append(temp)

    elif i == 3:
        answer.appendleft(q.pop())

answer.reverse()
print(' '.join(answer))