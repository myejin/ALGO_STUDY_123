idx = 0
while True:
    idx +=1
    l, p, v = map(int, input().split())

    if l == p == v == 0:
        break

    if v%p > l :
        print(f'Case {idx}: {(v//p)*l+l}')

    else :
        print(f'Case {idx}: {(v//p)*l+v%p}')