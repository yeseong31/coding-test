import java.util.PriorityQueue;

class Solution {
    
    public int solution(int n, int k, int[] enemy) {
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for (int i = 0; i < k && i < enemy.length; i++) {
            pq.offer(enemy[i]);
        }
        
        for (int i = k; i < enemy.length; i++) {
            pq.offer(enemy[i]);
            n -= pq.poll();
            
            if (n < 0) {
                return i;
            }
        }
        
        return enemy.length;
    }
}