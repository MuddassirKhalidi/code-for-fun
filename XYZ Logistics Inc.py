'''
Problem Link: https://www.hackerrank.com/contests/programming-jam-9/challenges/xyz-logistics-inc
'''

import heapq

def shortest_path(graph, source, destination, T):
    distance = {node: float('inf') for node in graph}
    distance[source] = 0
    pq = [(0, source)]  # priority queue (distance, node)
    
    while pq:
        dist, node = heapq.heappop(pq)
        if node == destination:
            return dist
        for neighbor, (c, p) in graph[node].items():
            if c > T:
                new_dist = dist + p
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
    
    return -1

def build_adjacency_list(N, edges):
    adjacency_list = {i: {} for i in range(1, N + 1)}
    for edge in edges:
        u, v, c, p = edge
        adjacency_list[u][v] = (c, p)
        
    return adjacency_list

N, M, S, D, T = map(int, input().split())
edges = []
for m in range(M):
    edge = tuple(map(int, input().split()))
    edges.append(edge)

adj_list = build_adjacency_list(N, edges)
print(shortest_path(adj_list, S, D, T))