from itertools import combinations

def solution(nums):
    answer, cnt = 0, 0
    for comb in combinations(nums, 3):
        answer += 1
        n = sum(comb)
        for i in range(2, int(n**1/2) +1):
            if n % i == 0:
                cnt += 1
                break
        
    return answer - cnt