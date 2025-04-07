def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

numbers = input()
num1, num2 = numbers.split(' ')
print(gcd(int(num1), int(num2)))