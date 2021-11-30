def binary(num):
    if num <= 1 :
        return str(num)
    a, b = divmod(num, 2)
    return binary(a)+str(b)

n = int(input())
print(binary(n))
