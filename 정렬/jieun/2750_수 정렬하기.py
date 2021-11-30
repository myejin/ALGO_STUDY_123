# 삽입
def insert_sort(array):
    for i in range(n-1):
        j = i
        while j >= 0 and array[j] > array[j+1]:
            array[j+1], array[j] = array[j], array[j+1]
            j-=1


# 버블
def bubble(array):
    for i in range(n-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


# 선택
def selection(array):
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

selection(numbers)

for z in numbers:
    print(z)
