#연속한 자연수가 중요 조건!!, 2중반복가능
#1. for i in range(n+1):
#2.     for j in range(i, n+1):
#3.         만약 j부터 순차적으로 더해서 15가 될때 cnt += 1 브레이크
#4.         15가 넘어가면 그냥 안되는거니까 브레이크


def solution(n):
    cnt = 0
    
    for i in range(1, n+1):
        total = 0
        for j in range(i, n+1):
            total += j
            if total == n:
                cnt += 1
                break
            elif total > n:
                break
            else: pass
                
    return cnt