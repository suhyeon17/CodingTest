def solution(s):
    s = s.split(' ')
    
    answer = []
    for word in s:
        if word == '':
            answer.append(word)
        elif word[0].isdigit():
            tmp = word[0] + word[1:].lower()
            answer.append(tmp)
        else:
            tmp = word[0].upper() + word[1:].lower()
            answer.append(tmp)
            
    return ' '.join(answer)
            
            
    