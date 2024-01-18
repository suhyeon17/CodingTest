def solution(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    r, c = -1, 0
    num = 1
    
    for i in range(n):
        if i % 3 == 0:
            for _ in range(n-i):
                r += 1
                arr[r][c] = num
                num += 1
        elif i % 3 == 1:
            for _ in range(n-i):
                c += 1
                arr[r][c] = num
                num += 1
        else:
            for _ in range(n-i):
                r -= 1
                c -= 1
                arr[r][c] = num
                num += 1
    answer = []  
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                answer.append(arr[i][j])
                
    return answer