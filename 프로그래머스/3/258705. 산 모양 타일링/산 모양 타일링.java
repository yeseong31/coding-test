class Solution {

    private static final int MOD = 10_007;

    public int solution(int n, int[] tops) {
        int size = n * 3 + 2;

        int[] dp = new int[size];
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i < size; i++) {
            dp[i] = dp[i - 1];
            dp[i] += switch (i % 3) {
                case 0 -> (tops[(i / 3) - 1] == 1) ? dp[i - 2] : 0;
                case 1 -> dp[i - 3];
                case 2 -> (tops[(i - 1) / 3 - 1] == 1) ? dp[i - 2] : dp[i - 3];
                default -> 0;
            };
            dp[i] %= MOD;
        }

        return dp[size - 1];
    }
}