def di_cnt(num):
    cnt = 0
    
    for i in range(1, num):
        if num % i == 0:
            cnt += 1
    
    return cnt 

def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        if di_cnt(i) % 2 == 0:
            answer += i
        else:
             answer -= i

    return abs(answer)