import java.util.Arrays;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        rocks = Arrays.copyOf(rocks, rocks.length + 1);
        rocks[rocks.length - 1] = distance;
        Arrays.sort(rocks);
        
        int answer = 0;
        int start = 0;
        int end = distance + 1;
        
        while (start < end) {
            int mid = (start + end) /  2;
            
            int prev = 0;
            int count = 0;
            
            for (int r : rocks) {
                if (r - prev < mid) {
                    count++;
                } else {
                    prev = r;
                }
                
                if (count > n) {
                    break;
                }
            }
            
            if (count > n) {
                end = mid;
            } else {
                answer = mid;
                start = mid + 1;
            }
        }
        
        return answer;
    }
}