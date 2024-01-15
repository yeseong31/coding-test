import java.util.Arrays;

class Solution {
    
    public int solution(int m, int n, int[][] puddles) {
        int[][] board = new int[n + 1][m + 1];
        board[1][1] = 1;
        
        for (int[] puddle : puddles) {
            board[puddle[1]][puddle[0]] = -1;
        }
        
        for (int x = 1; x <= n; x++) {
            for (int y = 1; y <= m; y++) {
                if (x == 1 && y == 1) {
                    continue;
                }
                if (board[x][y] == -1) {
                    board[x][y] = 0;
                    continue;
                }
                
                board[x][y] = (board[x - 1][y] + board[x][y - 1]) % 1_000_000_007;
            }
        }
        
        return board[n][m];
    }
}