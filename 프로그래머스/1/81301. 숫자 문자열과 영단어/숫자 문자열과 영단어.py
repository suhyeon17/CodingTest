def solution(s):
    answer = []
    word = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    check = ''
    
    for i in s:
        if i.isdigit():
            answer.append(i)
        else:
            check += i
            if check in word:
                answer.append(word[check])
                check = ''

    return int(''.join(answer))
