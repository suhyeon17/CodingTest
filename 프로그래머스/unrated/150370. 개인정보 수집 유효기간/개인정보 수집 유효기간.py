def solution(today, terms, privacies):
    answer = []
    
    t_y, t_m, t_d = map(int, today.split('.'))
    termDict = {}
    for term in terms:
        termType, month = term.split()
        termDict[termType] = int(month)
    
    p = {}
    for i, privacy in enumerate(privacies):
        date, termType = privacy.split()
        y, m, d = map(int, date.split('.'))
        y += (termDict[termType] // 12)
        m += (termDict[termType] % 12)
        if m > 12:
            y += 1
            m %= 12
        if d - 1 == 0:
            m -= 1
            d = 29
        p[i] = [y, m, d-1]
        if t_y > y:
            answer.append(i+1)
        elif t_y == y and t_m > m:
            answer.append(i+1)
        elif t_y == y and t_m == m and t_d > (d-1):
            answer.append(i+1)
    print(p)
    return answer