import java.util.Arrays;

class Solution {
    
    public int solution(int distance, int[] rocks, int n) {
        int answer = 1;
        int minDistance = 1;
        int maxDistance = distance + 1;
        
        rocks = Arrays.copyOf(rocks, rocks.length + 1);
        rocks[rocks.length - 1] = distance;
        Arrays.sort(rocks);
        
        while (minDistance < maxDistance) {
            int targetDistance = (minDistance + maxDistance) / 2;
            
            if (canCrossBridge(targetDistance, rocks, n)) {
                answer = Math.max(answer, targetDistance);
                minDistance = targetDistance + 1;
            } else {
                maxDistance = targetDistance;
            }
        }
        
        return answer;
    }
    
    private boolean canCrossBridge(int targetDistance, int[] rocks, int n) {
        int removed = 0;
        int last = 0;
        
        for (int rock : rocks) {
            if (rock - last < targetDistance) {
                removed++;
                continue;
            }
            last = rock;
        }
        
        return removed <= n;
    }
}
