import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final int[] dx = {-1, 0, 1, 0, -1, 1, 1, -1, -2, 0, 2, 0};
    private static final int[] dy = {0, 1, 0, -1, 1, 1, -1, -1, 0, 2, 0, -2};
    
    private class Point {
        private final int x;
        private final int y;
        
        private Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
        
        public int getX() {
            return x;
        }
        
        public int getY() {
            return y;
        }
    }
    
    private boolean isDistanced(char[][] place, Point p) {
        int x = p.getX();
        int y = p.getY();

        for (int i = 0; i < 12; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= 5 || ny < 0 || ny >= 5 || place[nx][ny] != 'P') {
                continue;
            }

            int distX = Math.abs(nx - x);
            int distY = Math.abs(ny - y);

            int mx = (nx < x) ? x - 1 : x + 1;
            int my = (ny < y) ? y - 1 : y + 1;

            if (distX == 2) {
                if (place[mx][ny] == 'O') {
                    return false;
                }
            } else if (distY == 2) {
                if (place[nx][my] == 'O') {
                    return false;
                }
            } else if (distX == 1 && distY == 1) {
                if (!(place[nx][y] == 'X' && place[x][ny] == 'X')) {
                    return false;
                }
            } else if (place[nx][ny] == 'P') {
                return false;
            }
        }
        
        return true;
    }
    
    private boolean isPossiblePlace(char[][] place) {
        List<Point> persons = new ArrayList<>();
        
        for (int x = 0; x < 5; x++) {
            for (int y = 0; y < 5; y++) {
                if (place[x][y] == 'P') {
                    persons.add(new Point(x, y));
                }
            }
        }
        
        for (Point person : persons) {
            if (!isDistanced(place, person)) {
                return false;
            }
        }
        
        return true;
    }
    
    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];
        
        for (int i = 0; i < places.length; i++) {
            char[][] place = new char[5][];
            for (int j = 0; j < 5; j++) {
                place[j] = places[i][j].toCharArray();
            }
            
            if (isPossiblePlace(place)) {
                answer[i] = 1;
            } else {
                answer[i] = 0;
            }
        }
        
        return answer;
    }
}