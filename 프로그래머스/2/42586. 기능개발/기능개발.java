import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        int count = 0;
        
        for (int index = 0; index < progresses.length; index++) {
            int remainingDay = calculateRemainingDay(index, progresses, speeds);
            
            while (!queue.isEmpty() && queue.peek() < remainingDay) {
                queue.poll();
                count++;
            }
            
            queue.add(remainingDay);
            
            if (count > 0) {
                answer.add(count);
                count = 0;
            }
        }
        
        answer.add(queue.size());
        
        return answer.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
    
    private int calculateRemainingDay(int index, int[] progresses, int[] speeds) {
        return (int) Math.ceil((100.0 - progresses[index]) / speeds[index]);
    }
}