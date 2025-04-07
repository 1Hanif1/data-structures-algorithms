def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

numbers = input().strip()
num1, num2 = map(int, numbers.split())

G = gcd(num1, num2)
LCM = (num1 * num2) // G  # Integer division to keep it neat
print(LCM)