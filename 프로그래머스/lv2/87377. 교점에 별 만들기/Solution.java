import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


class Solution {
    
    private static class Point {
        
        private final long x;
        private final long y;
        
        public Point(long x, long y) {
            this.x = x;
            this.y = y;
        }
        
        public long getMinimumX(long x) {
            return Math.min(this.x, x);
        }
        
        public long getMinimumY(long y) {
            return Math.min(this.y, y);
        }
        
        public long getMaximumX(long x) {
            return Math.max(this.x, x);
        }
        
        public long getMaximumY(long y) {
            return Math.max(this.y, y);
        }
    }
    
    public String[] solution(int[][] line) {
        List<Point> points = new ArrayList<>();
        
        for (int i = 0; i < line.length; i++) {
            for (int j = i + 1; j < line.length; j++) {
                Point intersection = findIntersection(line[i][0], line[i][1], line[i][2], line[j][0], line[j][1], line[j][2]);
                if (intersection != null) {
                    points.add(intersection);
                }
            }
        }
        
        Point minimum = getMinimumPoint(points);
        Point maximum = getMaximumPoint(points);
        
        int width = (int) (maximum.x - minimum.x + 1);
        int height = (int) (maximum.y - minimum.y + 1);
        
        char[][] board = new char[height][width];
        for (char[] row : board) {
            Arrays.fill(row, '.');
        }
        
        for (Point point : points) {
            int x = (int) (point.x - minimum.x);
            int y = (int) (maximum.y - point.y);
            board[y][x] = '*';
        }
        
        String[] answer = new String[height];
        for (int i = 0; i < height; i++) {
            answer[i] = new String(board[i]);
        }
        
        return answer;
    }
    
    private Point getMinimumPoint(List<Point> points) {
        long minimumX = Long.MAX_VALUE;
        long minimumY = Long.MAX_VALUE;
        
        for (Point point : points) {
            minimumX = point.getMinimumX(minimumX);
            minimumY = point.getMinimumY(minimumY);
        }
        
        return new Point(minimumX, minimumY);
    }
    
    private Point getMaximumPoint(List<Point> points) {
        long maximumX = Long.MIN_VALUE;
        long maximumY = Long.MIN_VALUE;
        
        for (Point point : points) {
            maximumX = point.getMaximumX(maximumX);
            maximumY = point.getMaximumY(maximumY);
        }
        
        return new Point(maximumX, maximumY);
    }
    
    private Point findIntersection(long a, long b, long e, long c, long d, long f) {
        if (a * d == b * c) {
            return null;
        }
        
        double x = (double) (b * f - e * d) / (a * d - b * c);
        double y = (double) (e * c - a * f) / (a * d - b * c);
        
        if (x % 1 != 0 || y % 1 != 0) {
            return null;
        }
        
        return new Point((long) x, (long) y);
    }
}