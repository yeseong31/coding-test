import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Objects;

class Solution {
    
    public int[][] solution(int n, int[][] build_frame) {
        
        List<Point> points = new ArrayList<>();
        
        for (int[] row : build_frame) {
            int x = row[0];  // 가로 좌표
            int y = row[1];  // 세로 좌표
            int a = row[2];  // 0은 기둥, 1은 보
            int b = row[3];  // 0은 삭제, 1은 설치
            
            Point p = new Point(x, y, a);
            
            if (b == 1) {
                points.add(p);
                if (!isValid(points)) points.remove(p);
            } else {
                points.remove(p);
                if (!isValid(points)) points.add(p);
            }
        }
        
        Collections.sort(points);
        
        int[][] answer = new int[points.size()][3];
        
        for (int i = 0; i < points.size(); i++) {
            Point p = points.get(i);
            answer[i][0] = p.x;
            answer[i][1] = p.y;
            answer[i][2] = p.a;
        }
        
        return answer;
    }
    
    private static boolean isValid(List<Point> points) {
        for (Point p : points) {
            int x = p.x;
            int y = p.y;
            int a = p.a;
            
            if (a == 0) {
                if (y == 0) continue;
                if (points.contains(new Point(x, y, 1)) || points.contains(new Point(x - 1, y, 1))) continue;
                if (points.contains(new Point(x, y - 1, 0))) continue;
                return false;
            } else {
                if (points.contains(new Point(x, y - 1, 0)) || points.contains(new Point(x + 1, y - 1, 0))) continue;
                if (points.contains(new Point(x - 1, y, 1)) && points.contains(new Point(x + 1, y, 1))) continue;
                return false;
            }
        }
        
        return true;
    }
    
    private static class Point implements Comparable<Point> {
        final int x;
        final int y;
        final int a;

        Point(int x, int y, int a) {
            this.x = x;
            this.y = y;
            this.a = a;
        }

        @Override
        public int compareTo(Point o) {
            if (this.x != o.x) {
                return Integer.compare(this.x, o.x);
            }
            if (this.y != o.y) {
                return Integer.compare(this.y, o.y);
            }
            return Integer.compare(this.a, o.a);
        }
        
        @Override
        public boolean equals(Object o) {
            if (!(o instanceof Point)) return false;
            Point p = (Point) o;
            return this.x == p.x && this.y == p.y && this.a == p.a;
        }
        
        @Override
        public int hashCode() {
            return Objects.hash(x, y, a);
        }
    }
}