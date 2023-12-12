import java.util.Arrays;


class Solution {
    public long solution(int n, int[] times) {
        long left = 1;
        long right = 1_000_000_000_000_000L;
        
        while (left < right) {
            long mid = (left + right) / 2;

            if (canImmigration(n, times, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    private boolean canImmigration(int n, int[] times, long mid) {
        long count = 0;
        for (int time : times) {
            count += mid / time;
        }
        return count >= n;
    }
}
