def solution(survey, choices):
    answer = ''
    dictP = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    dictC = {}
    n=-3
    for i in range(1,8):
        dictC[i] = n
        n += 1
    
    for idx, c in enumerate(choices):
        if dictC[c] == 0:
            pass
        elif dictC[c] > 0:
            dictP[survey[idx][1]] += dictC[c]
        else:
            dictP[survey[idx][0]] += abs(dictC[c])
    
    #RT
    if dictP['R'] >= dictP['T']:
        answer += 'R'
    else:
        answer += 'T'
    #CF
    if dictP['C'] >= dictP['F']:
        answer += 'C'
    else:
        answer += 'F'
    #JM
    if dictP['J'] >= dictP['M']:
        answer += 'J'
    else:
        answer += 'M'
    #AN
    if dictP['A'] >= dictP['N']:
        answer += 'A'
    else:
        answer += 'N'
        

    return answer 