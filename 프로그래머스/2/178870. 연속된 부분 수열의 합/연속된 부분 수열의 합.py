def solution(sequence, k):
    answer = []
    n = len(sequence)
    e, sub_sum = 0, 0
    
    for s in range(n):
        while sub_sum < k and e < n:
            sub_sum += sequence[e]
            e += 1
            
        if sub_sum == k:
            answer.append([s, e-1, e-s-1])
        
        sub_sum -= sequence[s]
    
    answer.sort(key = lambda x:(x[-1], x[0]))
    return answer[0][0:2]