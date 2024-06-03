#이중반복문까지는 안됨.
#0, 1, 10, 11, 100, 101, 
#1. bin(n) -> 1개수 세기
#2. while True:
#3.     num = n+1
#4.     bin(num) -> 1개수 세기
#5.     개수가 같으면 break
def solution(n):
    now = bin(n).count('1')
    num = n
    
    while True:
        num += 1
        if bin(num).count('1') == now:
            break
            
    return num