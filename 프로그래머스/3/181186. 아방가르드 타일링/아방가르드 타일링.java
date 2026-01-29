class Solution {
    public int solution(int n) {
        final int DIV = 1_000_000_007;

        if (n == 1) return 1;
        if (n == 2) return 3;
        if (n == 3) return 10;

        long[] dp = new long[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 3;
        dp[3] = 10;
        if (n >= 4) dp[4] = 23;

        for (int i = 5; i <= n; i++) {
            long val = dp[i - 1];
            val = (val + 2 * dp[i - 2]) % DIV;
            val = (val + 6 * dp[i - 3]) % DIV;
            val = (val + dp[i - 4]) % DIV;
            if (i - 6 >= 0) {
                val = (val - dp[i - 6]) % DIV;
            }
            if (val < 0) val += DIV;
            dp[i] = val;
        }

        return (int) dp[n];
    }
}