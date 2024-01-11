def solution(msg):
    LZW = {}
    for i in range(26):
        LZW[chr(65+i)] = i+1
    
    answer = []
    w, c, dict_num = 0, 0, 27

    while True:
        c += 1
        if c == len(msg):
            answer.append(LZW[msg[w:c]])
            return answer
        
        if msg[w:c+1] not in LZW:
            LZW[msg[w:c+1]] = dict_num
            dict_num += 1
            answer.append(LZW[msg[w:c]])
            w = c
        
