import java.util.*;

class Solution {
    
    public int solution(int[] food_times, long k) {
        long total = 0;
        for (int time : food_times) {
            total += time;
        }
        
        if (total <= k) return -1;
        
        PriorityQueue<Food> pq = new PriorityQueue<>(Comparator.comparingInt(f -> f.time));
        for (int i = 0; i < food_times.length; i++) {
            pq.offer(new Food(food_times[i], i + 1));
        }
        
        long prevTime = 0;
        long remainFoods = food_times.length;
        
        while (!pq.isEmpty()) {
            long currentTime = pq.peek().time;
            long diff = currentTime - prevTime;
            
            if (diff == 0) {
                pq.poll();
                remainFoods--;
                continue;
            }
            
            long totalSpend = diff * remainFoods;
            if (totalSpend > k) break;
            
            k -= totalSpend;
            prevTime = currentTime;
            pq.poll();
            remainFoods--;
        }
        
        List<Food> remainList = new ArrayList<>(pq);
        remainList.sort(Comparator.comparingInt(f -> f.index));
        
        return remainList.get((int) (k % remainFoods)).index;
    }
    
    private static class Food {
        int time;
        int index;
        
        Food(int time, int index) {
            this.time = time;
            this.index = index;
        }
    }
}