import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {

    private List<Point> movePoint(int x, int y, int nx, int ny) {
        List<Point> result = new ArrayList<>();

        int stepX = x <= nx ? 1 : -1;
        for (int cx = x + stepX; cx != nx + stepX; cx += stepX) {
            result.add(new Point(cx, y));
        }

        int lastX = nx;
        int stepY = y <= ny ? 1 : -1;
        for (int cy = y + stepY; cy != ny + stepY; cy += stepY) {
            result.add(new Point(lastX, cy));
        }

        return result;
    }

    private List<Point> getFootprints(int[][] points, int[] viaRoutes) {
        List<Point> result = new ArrayList<>();

        int[] start = points[viaRoutes[0] - 1];
        result.add(new Point(start[0], start[1]));

        for (int i = 1; i < viaRoutes.length; i++) {
            int[] prev = points[viaRoutes[i - 1] - 1];
            int[] next = points[viaRoutes[i] - 1];

            result.addAll(movePoint(prev[0], prev[1], next[0], next[1]));
        }

        return result;
    }

    public int solution(int[][] points, int[][] routes) {
        int answer = 0;
        List<List<Point>> footprints = new ArrayList<>();
        int maxLength = 0;

        for (int[] route : routes) {
            List<Point> path = getFootprints(points, route);
            footprints.add(path);
            maxLength = Math.max(maxLength, path.size());
        }

        for (int t = 0; t < maxLength; t++) {
            Map<Point, Integer> counter = new HashMap<>();

            for (List<Point> path : footprints) {
                if (t < path.size()) {
                    Point p = path.get(t);
                    counter.put(p, counter.getOrDefault(p, 0) + 1);
                }
            }

            for (int count : counter.values()) {
                if (count > 1) {
                    answer++;
                }
            }
        }

        return answer;
    }

    static class Point {
        int x;
        int y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (!(obj instanceof Point)) return false;
            Point other = (Point) obj;
            return x == other.x && y == other.y;
        }

        @Override
        public int hashCode() {
            return 31 * x + y;
        }
    }
}