def solution(s, n):
    answer = ''
    
    for alpha in s:
        if alpha == ' ':
            answer += alpha
        elif alpha >= 'A' and alpha <= 'Z':
            ascii = ord(alpha) + n
            if ascii < 65 or ascii > 90:
                ascii -= 26
            answer += chr(ascii)
        else:
            ascii = ord(alpha) + n
            if ascii < 97 or ascii > 122:
                ascii -= 26
            answer += chr(ascii)
            
        
            
    return answer