import java.util.*;

class Solution {
    
    public int solution(int[] priorities, int location) {
        Queue<int[]> queue = new LinkedList<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        
        for (int i = 0; i < priorities.length; i++) {
            queue.offer(new int[]{i, priorities[i]});
            maxHeap.offer(priorities[i]);
        }
        
        int order = 0;
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            
            if (current[1] < maxHeap.peek()) {
                queue.offer(current);
            } else {
                order++;
                maxHeap.poll();
                
                if (current[0] == location) {
                    return order;
                }
            }
        }
        
        return order;
    }
}