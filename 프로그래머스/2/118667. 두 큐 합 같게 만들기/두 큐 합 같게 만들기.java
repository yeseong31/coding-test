import java.util.*;

class Solution {
    
    public int solution(int[] queue1, int[] queue2) {
        long sum1 = 0, sum2 = 0;
        
        for (int n : queue1) sum1 += n;
        for (int n : queue2) sum2 += n;
        
        long total = sum1 + sum2;
        if (total % 2 != 0) return -1;
        
        long target = total / 2;
        
        Deque<Integer> q1 = new ArrayDeque<>();
        Deque<Integer> q2 = new ArrayDeque<>();
        
        for (int n : queue1) {
            q1.offer(n);
        }
        for (int n : queue2) {
            q2.offer(n);
        }
        
        int count = 0;
        int limit = (queue1.length + queue2.length) * 3;
        
        while (!q1.isEmpty() && !q2.isEmpty() && count <= limit) {
            if (sum1 == target) return count;
            
            if (sum1 > target) {
                int x = q1.poll();
                sum1 -= x;
                q2.offer(x);
            } else {
                int x = q2.poll();
                sum1 += x;
                q1.offer(x);
            }
            
            count++;
        }
        
        return -1;
    }
}