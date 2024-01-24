import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Vertex {
    
    public final int x;
    public final int y;
    public final String id; 
    public final Set<String> connects = new HashSet<>();
    
    public Vertex(int x, int y) {
        this.x = x;
        this.y = y;
        this.id = generateId(x, y);
    }
    
    public static String generateId(int x, int y) {
        return String.format("ID-%d-%d", x, y);
    }
}

class Solution {
    
    private static final int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    private static final int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};
    
    public int solution(int[] arrows) {
        Map<String, Vertex> vertices = new HashMap<>();
        
        Vertex v = new Vertex(0, 0);
        vertices.put(v.id, v);
        
        return findRooms(arrows, v, vertices);
    }
    
    private int findRooms(int[] arrows, Vertex v, Map<String, Vertex> vertices) {
        int result = 0;
        
        for (int arrow : arrows) {
            for (int i = 0; i < 2; i++) {
                int x = v.x + dx[arrow];
                int y = v.y + dy[arrow];

                String id = Vertex.generateId(x, y);

                if (!vertices.containsKey(id)) {
                    vertices.put(id, new Vertex(x, y));
                } else if (!v.connects.contains(id)) {
                    result++;
                }

                Vertex nv = vertices.get(id);
                v.connects.add(nv.id);
                nv.connects.add(v.id);

                v = nv;
            }
        }
        
        return result;
    }
}