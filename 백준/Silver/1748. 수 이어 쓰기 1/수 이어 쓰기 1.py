# 1자리수 9*1/2자리수 90*2/3자리수 900*3
n = int(input())
n_len = len(str(n))
count = 0

for i in range(n_len - 1):
    count += 9 * 10 ** i * (i + 1)

print(count + (n - 10 ** (n_len - 1) + 1) * n_len)



