def solution(k, d):
    cnt = 0
    valid = dict()
    
    for i in range(d+1):
        y = int(((d**2) - (i**2)) ** (1/2))
        valid[i] = y
        
    for i in range(0, d+1, k):
        cnt += (valid[i] // k) + 1
        
    return cnt