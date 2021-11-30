# 23, 46, 69, 92, ..... , 2300, 2323
# 그냥 23*k...
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    k = int(input())
    print(k*23)