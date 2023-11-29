def solution(s):
    answer = []
    words = s.split(' ')
    
    for word in words:
        new = ''
        n = len(word)
        for i in range(n):
            if i%2 == 0:
                new += word[i].upper()
            else:
                new += word[i].lower()
    
        answer.append(new)
        
    return ' '.join(answer)