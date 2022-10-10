n = int(input())
arr = list(map(int, input().split()))

stop = True
for i in range(n - 1, 0, -1):
    if arr[i] > arr[i - 1]:
        stop = False
        break
for j in range(n - 1, 0, -1):
    if arr[i-1] < arr[j]:
        arr[i-1], arr[j] = arr[j], arr[i-1] # swap
        break
   
if stop:
    print(-1)    
else:
    arr = arr[:i] + sorted(arr[i:])
    print(*arr) #요소만 출력하고 싶으면 이렇게!!
