import java.util.Arrays;

class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] board = new int[n][m];
        
        for (int[] row : board) {
            Arrays.fill(row, 0);
        }
        for (int[] puddle : puddles) {
            int y = puddle[0] - 1;
            int x = puddle[1] - 1;
            board[x][y] = -1;
        }
        
        board[0][0] = 1;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == -1) {
                    board[i][j] = 0;
                    continue;
                }
                if (i != 0) {
                    board[i][j] += board[i - 1][j];
                }
                if (j != 0) {
                    board[i][j] += board[i][j - 1];
                }
                board[i][j] %= 1000000007;
            }
        }
        
        return board[n - 1][m - 1];
    }
}