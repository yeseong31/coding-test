import java.util.*;

class Solution {
    
    public int solution(int distLimit, int splitLimit) {
        long distance = distLimit;
        long limit = splitLimit;
        
        List<Long> values = new ArrayList<>();
        generateValues(1, limit, values);
        Collections.sort(values);
        
        int n = values.size();
        long[] minCost = new long[n];
        Arrays.fill(minCost, Long.MAX_VALUE);
        minCost[0] = 0;
        
        Map<Long, Integer> index = new HashMap<>();
        for (int i = 0; i < n; i++) {
            index.put(values.get(i), i);
        }
        
        for (int i = 0; i < n; i++) {
            if (minCost[i] == Long.MAX_VALUE) {
                continue;
            }
            
            long value = values.get(i);

            updateCost(value, value * 2, i, index, minCost, limit);
            updateCost(value, value * 3, i, index, minCost, limit);
        }
        
        long answer = 1;
        
        for (int i = 0; i < n; i++) {
            long value = values.get(i);
            long cost = minCost[i];

            if (cost > distance) {
                continue;
            }
            
            answer = Math.max(answer, value);
            
            long remaining = distance - cost;
            long extra = Math.min(value, remaining);

            if (value * 2 <= limit) {
                answer = Math.max(answer, value + extra);
            }
            
            if (value * 3 <= limit) {
                answer = Math.max(answer, value + extra * 2);
            }
        }
        
        return (int) answer;
    }
    
    private void updateCost(
            long current,
            long nextValue,
            int currentIndex,
            Map<Long, Integer> index,
            long[] minCost,
            long limit
    ) {
        if (nextValue > limit) {
            return;
        }
        
        int nextIndex = index.get(nextValue);
        minCost[nextIndex] = Math.min(
                minCost[nextIndex],
                minCost[currentIndex] + current
        );
    }
    
    private void generateValues(long value, long limit, List<Long> values) {
        if (value > limit) {
            return;
        }
        
        values.add(value);
        
        generateValues(value * 2, limit, values);
        generateValues(value * 3, limit, values);
    }
}