def fibonacci(n):
    if n <= 1:
        return n

    arr = []

    for i in range(n+1):
        if i == 0:
            arr.append(0)
        elif i == 1:
            arr.append(1)
        else:
            arr.append(arr[i - 1] + arr[i - 2])

    return arr

def sum_squares(num):
    arr = fibonacci(num)
    h = arr[num]
    l = arr[num-1] + arr[num]
    return h*l

num1 = int(input())
print(sum_squares(num1) % 10)
