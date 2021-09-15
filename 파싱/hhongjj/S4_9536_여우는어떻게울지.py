# S4 9536 여우는 어떻게 울지?
# https://www.acmicpc.net/problem/9536
# 문자열, 파싱

T = int(input())
for _ in range(T):
    voice = input().split(' ')
    sound = []        # 다른 동물의 울음소리

    while True:
        animal = input().split(' goes ')   # goes 를 기준으로 자른다.

        if 'what does the fox say?' in animal:  # 질문이 들어왔으면 break
            break
        else:
            sound.append(animal[1])   # 울음 소리 저장

    for v in voice:
        if v not in sound:    # 다른 동물의 울음소리가 아니라면 print
            print(v, end=' ')

# 혹시나 싶어서 뒤에 공백 제거
# for s in sound:
#     for _ in range(voice.count(s)):
#         voice.remove(s)
#
# print(*voice)

# 테스트 케이스 생각을 안해서 엄청 틀림.. 문제 제대로 읽어보기!