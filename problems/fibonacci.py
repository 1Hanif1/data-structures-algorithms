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

    return arr[-1]


x = int(input())
print(fibonacci(x))