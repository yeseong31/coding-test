import java.util.HashSet;
import java.util.LinkedList;
import java.util.Objects;
import java.util.Queue;
import java.util.Set;

class Point {
    public int x;
    public int y;
    public int seq;
    
    public Point(int x, int y, int seq) {
        this.x = x;
        this.y = y;
        this.seq = seq;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }
        
        Point other = (Point) obj;
        return this.x == other.x && this.y == other.y;
    }
}

class Solution {
    private final int[] dx = {1, 0, -1, 0};
    private final int[] dy = {0, 1, 0, -1};
    
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        Point start = new Point(0, 0, 1);
        Point goal = new Point(n - 1, m - 1, 0);
        
        Set<Point> visited = new HashSet<>();
        Queue<Point> queue = new LinkedList<>();
        
        queue.offer(start);
        visited.add(start);
        
        while (!queue.isEmpty()) {
            Point point = queue.poll();
            if (point.x == goal.x && point.y == goal.y) {
                return point.seq;
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = point.x + dx[i];
                int ny = point.y + dy[i];
                
                if (nx < 0 || nx >= n || ny < 0 || ny >= m || maps[nx][ny] == 0) {
                    continue;
                }

                Point next = new Point(nx, ny, point.seq + 1);
                if (!visited.contains(next)) {
                    visited.add(next);
                    queue.offer(next);
                }
            }
        }
        
        return -1;
    }
}