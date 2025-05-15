class Vertex:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        self.id = self.get_id(x, y)
        self.connected = set()
        
    @staticmethod
    def get_id(x, y):
        return f'{x}_{y}'


def solution(arrows):
    dx, dy = (0, 1, 1, 1, 0, -1, -1, -1), (1, 1, 0, -1, -1, -1, 0, 1)
    
    x, y, count = 0, 0, 0
    v = Vertex(x, y)
    
    vertices = dict()
    vertices[v.id] = v
    
    for arrow in arrows:
        for _ in range(2):
            nx, ny = x + dx[arrow], y + dy[arrow]
            _id = Vertex.get_id(nx, ny)
            
            if _id not in vertices:
                vertices[_id] = Vertex(nx, ny)
            elif _id not in v.connected:
                count += 1
            
            nv = vertices[_id]
            v.connected.add(nv.id)
            nv.connected.add(v.id)
            
            x, y = nx, ny
            v = vertices[_id]
    
    return count