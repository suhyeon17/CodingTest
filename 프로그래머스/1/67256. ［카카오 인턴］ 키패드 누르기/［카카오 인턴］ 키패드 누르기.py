def solution(numbers, hand):
    answer = ''
    L, R = (3, 0), (3, 2)
    keypad = {1:(0, 0), 2:(0, 1), 3:(0, 2), 
              4:(1, 0), 5:(1, 1), 6:(1, 2), 
              7:(2, 0), 8:(2, 1), 9:(2, 2), 0:(3, 1)}
    
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += 'L'
            L = keypad[n]
        elif n == 3 or n == 6 or n == 9:
            answer += 'R'
            R = keypad[n]
        else:
            R_len = abs(R[0] - keypad[n][0]) + abs(R[1] - keypad[n][1])
            L_len = abs(L[0] - keypad[n][0]) + abs(L[1] - keypad[n][1])
            
            if R_len < L_len:
                answer += 'R'
                R = keypad[n]
            elif R_len > L_len:
                answer += 'L'
                L = keypad[n]
            else:
                if hand == 'left':
                    answer += 'L'
                    L = keypad[n]
                else:
                    answer += 'R'
                    R = keypad[n]
                
                
    return answer