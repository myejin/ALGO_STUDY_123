n = int(input())
l, r = 0, n
while l <= r:
    mid = (l+r)//2
    print(mid)
    if mid**2 < n :
        l = mid + 1
    else:
        r = mid - 1

print(l)