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


numbers = input()
num1, num2 = map(int, numbers.split(' '))
fib = fibonacci(num1)
result = fib % num2
print(result)