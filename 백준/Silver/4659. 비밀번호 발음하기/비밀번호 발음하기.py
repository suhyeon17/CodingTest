import sys
from itertools import product

def rule(s, vowel, vowel_comb, cons_comb):
    #1번조건
    if not any(v in s for v in vowel):
        return False
    #2번 조건
    if len(s) >= 3:
        for i in range(len(s)-2):
            if s[i:i+3] in vowel_comb or s[i:i+3] in cons_comb:
                return False
    if len(s) >= 2:
        for i in range(len(s)-1):
            if s[i:i+2] != 'ee' and s[i:i+2] != 'oo':
                if s[i] == s[i+1]:
                    return False

    return True
            

alpha = [chr(a) for a in range(97,123)]
vowel = ['a', 'e', 'i', 'o', 'u']
cons = [a for a in alpha if a not in vowel]
vowel_comb = [''.join(comb) for comb in product(vowel, repeat = 3)]
cons_comb = [''.join(comb) for comb in product(cons, repeat = 3)]

while True:
    s = sys.stdin.readline().rstrip()
    if s == 'end':
        break
    
    if rule(s, vowel, vowel_comb, cons_comb):
        print('<%s> is acceptable.' %s)
    else:
        print('<%s> is not acceptable.' %s)