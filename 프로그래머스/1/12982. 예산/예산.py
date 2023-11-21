def solution(d, budget):
    sum = 0
    d.sort()
    
    for i in range(len(d)):
        sum += d[i]
        if sum > budget:
            return i
    
    return i+1