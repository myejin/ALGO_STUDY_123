N, M = map(int, input().split())
blu_ray = list(map(int, input().split()))
l = max(blu_ray)
r = sum(blu_ray)
answer = 1000000001
while l <= r: # 최솟값 혹은 최소값을 가진 인덱스 -> l 반환
    mid = (l+r)//2
    cnt = 1
    res = mid
    for track in blu_ray:
        if res < track:
            cnt += 1
            res = mid
        res -= track
    if cnt <= M :
        r = mid - 1
    else :
        l = mid + 1

print(l)
