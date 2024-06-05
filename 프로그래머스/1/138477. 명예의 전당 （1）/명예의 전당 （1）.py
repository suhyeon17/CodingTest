#1. for s in score:
#2.     q.append(s)
#3.     q의 길이가 3을 벗어나면 최속값 제거
def solution(k, score):
    answer = []
    
    q = []
    for s in score:
        q.append(s)
        
        if len(q) > k:
            q.remove(min(q))
        answer.append(min(q))
    
    return answer