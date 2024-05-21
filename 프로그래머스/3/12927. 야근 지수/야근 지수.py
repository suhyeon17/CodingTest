import heapq as hq

def solution(n, works):
    h = []
    for w in works:
        hq.heappush(h, -w)
    
    while n:
        m = hq.heappop(h)
        if m == 0:
            break
        hq.heappush(h, m + 1)
        n -= 1
        
    return sum(i**2 for i in h)
        
        