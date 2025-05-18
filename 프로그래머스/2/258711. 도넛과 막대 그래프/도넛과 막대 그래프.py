def solution(edges):
    n = 0
    for a, b in edges:
        n = max(n, a, b)
    
    graph = [[] for _ in range(n + 1)]
    edge_info = [[0, 0] for _ in range(n + 1)]
    for a, b in edges:
        graph[a].append(b)
        edge_info[b][0] += 1
        edge_info[a][1] += 1
        
    root = -1
    for x, (in_edge, out_edge) in enumerate(edge_info):
        if in_edge == 0 and out_edge >= 2:
            root = x
            break
    
    donut, stick, eight = 0, 0, 0
    for node in graph[root]:
        visited = set()
        x = node
        is_donut = True
        
        while x not in visited:
            visited.add(x)
            in_edge, out_edge = edge_info[x]
            
            if out_edge == 0:
                stick += 1
                is_donut = False
                break
            
            if out_edge == 2:
                eight += 1
                is_donut = False
                break
            
            x = graph[x][0]
        
        if is_donut:
            donut += 1
            
    return root, donut, stick, eight