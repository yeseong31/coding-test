import java.util.Arrays;

class Solution {
    public int solution(int n, int[] tops) {
        int answer = 0;
        int size = n * 3 + 2;
        int mod = 10007;
        
        int[] dp = new int[size];
        dp[1] = 1;
        dp[2] = 2;
        
        for (int i = 3; i < size; i++) {
            switch (i % 3) {
                case 0 -> {
                    int idx = i / 3 - 1;
                    if (tops[idx] == 0) {
                        dp[i] = dp[i - 1];
                    } else {
                        dp[i] = (dp[i - 1] + dp[i - 2]) % mod;
                    }
                }
                case 1 -> {
                    dp[i] = (dp[i - 1] + dp[i - 3]) % mod;
                }
                case 2 -> {
                    int idx = (i - 1) / 3 - 1;
                    if (tops[idx] == 0) {
                        dp[i] = (dp[i - 1] + dp[i - 3]) % mod;
                    } else {
                        dp[i] = (dp[i - 1] + dp[i - 2]) % mod;
                    }
                }
            }
        }
        
        return dp[size - 1];
    }
}