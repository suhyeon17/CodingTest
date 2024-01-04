def solution(n, left, right):
    answer = []
    
    for idx in range(n):
        if idx < (left // n):
            continue
        if idx > (right // n):
            break
        arr = []
        for _ in range(idx+1):
            arr.append(idx+1)
        for x in range(idx+2, n+1):
            arr.append(x)

        answer += arr
    return answer[left%n:left%n+(right-left)+1]