def solution(n):
    a, b = 1, 1 
    
    if n == 2:
        return 1 % 1234567
    else:
        for i in range(1, n):
            a, b = b, a+b
            
        return a % 1234567        
    