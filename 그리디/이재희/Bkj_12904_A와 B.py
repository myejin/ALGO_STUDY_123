S = str(input())
T = str(input())

# T를 S와 길이가 같아질 때 까지 역으로 연산
while len(S) < len(T):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[-2::-1]

if S == T:
    print(1)
else:
    print(0)