import sys
n = int(sys.stdin.readline())
size = 10001
cntlist = [0]*size

for i in range(n) :
    cntlist[int(sys.stdin.readline())]+=1

for i in range(size):
    if cntlist[i] != 0:
        for j in range(cntlist[i]):
            print(i)

