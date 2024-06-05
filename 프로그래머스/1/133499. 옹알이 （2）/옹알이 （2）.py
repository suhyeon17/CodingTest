#1. ["aya", "ye", "woo", "ma"]
#2. for b in babbling:
#3.     연속된거 처리? -> '다른걸로 대체'
#4.     b.replace(aya, '')

def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        for c in can:
            b = b.replace(c*2, 'not')
            b = b.replace(c, '1')

        
        if b.isdigit():
            answer += 1
            
    return answer