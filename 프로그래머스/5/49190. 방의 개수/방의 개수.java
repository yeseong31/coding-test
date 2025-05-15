import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Vertex {
    private int x;
    private int y;
    private String id;
    private Set<String> connected = new HashSet<>();
    
    public static String generateId(int x, int y) {
        return String.format("%d_%d", x, y);
    }
    
    public Vertex(int x, int y) {
        this.x = x;
        this.y = y;
        this.id = generateId(x, y);
    }
    
    public int getX() {
        return x;
    }
    
    public int getY() {
        return y;
    }
    
    public String getId() {
        return id;
    }
    
    public boolean isConnected(String otherId) {
        return connected.contains(otherId);
    }
    
    public void connect(String otherId) {
        connected.add(otherId);
    }
}

class Solution {
    private final int[] dx = new int[] {0, 1, 1, 1, 0, -1, -1, -1};
    private final int[] dy = new int[] {1, 1, 0, -1, -1, -1, 0, 1};
    
    public int solution(int[] arrows) {
        int answer = 0;
        int x = 0;
        int y = 0;
        
        Map<String, Vertex> vertices = new HashMap<>();
        
        Vertex v = new Vertex(x, y);
        vertices.put(Vertex.generateId(x, y), v);
        
        for (int d : arrows) {
            for (int i = 0; i < 2; i++) {
                int nx = x + dx[d];
                int ny = y + dy[d];
                String id = Vertex.generateId(nx, ny);
                
                Vertex nv;
                if (!vertices.containsKey(id)) {
                    nv = new Vertex(nx, ny);
                    vertices.put(id, nv);
                } else {
                    nv = vertices.get(id);
                    if (!v.isConnected(id)) {
                        answer++;
                    }
                }
                
                v.connect(nv.getId());
                nv.connect(v.getId());
                
                x = nx;
                y = ny;
                v = nv;
            }
        }
        
        return answer;
    }
}