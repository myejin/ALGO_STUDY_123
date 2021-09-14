import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    records = input().rstrip().split()
    sound = set()
    while True:
        sentence = input().rstrip()
        if sentence == 'what does the fox say?':
            break
        sound.add(sentence.split()[2])
    for record in records:
        if record not in sound:
            print(record, end=' ')
    print()