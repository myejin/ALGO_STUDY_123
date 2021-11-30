import sys
input = sys.stdin.readline
for _ in range(int(input())):
    A, B, C = map(int, input().split())
    # ㄴ자 타일이 1*1 보다 많으면 무조건 No
    if C > A:
        print('No')
        continue
    # 1
    if A>0 and B%2:
        B -= 1
    if not ((A-C) % 2) and not B % 2:
        print('Yes')
    else:
        print('No')
