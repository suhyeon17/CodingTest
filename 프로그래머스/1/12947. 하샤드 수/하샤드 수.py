def solution(x):
    sum = 0
    copy_x = x
    
    while x > 0:
        sum += (x%10)
        x //= 10
    
    
    if copy_x % sum == 0:
        return True
    else:
        return False