import sys
input = sys.stdin.readline
sentence = input().rstrip()
bomb_sen = input().rstrip()

stack = []

for char in sentence:
    stack.append(char)
    if char == bomb_sen[-1] and len(stack) >= len(bomb_sen) and ''.join(stack[-len(bomb_sen):]) == bomb_sen :
        cnt = 0
        while cnt < len(bomb_sen):
            stack.pop()
            cnt += 1

if stack:
    print(''.join(stack))

else:
    print('FRULA')


# new_sentence = ''
# len_bomb = len(bomb_sen)
# i = 0
#
# isNotBomb = True
# while isNotBomb:
#     i = 0
#     isNotBomb = False
#     len_sen = len(sentence)
#     while i < len_sen :
#         if i+len_bomb-1 < len_sen and sentence[i:i+len_bomb] == bomb_sen:
#             i += len_bomb
#             isNotBomb = True
#         else :
#             new_sentence += sentence[i]
#             i += 1
#     sentence = new_sentence
#     new_sentence=''
#
# if sentence:
#     print(sentence)
# else:
#     print('FRULA')
