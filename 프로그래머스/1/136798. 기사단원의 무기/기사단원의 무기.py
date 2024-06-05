def divisor(n):
    cnt = 0
    
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            if i ** 2 != n:
                cnt += 2
            else: 
                cnt += 1
    
    return cnt

def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1):
        hp = divisor(i)
        if hp > limit:
            hp = power
            
        answer += hp
        
    return answer