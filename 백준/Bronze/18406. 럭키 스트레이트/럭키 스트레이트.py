import sys

N = list(map(int, sys.stdin.readline().rstrip()))

left, right = sum(N[:len(N)//2]), sum(N[len(N)//2:]) 

if left == right:
    print('LUCKY')
else:
    print('READY')