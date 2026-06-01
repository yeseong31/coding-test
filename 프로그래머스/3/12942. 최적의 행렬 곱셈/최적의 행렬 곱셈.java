import java.util.Arrays;

class Solution {
    
    private static final int INFINITY = 1_000_000_000;
    
    public int solution(int[][] matrixSizes) {
        int n = matrixSizes.length;
        int[][] dp = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], INFINITY);
            dp[i][i] = 0;
        }
        
        for (int length = 1; length < n; length++) {
            for (int i = 0; i < n - length; i++) {
                int j = i + length;
                
                for (int k = i; k < j; k++) {
                    int cost = dp[i][k] + dp[k + 1][j] + (matrixSizes[i][0] * matrixSizes[k][1] * matrixSizes[j][1]);
                    if (cost < dp[i][j]) {
                        dp[i][j] = cost;
                    }
                }
            }
        }
        
        return dp[0][n - 1];
    }
}