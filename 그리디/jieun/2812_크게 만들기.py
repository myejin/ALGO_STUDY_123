N, K = map(int, input().split())
num = input()
stack = [num[0]]
for i in range(1, N):
    if int(stack[-1]) < int(num[i]) and K:
        while stack:
            if int(stack[-1]) >= int(num[i]):
                break
            stack.pop()
            K -= 1
            if not K:
                break
    stack.append(num[i])

while K:
    stack.pop()
    K -= 1

print(''.join(stack))
