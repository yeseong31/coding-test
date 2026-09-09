import java.util.ArrayDeque;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Queue;

class Solution {
    
    public int solution(int[] priorities, int location) {
        Queue<int[]> queue = new ArrayDeque<>();
        PriorityQueue<Integer> maxHeap =
                new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < priorities.length; i++) {
            queue.offer(new int[]{i, priorities[i]});
            maxHeap.offer(priorities[i]);
        }

        int order = 0;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();

            if (current[1] < maxHeap.peek()) {
                queue.offer(current);
                continue;
            }

            order++;
            maxHeap.poll();

            if (current[0] == location) {
                return order;
            }
        }

        return -1;
    }
}