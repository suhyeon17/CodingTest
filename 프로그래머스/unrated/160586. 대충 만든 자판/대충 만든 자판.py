def solution(keymap, targets):
    answer = []
    keyDict = {}
    
    for key in keymap:
        for i, k in enumerate(key):
            if k in keyDict:
                if keyDict[k] >= i+1:
                    keyDict[k] = i+1
            
            else:
                keyDict[k] = i+1
                
    for target in targets:
        rst = 0
        for t in target:
            if t not in keyDict:
                rst = -1
                break
            rst += keyDict[t] 
        answer.append(rst)
    
    return answer