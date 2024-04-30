board = input()
board = board.split('.')
answer = ''

for b in board:
    l = len(b)
    if l == 0:
        answer += '.'
    else:
        if l % 4 == 0:
            answer += 'AAAA' * (l//4)
        elif l % 4 == 2:
            answer += ('AAAA' * (l//4) + 'BB')
        elif l % 2 == 0:
            answer += 'BB' * (l//2)
        else:
            answer = '-1.'
            break
        answer += '.'

print(answer[:-1])