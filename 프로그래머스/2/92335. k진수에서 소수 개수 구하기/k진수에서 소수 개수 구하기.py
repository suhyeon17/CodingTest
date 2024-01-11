def kJinsu(n, k):
    answer = []
    while n>0:
        answer.append(str(n%k))

        n//=k
        
    return ''.join(answer[::-1])

def sosu(n):
    if n == 2:
        return True
    cnt = 0
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    
    return True
        
def solution(n, k):
    answer = 0
    nums = kJinsu(n, k).split('0')
    
    for num in nums:
        if num == '' or num == '1':
            continue
        if sosu(int(num)):
            answer += 1
        
    return answer
            
