import java.util.Arrays;

class Solution {

    public int solution(int distance, int[] rocks, int n) {
        Arrays.sort(rocks);

        int low = 1;
        int high = distance;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (canMaintainDistance(rocks, distance, n, mid)) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return high;
    }

    private boolean canMaintainDistance(
            int[] rocks,
            int distance,
            int maxRemovals,
            int minDistance
    ) {
        int removed = 0;
        int previous = 0;

        for (int rock : rocks) {
            if (rock - previous < minDistance) {
                removed++;

                if (removed > maxRemovals) {
                    return false;
                }
            } else {
                previous = rock;
            }
        }
        
        if (distance - previous < minDistance) {
            removed++;
        }

        return removed <= maxRemovals;
    }
}