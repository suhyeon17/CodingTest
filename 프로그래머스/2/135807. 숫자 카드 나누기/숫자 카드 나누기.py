def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
        
    return a

def solution(arrayA, arrayB):
    arrayA = list(set(arrayA))
    arrayB = list(set(arrayB))
    
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    
    for i in range(1, len(arrayA)):
        gcdA = gcd(gcdA, arrayA[i])
    for i in range(1, len(arrayB)):
        gcdB = gcd(gcdB, arrayB[i])
    
    if (gcdA == 1 and gcdB == 1) or (gcdA==gcdB):
        return 0
    
    if gcdA > gcdB:
        for num in arrayB:
            if num % gcdA == 0:
                return 0
            
    if gcdA < gcdB:
        for num in arrayA:
            if num % gcdB == 0:
                return 0
    
    return max(gcdA, gcdB)
    
    
    