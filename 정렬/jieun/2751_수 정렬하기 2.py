def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    new_arr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            new_arr.append(left[i])
            i += 1
        else:
            new_arr.append(right[j])
            j += 1

    if i==len(left):
        new_arr += right[j:]
    else :
        new_arr += left[i:]

    return new_arr

n = int(input())
num = [int(input()) for _ in range(n)]

for i in merge_sort(num):
    print(i)