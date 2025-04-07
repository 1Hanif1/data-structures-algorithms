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

def partial_sum(m, n):
    arr = fibonacci(n)
    sum = 0
    for i in range(m, n+1):
        sum += arr[i]
    return sum

numbers = input().strip()
num1, num2 = map(int, numbers.split())
print(partial_sum(num1, num2) % 10)

