import java.util.Arrays;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        Arrays.sort(rocks);
        rocks = Arrays.copyOf(rocks, rocks.length + 1);
        rocks[rocks.length - 1] = distance;
        
        int start = 1;
        int end = distance + 1;
        
        while (end - start > 1) {
            int mid = (start + end) / 2;
            if (isValid(mid, rocks, n)) {
                start = mid;
            } else {
                end = mid;
            }
        }
        
        return start;
    }
    
    private static boolean isValid(int mid, int[] rocks, int n) {
        int removed = 0;
        int last = 0;
        
        for (int rock : rocks) {
            if (rock - last < mid) {
                removed++;
                continue;
            }
            
            last = rock;
        }
        
        return removed <= n;
    }
}