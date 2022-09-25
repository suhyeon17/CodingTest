# 소수 데이터 리스트
num = 1000001
prime = [True for _ in range(num)]
for i in range(2, int((num-1)**0.5) + 1) :
    if prime[i] :
        for j in range(i + i, num, i) :
            prime[j] = False

def goldbach(n, prime):
    for i in range(3, n + 1, 2):
        if prime[i] and prime[n - i]:
            return print('%d = %d + %d'%(n, i, n - i))

    return print("Goldbach's conjecture is wrong.") 

while True:
    n = int(input())
    if n == 0:
        break
    goldbach(n, prime)
    