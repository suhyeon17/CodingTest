def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma" ]
    for b in babbling:
        for c in can:
            if c*2 not in b:
                b = b.replace(c, '1')
                
        if b.isdigit():
            answer += 1

    return answer