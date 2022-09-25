m, n = map(int, input().split())

def gcd(num1, num2):
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i 

def lcm(num1, num2):
    for i in range(max(num1, num2), (num1 * num2) + 1):
        if i % num1 == 0 and i % num2 == 0:
            return i

print(gcd(n, m))
print(lcm(n, m))
