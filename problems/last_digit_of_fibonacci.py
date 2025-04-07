def last_digit(num):
    if num <= 1:
        return num

    a, b = 0, 1
    for i in range(2, num + 1):
        a, b = b, (a + b) % 10

    return b

x = int(input())
print(last_digit(x))