import java.util.*;

class Solution {
    
    public int solution(int[] priorities, int location) {
        Deque<int[]> q = new ArrayDeque<>();
        
        for (int i = 0; i < priorities.length; i++) {
            q.offer(new int[]{i, priorities[i]});
        }
        
        int cnt = 1;
        
        while (!q.isEmpty()) {
            int[] current = q.poll();
            int idx = current[0];
            int val = current[1];
            
            boolean hasHigher = false;
            
            for (int[] item : q) {
                if (item[1] > val) {
                    hasHigher = true;
                    break;
                }
            }
            
            if (hasHigher) {
                q.offer(current);
                continue;
            }
            
            if (idx == location) {
                return cnt;
            }
            
            cnt++;
        }
        
        return cnt;
    }
}