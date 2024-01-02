from math import ceil

def solution(n,a,b):
    cnt = 0
    
    if a > b:
        a, b = b, a
    
    while a != b:
        a = ceil(a/2)
        b = ceil(b/2)
        print(a, b)
        cnt += 1
        
    return cnt
    