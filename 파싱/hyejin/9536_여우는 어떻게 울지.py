tc = int(input())
for _ in range(tc):
    sounds = list(input().split())
    noise = []
    while True:
        inp = input().split()
        if inp[0] != 'what':
            noise.append(inp[2])
        else:
            break

    noise = set(noise)
    for sound in sounds:
        if sound not in noise:
            print(sound, end=' ')
    print()
