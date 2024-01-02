from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    cnt_dict = Counter(tangerine)
    cnt = sorted(cnt_dict.items(), key = lambda x:x[1], reverse = True)

    for c in cnt:
        print(c[1])
        k -= c[1]
        answer += 1
        
        if k <= 0:
            return answer