import sys
input = sys.stdin.readline
S, C = map(int, input().split())
green_onion = []
for _ in range(S):
    green_onion.append(int(input()))

green_onion.sort()
l = 1
r = green_onion[-1]
sum_g = sum(green_onion)
answer = 0
while l<=r:
    mid = (l+r)//2
    cnt = 0
    left = 0
    for g_o in green_onion: #해당 길이로 파닭에 얼마나 넣을 수 있는지 계산
        cnt += g_o // mid
    if cnt >= C : #파의 수와 파닭의 수가 같은 경우에도, 더 많은 양의 파를 넣어야 함
        l = mid + 1
        answer = max(answer, mid) #현재 파의 양과 이전에 저장된 파 중 많은 양 저장
    else :
        r = mid - 1

print(sum_g-answer*C)