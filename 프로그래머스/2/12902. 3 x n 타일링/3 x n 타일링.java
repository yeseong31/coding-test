class Solution {

    private static final long MOD = 1_000_000_007L;

    public int solution(int n) {
        if (n % 2 == 1) {
            return 0;
        }

        if (n == 0) {
            return 1;
        }

        if (n == 2) {
            return 3;
        }

        long previousPrevious = 1;
        long previous = 3;

        for (int i = 4; i <= n; i += 2) {
            long current = (4 * previous - previousPrevious + MOD) % MOD;

            previousPrevious = previous;
            previous = current;
        }

        return (int) previous;
    }
}