import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Point {
    
    public final int x;
    public final int y;
    public final String id;
    public final Set<String> connected;
    
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
        this.id = createId(x, y);
        this.connected = new HashSet<>();
    }
    
    public static String createId(int x, int y) {
        return String.format("%d_%d", x, y);
    }
}

class Solution {
    
    private static final int[] dx = {0, 1, 1, 1, 0, -1, -1, -1};
    private static final int[] dy = {1, 1, 0, -1, -1, -1, 0, 1};
    
    public int solution(int[] arrows) {
        int answer = 0;
        Map<String, Point> points = new HashMap<>();
        
        Point v = new Point(0, 0);
        points.put(v.id, v);
        
        for (int d : arrows) {
            for (int i = 0; i < 2; i++) {
                int x = v.x + dx[d];
                int y = v.y + dy[d];

                String id = Point.createId(x, y);
                
                if (!points.containsKey(id)) {
                    points.put(id, new Point(x, y));
                } else if (!v.connected.contains(id)) {
                    answer++;
                }

                Point u = points.get(id);
                v.connected.add(u.id);
                u.connected.add(v.id);
                v = points.get(id);
            }
        }
        
        return answer;
    }
}