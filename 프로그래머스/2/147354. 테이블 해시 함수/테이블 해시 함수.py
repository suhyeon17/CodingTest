def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x: (x[col-1], -x[0]))
    
    answer = 0
    for r in range(row_begin-1, row_end):
        s_i = 0
        for c in range(len(data[0])):
            s_i += data[r][c] % (r+1)
        answer ^= s_i

    return answer
        
            