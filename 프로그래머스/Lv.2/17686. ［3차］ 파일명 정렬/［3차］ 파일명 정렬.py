import re

def solution(files):
    new = []
    answer = []
    
    for i, file in enumerate(files):
        nfile = re.split(r'([0-9]+)', file)
        nfile[1] = '0'*(5-len(nfile[1])) + nfile[1]
        nfile[0] = nfile[0].lower()
        new.append((nfile, i))
        
    new.sort(key = lambda s:(s[0][0],s[0][1], s[1]))
    
    for i in range(len(new)):
        answer.append(files[new[i][1]])
        
    return answer