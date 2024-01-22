def solution(storey):
    answer = 0
    
    while storey:
        n = storey % 10
        if n > 5:
            answer += (10-n)
            storey //= 10
            storey += 1
        elif n < 5:
            answer += n
            storey //= 10
        else:
            answer += n
            storey //= 10
            if storey % 10 >= 5:
                storey += 1
    return answer