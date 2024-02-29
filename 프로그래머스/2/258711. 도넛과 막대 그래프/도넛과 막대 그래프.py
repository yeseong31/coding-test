from collections import defaultdict


def solution(edges):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        
    n = len(graph)
    
    root = sorted(graph, key=lambda x: len(graph[x]), reverse=True)[0]
    donut = stick = eight = 0

    visited = set()
    visited.add(root)
    
    for node in graph[root]:
        if len(graph[node]) == 2:
            visited.add(node)
            eight += 1
            continue
        
        if graph[node] and node == graph[node]:
            visited.add(node)
            donut += 1
            continue
            
        count_node = count_edge = 0
        checked = False
        
        while node not in visited:
            count_node += 1
            visited.add(node)
            
            if len(graph[node]) == 2:
                eight += 1
                checked = True
                break
            
            if not graph[node]:
                stick += 1
                checked = True
                break
            
            count_edge += 1
            node = graph[node][0]
        
        if checked:
            continue
        if not graph[node]:
            stick += 1
        elif count_node == count_edge:
            donut += 1
        else:
            eight += 1
    
    return root, donut, stick, eight
