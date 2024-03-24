from heapq import *


def find_parent(x, parent):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(x, y, parent):
    if parent[x] > parent[y]:
        parent[x] = y
    else:
        if parent[x] == parent[y]:
            parent[x] -= 1
        parent[y] = x


def solution(n, costs):
    answer = 0
    
    parent = [-1] * n
    costs.sort(key=lambda x: x[2])
    
    for cost in costs:
        a, b, w = cost
        x = find_parent(a, parent)
        y = find_parent(b, parent)
        if x != y:
            union_parent(x, y, parent)
            answer += w
    
    
        
    
    return answer