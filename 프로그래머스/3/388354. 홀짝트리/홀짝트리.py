import sys

from collections import defaultdict

sys.setrecursionlimit(10**5)


def is_oe_tree(node, parent, visited, graph):
    children = graph[node]
    count = len(children)
    
    if parent != -1:
        count -= 1
    
    if node % 2 != count % 2:
        return False
    
    visited[node] = True
    
    for child in children:
        if child == parent:
            continue
        if not is_oe_tree(child, node, visited, graph):
            visited[node] = False
            return False
    
    return True


def is_roe_tree(node, parent, visited, graph):
    children = graph[node]
    count = len(children)
    
    if parent != -1:
        count -= 1
    
    if node % 2 == count % 2:
        return False
        
    visited[node] = True
    
    for child in children:
        if child == parent:
            continue
        if not is_roe_tree(child, node, visited, graph):
            visited[node] = False
            return False

    return True


def solution(nodes, edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * 1_000_001
    oe = sum(not visited[n] and is_oe_tree(n, -1, visited, graph) for n in nodes)
    
    visited = [False] * 1_000_001
    roe = sum(not visited[n] and is_roe_tree(n, -1, visited, graph) for n in nodes)
    
    return oe, roe