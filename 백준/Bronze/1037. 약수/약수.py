cnt = int(input())
divisor = list(map(int, input().split()))

# cnt는 자연수이므로 항상 0보다 큼 -> 소수의 경우는 해당이 안됨
# divisor list에서 가장 작은 수와 가장 큰 수를 곱하면 답 

divisor.sort()

min = divisor[0]
max = divisor[-1]
n = min * max

print(n)