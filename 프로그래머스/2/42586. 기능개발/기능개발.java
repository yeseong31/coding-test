import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int n = progresses.length;
        int[] days = new int[n];
        
        for (int i = 0; i < n; i++) {
            days[i] = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
        }
        
        List<Integer> answer = new ArrayList<>(); 
        int prev = 0;
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            if (days[prev] >= days[i]) {
                count++;
                continue;
            }
            
            answer.add(count);
            count = 1;
            prev = i;
        }
        
        answer.add(count);
        return answer.stream().mapToInt(v -> v).toArray();
    }
}