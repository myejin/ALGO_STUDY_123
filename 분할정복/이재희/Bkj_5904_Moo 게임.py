# 'm', 'o' 판별
def check_m_o(n, k):
    # S(k-1)의 길이보다 작은 경우 'k-1'에서 판별
    if k and n <= moo_arr[k-1]:
        return check_m_o(n, k-1)
    # k가 초기값이 아닌 경우 S(k-1)의 길이만큼 자르기
    if k:
        n -= moo_arr[k-1]
    # 중앙에 추가되는 문자열의 길이보다 작을 경우 바로 판별
    if n <= k+3:
        if n == 1:
            return 'm'
        else:
            return 'o'
    # 아닌 경우 중앙의 문자열 길이만큼 자르기
    else:
        n -= (k+3)
    return check_m_o(n, k-1)

N = int(input())

k = 0
moo_arr = [3]  # S(0)에 해당하는 길이 초기화
while True:
    # k가 0이 아닌 경우 S(k) 길이 추가
    if k:
        moo_arr.append(moo_arr[k-1]*2 + k+3)
    # N이 S(k)의 길이보다 작을 경우 break
    if N <= moo_arr[k]:
        break
    k += 1

print(check_m_o(N, k))