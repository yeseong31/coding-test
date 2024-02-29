from collections import defaultdict


def solution(edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
    
    root = sorted(graph, key=lambda x: len(graph[x]), reverse=True)[0]
    visited = set()
    visited.add(root)
    
    donut = stick = eight = 0
    
    for node in graph[root]:
        if len(graph[node]) == 2:
            eight += 1
            continue
        
        if graph[node] and node == graph[node]:
            donut += 1
            continue
            
        count_node = count_edge = 0
        checked = False
        
        while not checked and node not in visited:
            count_node += 1
            visited.add(node)
            
            if len(graph[node]) == 1:
                count_edge += 1
                node = graph[node].pop()
                continue
            
            checked = True
            if len(graph[node]) == 2:
                eight += 1
            if not graph[node]:
                stick += 1
        
        if checked:
            continue
        
        if count_node == count_edge:
            donut += 1
        else:
            eight += 1
    
    return root, donut, stick, eight
