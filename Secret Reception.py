'''
Problem Link: https://www.hackerrank.com/contests/programming-jam-9/challenges/secret-reception 
'''
n = int(input())

relations = {1:[], 2:[]}
for x in range(n):
    a, b = map(int, input().split())
    
    if a in relations:
        relations[a].append(b)
    else:
        relations[a] = []
        relations[a].append(b)
    
    if b in relations:
        relations[b].append(a)
    else:
        relations[b] = []
        relations[b].append(a)

if 2 in relations[1]:
    relations[1].remove(1)

for friend in relations[2]:
    if friend in relations[1]:
        relations[1].remove(friend)

for key in relations:
    if key == 1 or key == 2:
        continue
    if 2 in relations[key]:
        for friend in relations[key]:
            if friend in relations[1]:
                relations[1].remove(friend)

relations[1].sort()
if relations[1]:
    for x in relations[1]:
        print(x, end = ' ')
else:
    print('nobody')