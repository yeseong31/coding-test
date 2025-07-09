import java.util.PriorityQueue;

class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.offer(24);
        
        for (int t = 0; t < players.length; t++) {
            int p = players[t];
            
            while (!pq.isEmpty() && pq.peek() == t) {
                pq.poll();
            }
            
            if (p < pq.size() * m) continue;
            
            while (pq.size() * m <= p) {
                pq.offer(t + k);
                answer++;
            }
        }
        
        return answer;
    }
}