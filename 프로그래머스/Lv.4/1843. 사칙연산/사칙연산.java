import java.util.Arrays;

class Solution {
    
    private static final int INFINITY = 1_000_000_000;
    
    public int solution(String arr[]) {
        int size = arr.length / 2 + 1;
        
        int[][] maxDp = createDp(size, -INFINITY, arr);
        int[][] minDp = createDp(size, INFINITY, arr);
        
        for (int step = 1; step < size; step++) {
            for (int i = 0; i < size - step; i++) {
                int j = i + step;
                
                for (int k = i; k < j; k++) {
                    if (arr[k * 2 + 1].equals("+")) {
                        maxDp[i][j] = Math.max(maxDp[i][j], maxDp[i][k] + maxDp[k + 1][j]);
                        minDp[i][j] = Math.min(minDp[i][j], minDp[i][k] + minDp[k + 1][j]);
                    } else {
                        maxDp[i][j] = Math.max(maxDp[i][j], maxDp[i][k] - minDp[k + 1][j]);
                        minDp[i][j] = Math.min(minDp[i][j], minDp[i][k] - maxDp[k + 1][j]);
                    }
                }
            }
        }
        
        return maxDp[0][size - 1];
    }
    
    private int[][] createDp(int size, int number, String[] arr) {
        int[][] dp = new int[size][size];
        
        for (int[] row : dp) {
            Arrays.fill(row, number);
        }
        for (int index = 0; index < size; index++) {
            dp[index][index] = Integer.parseInt(arr[index * 2]);
        }
        
        return dp;
    }
}
