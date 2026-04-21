import java.util.*;

class Solution {
    
    public int solution(int[] food_times, long k) {
        long total = 0;
        for (int t : food_times) {
            total += t;
        }
        
        if (total <= k) return -1;
        
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        
        for (int i = 0; i < food_times.length; i++) {
            pq.offer(new int[]{food_times[i], i + 1});
        }
        
        long prev = 0;
        int n = food_times.length;
        
        while (!pq.isEmpty()) {
            int[] current = pq.peek();
            long diff = current[0] - prev;
            
            if (diff == 0) {
                pq.poll();
                n--;
                continue;
            }
            
            long spend = diff * n;
            
            if (spend > k) break;
            
            k -= spend;
            prev = current[0];
            pq.poll();
            n--;
        }
        
        List<int[]> remain = new ArrayList<>();
        while (!pq.isEmpty()) {
            remain.add(pq.poll());
        }
        
        remain.sort(Comparator.comparingInt(a -> a[1]));
        
        return remain.get((int)(k % remain.size()))[1];
    }
}