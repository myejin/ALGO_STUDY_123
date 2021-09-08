"""
Title : 캠핑
Link : https://www.acmicpc.net/problem/4796
"""

tc = 0
while True:
    l, p, v = map(int, input().split())
    tc += 1
    if l == 0 and p == 0 and v == 0:
        break
    
    cnt = 0
    cnt += (v // p) * l
    
    cnt += min(l, v % p)
    
    print(f'Case {tc}: {cnt}')