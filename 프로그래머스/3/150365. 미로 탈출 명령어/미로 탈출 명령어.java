import java.util.*;

class Solution {
    
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        int[] dx = {1, 0, 0, -1};
        int[] dy = {0, -1, 1, 0};
        char[] dz = {'d', 'l', 'r', 'u'};
        
        Queue<State> q = new ArrayDeque<>();
        q.offer(new State(x, y, ""));
        
        while (!q.isEmpty()) {
            State cur = q.poll();
            
            if (cur.x == r && cur.y == c) {
                if (k % 2 != cur.path.length() % 2) break;
                if (cur.path.length() == k) return cur.path;
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                
                if (0 < nx && nx <= n && 0 < ny && ny <= m &&
                    cur.path.length() + Math.abs(nx - r) + Math.abs(ny - c) < k) {
                    q.offer(new State(nx, ny, cur.path + dz[i]));
                    break;
                }
            }
        }
        
        return "impossible";
    }
    
    static class State {
        int x, y;
        String path;
        
        State(int x, int y, String path) {
            this.x = x;
            this.y = y;
            this.path = path;
        }
    }
}