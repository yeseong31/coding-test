import java.util.Arrays;

class Solution {
    public int solution(int[][] board, int[][] skill) {
        int n = board.length;
        int m = board[0].length;
        int[][] scores = new int[n + 1][m + 1];
        
        for (int[] row : scores) {
            Arrays.fill(row, 0);
        }
        
        for (int[] s : skill) {
            int r1 = s[1];
            int c1 = s[2];
            int r2 = s[3];
            int c2 = s[4];
            int degree = s[5];
            
            if (s[0] == 1) degree *= -1;
            
            scores[r1][c1] += degree;
            scores[r1][c2 + 1] -= degree;
            scores[r2 + 1][c1] -= degree;
            scores[r2 + 1][c2 + 1] += degree;
        }
        
        for (int x = 1; x < n; x++) {
            for (int y = 0; y < m; y++) {
                scores[x][y] += scores[x - 1][y];
            }
        }
        
        for (int x = 0; x < n; x++) {
            for (int y = 1; y < m; y++) {
                scores[x][y] += scores[x][y - 1];
            }
        }
        
        int answer = 0;
        
        for (int x = 0; x < n; x++) {
            for (int y = 0; y < m; y++) {
                if (board[x][y] + scores[x][y] > 0) {
                    answer++;
                }
            }
        }
        
        return answer;
    }
}