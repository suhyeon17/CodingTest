def solution(s, skip, index):
    answer = ''
    for alpha in s:
        ascii1 = ord(alpha)
        cnt = 0
        while cnt != index :
            if ascii1 + 1 > 122:
                ascii1 = 96
            if chr(ascii1 + 1) in skip:
                ascii1 += 1
            else:
                ascii1 += 1
                cnt += 1
  
        answer += chr(ascii1)
            
    return answer