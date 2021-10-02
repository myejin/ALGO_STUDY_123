# 주어진 크기에 size에 해당하는 큐브를 최대로 채우기
def box_fill(l, w, h, size):
    if size < 0:
        return
    if 2**size <= l and 2**size <= w:
        x = l // (2**size)
        y = w // (2**size)
        z = h // (2**size)
        cube_cnt[size] += x*y*z
        # length에 남은 공간이 생길 경우
        if l % (2**size):
            box_fill(l-(2**size)*x, (2**size)*y, h, size-1)
        # width에 남은 공간이 생길 경우
        if w % (2**size):
            box_fill(l, w-(2**size)*y, h, size-1)
    else:
        # size의 큐브로 채울 수 없는 경우
        box_fill(l, w, h, size-1)
    

l, w, h = map(int, input().split())
N = int(input())
cube = [0]*20
cube_cnt = [0]*20  # 요구되는 큐브의 개수 체크

for _ in range(N):
    A, B = map(int, input().split())
    cube[A] = B

# 크기가 큰 큐브부터 채우기
for i in range(19, -1, -1):
    if h > 0:
        if (2**i) <= l and (2**i) <= w and (2**i) <= h:
            height = h % (2**i)
            # 가능한 높이(h-height)만큼 채우기
            box_fill(l, w, h-height, i)
            h = height

# 큰 큐브가 부족한 경우 한 단계 작은 크기의 큐브 8개로 변환
for i in range(19, 0, -1):
    if cube_cnt[i] > cube[i]:
        cube_cnt[i-1] += (cube_cnt[i] - cube[i]) * 8
        cube_cnt[i] = cube[i]

# 가장 작은 큐브만 검사하여 채울 수 있는지 판별
if cube_cnt[0] > cube[0]:
    print(-1)
else:
    print(sum(cube_cnt))