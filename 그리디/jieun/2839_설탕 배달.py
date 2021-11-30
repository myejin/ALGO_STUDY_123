n = int(input())

num_5 = n//5

while True:
    ret = n - num_5*5
    if ret%3 == 0:
        print(num_5+ret//3)
        break
    num_5 -= 1
    if num_5 < 0 :
        print(-1)
        break