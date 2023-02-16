#셀프넘버 출력문제
def digit(n): #자릿수 합을 구하는 함수
	num = 0	
	while n > 0:
		num += (n % 10)
		n //= 10
	
	return num

def d(n): # 생성자 구하는 함수
    return n + digit(n)

lst = [i for i in range(10001)]
nonselfnum = []
for i in lst:
    nonselfnum.append(d(i))

selfnum = sorted(set(lst) - set(nonselfnum))

print(*selfnum, sep = '\n')