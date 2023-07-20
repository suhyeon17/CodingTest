def solution(s):
    answer = []
    alphaDict = {}
    for i, alpha in enumerate(s):
        if alpha not in alphaDict:
            alphaDict[alpha] = i
            answer.append(-1)
        else:
            answer.append(i - alphaDict[alpha])
            alphaDict[alpha] = i
    return answer