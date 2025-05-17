import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Point {
    public int x;
    public int y;
    
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Solution {
    private final int[] dx = {0, 0, 1, -1};
    private final int[] dy = {1, -1, 0, 0};
    
    private void isOutside(char[][] storage, Point point) {
        boolean result = false;
        int nx;
        int ny;
        
        for (int i = 0; i < 4; i++) {
            nx = point.x + dx[i];
            ny = point.y + dy[i];
            
            if (storage[nx][ny] == '0') {
                storage[point.x][point.y] = '0';
                result = true;
                break;
            }
        }
        
        if (!result) {
            return;
        }
        
        for (int i = 0; i < 4; i++) {
            nx = point.x + dx[i];
            ny = point.y + dy[i];

            if (storage[nx][ny] == '#') {
                storage[nx][ny] = '0';
                isOutside(storage, new Point(nx, ny));
            }
        }
    }
    
    private void useFork(char q, char[][] storage) {
        List<Point> points = new ArrayList<>();
        
        for (int x = 1; x < storage.length - 1; x++) {
            for (int y = 1; y < storage[0].length - 1; y++) {
                if (storage[x][y] != q) {
                    continue;
                }
                
                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    
                    if (storage[nx][ny] == '0') {
                        points.add(new Point(x, y));
                        break;
                    }
                }
            }
        }
        
        for (Point point : points) {
            storage[point.x][point.y] = '0';
            isOutside(storage, point);
        }
    }
    
    private void useCrane(char q, char[][] storage) {
        for (int x = 1; x < storage.length - 1; x++) {
            for (int y = 1; y < storage[0].length - 1; y++) {
                if (storage[x][y] == q) {
                    storage[x][y] = '#';
                    isOutside(storage, new Point(x, y));
                }
            }
        }
    }
    
    public int solution(String[] storage, String[] requests) {
        int answer = 0;
        char[][] extStorage = new char[storage.length + 2][storage[0].length() + 2];
        
        for (int i = 0; i < extStorage.length; i++) {
            Arrays.fill(extStorage[i], '0');
        }   
        
        for (int i = 0; i < storage.length; i++) {
            for (int j = 0; j < storage[i].length(); j++) {
                extStorage[i + 1][j + 1] = storage[i].charAt(j);
            }
        }
        
        for (String query : requests) {
            if (query.length() == 1) {
                useFork(query.charAt(0), extStorage);
            } else {
                useCrane(query.charAt(0), extStorage);
            }
        }
        
        for (int i = 1; i < storage.length + 1; i++) {
            for (int j = 1; j <= storage[0].length(); j++) {
                if (extStorage[i][j] != '0' && extStorage[i][j] != '#') {
                    answer++;
                }
            }
        }
        
        return answer;
    }
}