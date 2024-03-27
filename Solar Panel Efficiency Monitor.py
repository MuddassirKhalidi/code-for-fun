'''
Problem Link: https://www.hackerrank.com/contests/programming-jam-9/challenges/solar-panel-efficiency-monitor
'''
def getAvg(i, j, d):
    summ = 0
    count = 0
    for k in range(i, j + 1):
        summ += d[k]
        count += 1
        
    return summ / count

def getMax(i, j, d):
    lst = [d[x] for x in range(i, j + 1)]
    return max(lst)


no_panels, operations = map(int, input().split())
ratings = list(map(float, input().split()))
panels = {x + 1:rating for x,rating in enumerate(ratings)}
results = []

for q in range(operations):
    op, q1, q2 = input().split()
    
    if op == '1':
        q1, q2 = int(q1), float(q2)
        panels[q1] = q2
    
    if op == '2':
        q1, q2 = int(q1), int(q2)
        results.append(getMax(q1, q2, panels))
    
    if op == '3':
        q1, q2 = int(q1), int(q2)
        results.append(getAvg(q1, q2, panels))

for result in results:
    print(result)