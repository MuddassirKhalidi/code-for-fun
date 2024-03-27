'''
Problem Link: https://www.hackerrank.com/contests/programming-jam-9/challenges/server-blues
'''
levels, offices, servers = map(int, input().split())
on = [int(input()) for x in range(levels)]

on.sort()
for i in range(servers):
    on[i] = offices - on[i]

sum = 0
for i in on:
    sum += i

print(sum)