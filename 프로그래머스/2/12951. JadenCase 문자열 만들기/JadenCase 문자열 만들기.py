def solution(s):
    JadenCase = ''
    s = s.lower()
    s = s.split(' ')
    
    for word in s:
        if len(word) != 0:
            new_word = word[0].upper() + word[1:]
            JadenCase += new_word
            
        JadenCase += ' '
    
    return JadenCase[:-1]