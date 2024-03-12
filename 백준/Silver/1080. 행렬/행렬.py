import sys

def change(matrix, row, col):
    for i in range(3):
        for j in range(3):
            if matrix[row+i][col+j] == '1':
                matrix[row+i][col+j] = '0'
            else:
                matrix[row+i][col+j] = '1'



N, M = map(int, sys.stdin.readline().split())
A, B = [], []
for _ in range(N):
    A.append(list(sys.stdin.readline().rstrip('\n')))
for _ in range(N):
    B.append(list(sys.stdin.readline().rstrip('\n')))

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            change(A, i, j)
            cnt += 1
if A != B:
    print(-1)
else: print(cnt)