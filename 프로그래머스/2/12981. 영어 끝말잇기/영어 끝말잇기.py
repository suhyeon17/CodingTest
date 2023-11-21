import math

def solution(n, words):
    word_dict, idx = {}, 0
    
    for word in words:
        first = word[0]
        idx += 1
        if idx == 1:
            last = word[-1]
            word_dict[word] = 1
            continue
        if last != first:
            a = idx%n
            b = math.ceil(idx/n)
            if idx%n == 0:
                a = n
            return [a, b]
        elif word in word_dict:
            a = idx%n
            b = math.ceil(idx/n)
            if idx%n == 0:
                a = n
            return [a, b]
        
        word_dict[word] = 1
        last = word[-1]

    return [0,0]