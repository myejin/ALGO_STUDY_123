N = int(input())
nums = list(map(int, input().split()))

# 값이 하나인 경우 모든 a, b 조합 가능
if len(nums) == 1:
    print('A')
# 값이 2개인 경우
elif len(nums) == 2:
    # 값이 같은 경우 'a = 1' 또는 'b = x0' → 값은 동일
    if nums[0] == nums[1]:
        print(nums[0])
    # 다른 경우 여러 a, b 가능
    else:
        print('A')
else:
    # diff : 주어진 수 들의 차
    # → (a*x1 + b) - (a*x0 + b) = a(x1 - x0)
    diff = []
    for i in range(N - 1):
        diff.append(nums[i + 1] - nums[i])
    # 두번째 수 부터 모두 동일한 경우 (차이가 모두 0)
    # → 'a = 1' 또는 'b = x0' → 값은 동일
    if diff[1:].count(0) == len(diff) - 1:
        print(nums[-1])
        exit()
    # pat : diff 가 증가하는 배수 (패턴)
    pat = []
    for i in range(N - 2):
        # 배수가 무한대거나, 정수가 아닌 경우 성립 X
        if not diff[i] or diff[i + 1] % diff[i]:
            print('B')
            exit()
        pat.append(diff[i + 1] // diff[i])
    # 동일한 배수로 계속 증가하는 경우
    if pat.count(pat[0]) == len(pat):
        # 다음 diff 를 더해준 값을 출력
        print(nums[-1] + (diff[-1] * pat[0]))
    else:
        print('B')