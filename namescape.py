'''
Problem Link: https://www.hackerrank.com/contests/programming-jam-9/challenges/namescape
'''
m = int(input('Enter a number: '))
names = {}
for x in range(n):
    name = input().lower().split()
    key = name[-1]
    if key in names:
        names[key] += 1
    else:
        names[key] = 1
unique = 0
rare = 0
total = 0
for name in names:
    total += names[name]
    if names[name] == 1:
        unique += 1
    else:
        rare += 1
diversity = (unique / total) * 100
rarity = (rare / total) * 100

print(int(diversity))
print(int(rarity))