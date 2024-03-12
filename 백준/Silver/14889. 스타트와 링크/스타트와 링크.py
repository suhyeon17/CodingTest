from itertools import combinations

n = int(input())
skills = [list(map(int, input().split())) for _ in range(n)]

min = 100
teams = combinations(range(0, n), n//2)
for team in teams:
    start = list(team)
    link = [i for i in range(0, n) if i not in start]

    start_skill = 0
    link_skill = 0

    for i in range((n//2)-1):
        for j in range(i+1, n//2):
            start_skill += skills[start[i]][start[j]] + skills[start[j]][start[i]]
            link_skill += skills[link[i]][link[j]] + skills[link[j]][link[i]]
    
    diff =  abs(start_skill - link_skill)
    if min > diff:
        min = diff
    
print(min)
 
            