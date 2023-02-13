h, m = map(int, input().split())
time = int(input()) #0<=time<=1000이라서 날짜 바뀌는거 고려해야함


start = h * 60 + m
end = start + time

h = end // 60
while h >= 24: #항상 범위 생각해주기
    #if h 30 -> 24h 빼주기
    h -= 24

m = end % 60

print(h, m)