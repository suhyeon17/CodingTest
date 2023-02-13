import sys
#sys.stdin.readline() == input()
#input = sys.stdin.readline이라고 정의해놓고 써도 됨

input = sys.stdin.readline

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(a + b)