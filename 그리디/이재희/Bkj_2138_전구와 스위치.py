N = int(input())
arr1 = list(map(int, input()))
arr2 = list(map(int, input()))

# 배열을 하나 더 만들어 첫 스위치를 누를 때와 누르지 않을 때로 나누어 계산
arr1_2 = list(arr1)
result = -1

# 첫 스위치를 누르는 경우
cnt = 0
for i in range(N):
    if i == 0:
        cnt += 1
        for t in range(i, i+2):
            arr1[t] = 1 - arr1[t]
    else:
        if arr1[i-1] != arr2[i-1]:
            cnt += 1
            for t in range(i-1, min(i+2, N)):
                arr1[t] = 1 - arr1[t]

if arr1 == arr2:
    result = cnt

# 첫 스위치를 누르지 않는 경우
cnt = 0
for i in range(N):
    if i == 0:
        continue
    else:
        if arr1_2[i-1] != arr2[i-1]:
            cnt += 1
            for t in range(i-1, min(i+2, N)):
                arr1_2[t] = 1 - arr1_2[t]

# 첫 스위치를 누르거나 누르지 않는 경우 중 작은 값을 결과에 입력
if arr1_2 == arr2:
    if result != -1:
        result = min(result, cnt)
    else:
        result = cnt

print(result)