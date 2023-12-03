import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;


class Solution {

    private final int[] dx = {-1, 0, 1, 0};
    private final int[] dy = {0, 1, 0, -1};

    static class Point {

        private final int x;
        private final int y;
        private final int step;

        private Point(final int x, final int y, final int step) {
            this.x = x;
            this.y = y;
            this.step = step;
        }

        public static Point of(final int x, final int y) {
            return of(x, y, 0);
        }

        public static Point of(final int x, final int y, final int step) {
            return new Point(x, y, step);
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public int getStep() {
            return step;
        }

        public boolean isEnd(String[] maps, char end) {
            return maps[x].charAt(y) == end;
        }
    }

    public int solution(String[] maps) {
        Map<Character, Point> points = new HashMap<>();

        for (int i = 0; i < maps.length; i++) {
            for (int j = 0; j < maps[0].length(); j++) {
                if (isPhase(maps[i].charAt(j))) {
                    points.put(maps[i].charAt(j), Point.of(i, j));
                }
            }
        }

        int startToLever = bfs('S', 'L', maps, points);
        int LeverToEnd = bfs('L', 'E', maps, points);

        if (startToLever > 0 && LeverToEnd > 0) {
            return startToLever + LeverToEnd;
        }
        return -1;
    }

    private int bfs(char start, char end, String[] maps, Map<Character, Point> points) {
        Point point = points.get(start);

        Queue<Point> q = new LinkedList<>();
        q.add(point);

        boolean[][] visited = new boolean[maps.length][maps[0].length()];
        visited[point.getX()][point.getY()] = true;

        while (!q.isEmpty()) {
            Point poll = q.poll();

            if (poll.isEnd(maps, end)) {
                return poll.getStep();
            }

            for (int i = 0; i < 4; i++) {
                int nx = poll.getX() + dx[i];
                int ny = poll.getY() + dy[i];

                if (isOutOfRange(maps, nx, ny) || visited[nx][ny] || maps[nx].charAt(ny) == 'X') {
                    continue;
                }
                visited[nx][ny] = true;
                q.add(Point.of(nx, ny, poll.getStep() + 1));
            }
        }

        return 0;
    }

    private boolean isOutOfRange(String[] maps, int x, int y) {
        return x < 0 || x >= maps.length || y < 0 || y >= maps[0].length();
    }

    private boolean isPhase(char c) {
        return c == 'S' || c == 'E' || c == 'L';
    }
}