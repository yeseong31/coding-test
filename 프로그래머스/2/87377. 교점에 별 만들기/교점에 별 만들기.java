import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Point {

    private final long x;
    private final long y;

    private Point(final long x, final long y) {
        this.x = x;
        this.y = y;
    }

    public static Point of(final long x, final long y) {
        return new Point(x, y);
    }
    
    public long getX() {
        return x;
    }
    
    public long getY() {
        return y;
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

class Solution {
        
    public String[] solution(int[][] line) {
        
        List<Point> points = new ArrayList<>();
        
        for (int i = 0; i < line.length; i++) {
            for (int j = i + 1; j < line.length; j++) {
                Point intersaction = findIntersaction(line[i][0], line[i][1], line[i][2], line[j][0], line[j][1], line[j][2]);
                
                if (intersaction != null) {
                    points.add(intersaction);
                }
            }
        }
        
        Point minimumPoint = findMinimumPoint(points);
        Point maximumPoint = findMaximumPoint(points);
        
        int width = calculateWidth(minimumPoint, maximumPoint);
        int height = calculateHeight(minimumPoint, maximumPoint);
        
        char[][] board = new char[height][width];
        for (char[] row : board) {
            Arrays.fill(row, '.');
        }
        
        for (Point point : points) {
            int x = (int) (point.getX() - minimumPoint.getX());
            int y = (int) (maximumPoint.getY() - point.getY());
            board[y][x] = '*';
        }
        
        String[] answer = new String[height];
        for (int i = 0; i < height; i++) {
            answer[i] = new String(board[i]);
        }
        
        return answer;
    }
    
    private int calculateWidth(final Point minimumPoint, final Point maximumPoint) {
        return (int) (maximumPoint.getX() - minimumPoint.getX() + 1);
    }
    
    private int calculateHeight(final Point minimumPoint, final Point maximumPoint) {
        return (int) (maximumPoint.getY() - minimumPoint.getY() + 1);
    }
    
    private Point findMinimumPoint(final List<Point> points) {
        long x = Long.MAX_VALUE;
        long y = Long.MAX_VALUE;
        
        for (Point point : points) {
            x = point.getMinimumX(x);
            y = point.getMinimumY(y);
        }
        
        return Point.of(x, y);
    }
    
    private Point findMaximumPoint(final List<Point> points) {
        long x = Long.MIN_VALUE;
        long y = Long.MIN_VALUE;
        
        for (Point point : points) {
            x = point.getMaximumX(x);
            y = point.getMaximumY(y);
        }
        
        return Point.of(x, y);
    }
    
    private Point findIntersaction(long a, long b, long e, long c, long d, long f) {
        if (a * d == b * c) {
            return null;
        }
        
        double x = (double) (b * f - e * d) / (a * d - b * c);
        double y = (double) (e * c - a * f) / (a * d - b * c);
        
        if (x % 1 != 0 || y % 1 != 0) {
            return null;
        }
        
        return Point.of((long) x, (long) y);
    }
}
