def solution(s):
    answer = []
    word = s.lower().split(' ')
    print(word)
    
    for w in word:
        w = list(w)
        if len(w) != 0:
            w[0] = w[0].upper()
        
        answer.append(''.join(w))
        
    answer = ' '.join(answer)
    
    return answer