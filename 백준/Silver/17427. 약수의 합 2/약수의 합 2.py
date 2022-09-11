n = int(input())

'''
# 시간복잡도 = O(n^2) -> 시간초과이므로 for문 하나만 있는걸 고려
def divisor(n):
    div_sum = 0

    for i in range(1, n+1):
        if n % i == 0:
            div_sum += i

    return div_sum

rst = 0
for i in range(1, n+1):
    rst += divisor(i)

print(rst)    
'''

# g(6) = 1*1 + 2*3 + 3*2 + 4*1 + 5*1 + 6*1
# 즉 자연수 1*1/6 + 2*2/6 + ... + n*n/6

div_sum = 0
for i in range(1, n+1):
    div_sum = div_sum + (i * (n // i))

print(div_sum)