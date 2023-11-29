def solution(phone_number):
    n = len(phone_number)
    s = '*' * (n-4)
    s += phone_number[-4:]
    
    return s