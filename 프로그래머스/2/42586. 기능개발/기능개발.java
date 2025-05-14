import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        
        int n = progresses.length;
        int days = 0;
        int current = 0;
        int count;
        
        while (true) {
            days++;
            if (current == n) {
                break;
            }
            
            count = 0;
            while (current < n && progresses[current] + speeds[current] * days >= 100) {
                count++;
                current++;
            }
            
            if (count > 0) {
                answer.add(count);
            }
        }
        
        return answer.stream()
                .mapToInt(Integer::valueOf)
                .toArray();
    }
}