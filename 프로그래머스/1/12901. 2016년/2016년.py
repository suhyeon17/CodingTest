def solution(a, b):
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'] 
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    date = sum(month[:a-1]) + b
    
    return days[date%7]