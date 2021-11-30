N = int(input())
hap = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0}
for _ in range(N):
    data = input()
    for i in range(len(data)):
        hap[data[i]] += 10**(len(data)-i-1)

print(hap)
