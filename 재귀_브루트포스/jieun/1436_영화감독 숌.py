n = int(input())

name = 666
cnt = 0

while True:
    if "666" in str(name):
        cnt += 1
        if cnt == n :
            print(name)
            break
    name += 1