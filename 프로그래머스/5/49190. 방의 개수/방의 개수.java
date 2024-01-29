import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Vertex {
    
    private final int x;
    private final int y;
    private final String id; 
    private final Set<String> connects = new HashSet<>();
    
    private Vertex(int x, int y) {
        this.x = x;
        this.y = y;
        this.id = generateId(x, y);
    }
    
    public static Vertex of(int x, int y) {
        return new Vertex(x, y);
    }
    
    public static String generateId(int x, int y) {
        return String.format("(%d, %d)", x, y);
    }
    
    public String getId() {
        return id;
    }
    
    public int getNextX(int dx) {
        return x + dx;
    }
    
    public int getNextY(int dy) {
        return y + dy;
    }
    
    public boolean isConnected(String id) {
        return connects.contains(id);
    }
    
    public void connect(String id) {
        connects.add(id);
    }
}

class Solution {
    
    private static final int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    private static final int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};
    
    public int solution(int[] arrows) {
        Map<String, Vertex> vertices = new HashMap<>();
        
        Vertex v = Vertex.of(0, 0);
        vertices.put(v.getId(), v);
        
        return findRooms(arrows, v, vertices);
    }
    
    private int findRooms(int[] arrows, Vertex v, Map<String, Vertex> vertices) {
        int result = 0;
        
        for (int arrow : arrows) {
            for (int i = 0; i < 2; i++) {
                int x = v.getNextX(dx[arrow]);
                int y = v.getNextY(dy[arrow]);

                String id = Vertex.generateId(x, y);

                if (!vertices.containsKey(id)) {
                    vertices.put(id, Vertex.of(x, y));
                } else if (!v.isConnected(id)) {
                    result++;
                }

                Vertex nv = vertices.get(id);
                v.connect(nv.getId());
                nv.connect(v.getId());

                v = nv;
            }
        }
        
        return result;
    }
}