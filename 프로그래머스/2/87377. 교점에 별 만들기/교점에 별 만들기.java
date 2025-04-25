import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Point {
    private final long x;
    private final long y;
    
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Solution {
    private class Point {
        private final long x;
        private final long y;

        private Point(long x, long y) {
            this.x = x;
            this.y = y;
        }
        
        public long getX() {
            return x;
        }
        
        public long getY() {
            return y;
        }
    }
    
    private Point getIntersection(long a, long b, long e, long c, long d, long f) {
        if ((a * d) == (b * c)) {
            return null;
        }
        
        double x = (double) ((b * f) - (e * d)) / ((a * d) - (b * c));
        double y = (double) ((e * c) - (a * f)) / ((a * d) - (b * c));
        
        if (x % 1 != 0 || y % 1 != 0) {
            return null;
        }
        
        return new Point((long) x, (long) y);
    }
    
    private Point getMinPoint(List<Point> points) {
        long minX = Long.MAX_VALUE;
        long minY = Long.MAX_VALUE;
        
        for (Point point : points) {
            long px = point.getX();
            long py = point.getY();
            
            if (px < minX) {
                minX = px;
            }
            if (py < minY) {
                minY = py;
            }
        }
        
        return new Point(minX, minY);
    }
    
    private Point getMaxPoint(List<Point> points) {
        long maxX = Long.MIN_VALUE;
        long maxY = Long.MIN_VALUE;
        
        for (Point point : points) {
            long px = point.getX();
            long py = point.getY();
            
            if (maxX < px) {
                maxX = px;
            }
            if (maxY < py) {
                maxY = py;
            }
        }
        
        return new Point(maxX, maxY);
    }
    
    public String[] solution(int[][] line) {
        List<Point> points = new ArrayList<>();
        
        for (int i = 0; i < line.length; i++) {
            for (int j = i + 1; j < line.length; j++) {
                Point point = getIntersection(line[i][0], line[i][1], line[i][2], line[j][0], line[j][1], line[j][2]);
                if (point != null) {
                    points.add(point);
                }
            }
        }
        
        Point minPoint = getMinPoint(points);
        Point maxPoint = getMaxPoint(points);
        
        int width = (int) (maxPoint.getX() - minPoint.getX() + 1);
        int height = (int) (maxPoint.getY() - minPoint.getY() + 1);
        
        char[][] board = new char[height][width];
        for (char[] row : board) {
            Arrays.fill(row, '.');
        }
        
        for (Point point : points) {
            int x = (int) (point.getX() - minPoint.getX());
            int y = (int) (maxPoint.getY() - point.getY());
            board[y][x] = '*';
        }
        
        String[] answer = new String[board.length];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = new String(board[i]);
        }
        return answer;
    }
}