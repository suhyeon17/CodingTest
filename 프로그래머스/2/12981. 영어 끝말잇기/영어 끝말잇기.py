def solution(n, words):
    word_dict = {}
    word_dict[words[0]] = 1
    
    for i in range(1, len(words)):
        first = words[i][0]
        last = words[i-1][-1]
        
        if first == last and words[i] not in word_dict:
            word_dict[words[i]] = 1
        else:
            return [(i%n)+1, (i//n)+1]
    
    return [0, 0]