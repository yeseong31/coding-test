import java.util.*;

class Solution {

    public final int[] dx = {-1, 0, 1, 0};
    public final int[] dy = {0, 1, 0, -1};

    public static class Point {
        public int x, y, step;

        public Point(int x, int y, int step) {
            this.x = x;
            this.y = y;
            this.step = step;
        }
    }

    public int solution(String[] maps) {
        Map<Character, Point> points = new HashMap<>();

        for (int i = 0; i < maps.length; i++) {
            for (int j = 0; j < maps[0].length(); j++) {
                char c = maps[i].charAt(j);
                if (c == 'S' || c == 'E' || c == 'L') {
                    points.put(c, new Point(i, j, 0));
                }
            }
        }

        int startToLever = bfs('S', 'L', maps, points);
        int leverToEnd = bfs('L', 'E', maps, points);

        return (startToLever > 0 && leverToEnd > 0) ? startToLever + leverToEnd : -1;
    }

    public int bfs(char start, char end, String[] maps, Map<Character, Point> points) {
        Point p = points.get(start);
        Queue<Point> q = new LinkedList<>();
        q.add(p);

        boolean[][] visited = new boolean[maps.length][maps[0].length()];
        visited[p.x][p.y] = true;

        while (!q.isEmpty()) {
            Point cur = q.poll();
            if (maps[cur.x].charAt(cur.y) == end) {
                return cur.step;
            }

            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                if (nx < 0 || ny < 0 || nx >= maps.length || ny >= maps[0].length()) {
                    continue;
                }
                if (visited[nx][ny] || maps[nx].charAt(ny) == 'X') {
                    continue;
                }

                visited[nx][ny] = true;
                q.add(new Point(nx, ny, cur.step + 1));
            }
        }
        
        return 0;
    }
}