n = int(input())
num_list = list(map(int, input().split()))

def is_prime(num):
    if num == 1:
        return 0

    for i in range(2, num):
        if num % i == 0:
            return 0
    
    return 1

cnt = 0
for i in num_list:
    cnt += is_prime(i)

print(cnt)