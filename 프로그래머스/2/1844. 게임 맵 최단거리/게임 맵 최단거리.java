import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Point {
    
    private final int x;
    private final int y;
    private final int distance;
    
    public Point(int x, int y, int distance) {
        this.x = x;
        this.y = y;
        this.distance = distance;
    }
    
    public int getX() {
        return x;
    }
    
    public int getY() {
        return y;
    }
    
    public int getDistance() {
        return distance;
    }
}

class Solution {
    
    private static final int[] dx = {-1, 0, 1, 0};
    private static final int[] dy = {0, 1, 0, -1};
    
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        Queue<Point> queue = new LinkedList<>();
        queue.add(new Point(0, 0, 1));
        
        boolean[][] visited = new boolean[n][m];
        for (boolean[] row : visited) {
            Arrays.fill(row, false);
        }
        
        while (!queue.isEmpty()) {
            Point point = queue.poll();
            
            int x = point.getX();
            int y = point.getY();
            int distance = point.getDistance();
            
            if (x == n - 1 && y == m - 1) {
               return distance;
            }
            
            for (int index = 0; index < 4; index++) {
                int nx = x + dx[index];
                int ny = y + dy[index];
                
                if (nx < 0 || nx >= n || ny < 0 || ny >= m || maps[nx][ny] == 0 || visited[nx][ny]) {
                    continue;
                }
                
                visited[nx][ny] = true;
                queue.add(new Point(nx, ny, distance + 1));
            }
        }
        
        return -1;
    }
}