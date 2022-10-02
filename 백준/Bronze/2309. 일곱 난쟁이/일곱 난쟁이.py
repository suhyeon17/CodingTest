h = [int(input()) for _ in range(9)]
 
# sum(h) - (h[i] + h[j]) == 100 되는 걸 찾자!!
sum_h = sum(h)
del1,  del2= 0, 0

for i in range(len(h)):
    for j in range(i+1, len(h)):
        if sum_h - (h[i] + h[j]) == 100:
            del1 = h[i]
            del2 = h[j]

h.remove(del1)
h.remove(del2)
h.sort()

print(*h, sep = '\n')