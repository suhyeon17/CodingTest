def solution(brown, yellow):
    for j in range(1, yellow+1):
        if yellow % j != 0:
            continue
        i = yellow // j
        if (i+2) * (j+2) == brown+yellow:
            break
            
    return [i+2, j+2]