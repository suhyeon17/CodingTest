from collections import Counter

def solution(clothes):
    answer = 1
    clo_dict = Counter([k for n, k in clothes])
    
    for k, num in clo_dict.items():
        answer *= (num+1)
        
    return answer - 1
    