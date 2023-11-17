def makeBinary(n):
    binary = []
    
    while n > 0:
        binary.append(n%2)
        n //= 2
    
    return binary

def solution(n):
    cnt = makeBinary(n).count(1)
    
    while True:
        n += 1
        
        if makeBinary(n).count(1) == cnt:
            return n
    
    
    
    
    