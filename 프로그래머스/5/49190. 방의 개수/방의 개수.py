class Vertex:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        self.id = self.generate_id(x, y)
        self.connects = set()
        
    @staticmethod
    def generate_id(x, y):
        return f'{x}-{y}'


def solution(arrows):
    answer = 0
    dx, dy = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
    
    v = Vertex(0, 0)
    
    vertices = {}
    vertices[v.id] = v
    
    for arrow in arrows:
        for _ in range(2):
            x, y = v.x + dx[arrow], v.y + dy[arrow]
            id = Vertex.generate_id(x, y)
            
            if id not in vertices:
                vertices[id] = Vertex(x, y)
            elif id not in v.connects:
                answer += 1
            
            next_v = vertices[id]
            
            v.connects.add(next_v.id)
            next_v.connects.add(v.id)
            
            v = next_v
    
    return answer
