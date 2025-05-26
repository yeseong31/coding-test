import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        
        Map<Integer, Integer> counter = new HashMap<>();
        Set<Integer> checked = new HashSet<>();
        
        for (int t : topping) {
            counter.put(t, counter.getOrDefault(t, 0) + 1);
        }
        
        for (int t : topping) {
            counter.put(t, counter.get(t) - 1);
            if (counter.get(t) == 0) {
                counter.remove(t);
            }
            
            checked.add(t);
            if (checked.size() == counter.size()) {
                answer++;
            }
        }
        
        return answer;
    }
}