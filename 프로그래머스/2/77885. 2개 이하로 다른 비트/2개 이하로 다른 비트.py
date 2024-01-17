def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
        else:
            n = '0' + bin(num)[2:]
            n = list(n)
            idx = -1
            for i in n[::-1]:
                if i == '0':
                    break   
                idx -= 1
                
            n[idx] = '1'
            n[idx+1] = '0'
            answer.append(int(''.join(n), 2))
            
    return answer
                    