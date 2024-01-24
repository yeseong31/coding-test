class Vertex:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        self.id = (x, y)
        self.connects = set()


def solution(arrows):
    answer = 0
    dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
    
    v = Vertex(0, 0)
    
    vertices = {}
    vertices[v.id] = v
    
    for arrow in arrows:
        for _ in range(2):
            x, y = v.x + dx[arrow], v.y + dy[arrow]
            
            if (x, y) not in vertices:
                vertices[(x, y)] = Vertex(x, y)
            elif (x, y) not in v.connects:
                answer += 1
            
            next_v = vertices[(x, y)]
            
            v.connects.add(next_v.id)
            next_v.connects.add(v.id)
            
            v = next_v
    
    return answer
