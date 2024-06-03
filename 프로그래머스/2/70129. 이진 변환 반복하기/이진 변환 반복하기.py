#1. while s!='1'
#2.     0의 제거 + 개수 cnt // 횟수 cnt
#3.     2진 변환 -> bin사용

def solution(s):
    cnt = 0
    cnt_0 = 0
    while s!='1':
        tmp = ''
        for digit in s:
            if digit == '0':
                cnt_0 += 1
            else:
                tmp += digit
                
        s = bin(len(tmp))[2:]
        cnt += 1
        
    return [cnt, cnt_0]