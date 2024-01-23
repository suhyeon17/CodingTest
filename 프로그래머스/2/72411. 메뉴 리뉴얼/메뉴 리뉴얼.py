from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        menu = []
        for order in orders:
            menu += [''.join(sorted(comb)) for comb in combinations(order, c)]
            
        menu = Counter(menu)
        menu = sorted(menu.items(), key = lambda x:(-x[1]))
        if menu:
            m = menu[0][1]
            answer += [k for k, v in menu if v != 1 and v == m]
    
    answer.sort()

    return answer