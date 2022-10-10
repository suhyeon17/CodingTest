import itertools

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    if k == 0:
        break
    del arr[0]
    for i in list(itertools.combinations(arr, 6)):
        print(*i)
    print()