def solution(n):
    answer = ''
    pattern = '124'

    while n != 0:
        r = n%3
        answer += pattern[r-1]
        if r == 0:
            n -= 1
            
        n//=3

    return answer[::-1]