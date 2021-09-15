import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    sounds = list(map(str, input().split()))

    other_sound = []
    result = []

    while True:
        # 동물들의 울음소리는 한 단어이기에 리스트화하여 마지막 요소만 사용
        S = list(map(str, input().split()))
        if S[-1] == 'say?':
            break
        other_sound.append(S[-1])
    
    for sound in sounds:
        if sound not in other_sound:
            result.append(sound)

    print(*result)