import java.util.Arrays;

class Solution {
    
    private static final int INFINITY = 1_000_000_000;
    
    public int solution(int[][] matrix_sizes) {
        int n = matrix_sizes.length;
        int[][] dp = createDp(n);
        
        for (int step = 1; step < n; step++) {
            for (int i = 0; i < n; i++) {
                int j = i + step;
                
                if (n <= j) {
                    break;
                }
                
                for (int k = i; k < j; k++) {
                    dp[i][j] = receiveMinValue(i, j, k, dp, matrix_sizes);
                }
            }
        }
        
        return dp[0][n - 1];
    }
    
    private int receiveMinValue(int i, int j, int k, int[][] dp, int[][] matrix_sizes) {
        return Math.min(
                dp[i][j], 
                dp[i][k] + dp[k + 1][j] + (matrix_sizes[i][0] * matrix_sizes[k + 1][0] * matrix_sizes[j][1]));
    }
    
    private int[][] createDp(int n) {
        int[][] dp = new int[n][n];
        
        for (int[] row : dp) {
            Arrays.fill(row, INFINITY);
        }
        
        for (int x = 0; x < n; x++) {
            dp[x][x] = 0;
        }
        
        return dp;
    }
}