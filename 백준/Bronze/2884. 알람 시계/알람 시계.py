h, m = map(int, input().split())

if h == 0:
    h = 24

total = h * 60 + m
total -= 45

h = total // 60
m = total % 60

if h == 24:
    h = 0

print(h, m)