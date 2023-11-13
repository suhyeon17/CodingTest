def solution(n):
    trit = []
    
    #거꾸로 3진수 변환
    while n > 0:
        trit.append(n%3)
        n //= 3
        
    print(trit)
    #10진수로
    length = len(trit)
    decimal = 0 
    for i in range(length):
        decimal += trit[i] * 3**(length-1-i)
    
    return decimal