def hansu(n):
	digit1 = int(str(n)[0])
	digit2 = int(str(n)[1])
	digit3 = int(str(n)[2])

	if (digit1-digit2) == (digit2 - digit3):
		return 1
	else:
		return 0


n = int(input())
cnt  = 99

if n > 99:
	for i in range(100, n + 1):
		 cnt += hansu(i)
else:
	cnt = n		

print(cnt)
	