text = input()
cnt = 0
for i in range(len(text)-1):
    if text[i] != text[i+1]:
        cnt += 1
print((cnt+1)//2)