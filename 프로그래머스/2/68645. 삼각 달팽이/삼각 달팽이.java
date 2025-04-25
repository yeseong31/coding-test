import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final int[] dx = {1, 0, -1};
    private static final int[] dy = {0, 1, -1};
    
    public int[] solution(int n) {
        int[][] triangle = new int[n][n];
        
        int x = -1;
        int y = 0;
        int count = 1;
        
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                x += dx[i % 3];
                y += dy[i % 3];
                triangle[x][y] = count++;
            }
        }
        
        List<Integer> answer = new ArrayList<>();
        for (int[] row : triangle) {
            for (int r : row) {
                if (r != 0) {
                    answer.add(r);
                }
            }
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
}