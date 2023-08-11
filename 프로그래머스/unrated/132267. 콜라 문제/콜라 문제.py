def solution(a, b, n):
    answer = 0
    extra = 0
    
    while n >= a:
        answer += n//a*b
        print('새로 받은 병', answer)
        extra = n%a
        print('남은 빈병', extra)
        n = n//a*b
        n += extra
        
        print('바꿀 수 있는 빈병 수', n)
    
    return answer