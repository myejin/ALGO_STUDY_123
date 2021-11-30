# 트리 ??
# 내림차순 정렬해서 정렬전과 다르면 ... .......
# 위치 -1로 초기화 하고 ?? -> 다른 풀이
# 그냥 내림차순인지만 확인하면 된다!!

import sys
input = sys.stdin.readline

# 교과서 N, 더미 M
N, M = map(int, input().split())

for i in range(M):
    k = int(input())
    dummy = list(map(int, input().split()))
    # 그냥 현재 스택에 들어있는 값이 내림차순이 맞는지만 확인하면 된다.
    # 내림차순으로 들어있다면 무조건 순서대로 책을 꺼낼 수 있음
    if sorted(dummy, reverse=True) == dummy:
        continue
    else:
        print('No')
        break
else:
    print('Yes')




