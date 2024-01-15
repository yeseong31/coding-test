import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String before, String after) {
        Map<Character, Integer> used = new HashMap<>();
        
        for (char c : before.toCharArray()) {
            used.putIfAbsent(c, 0);
            used.put(c, used.get(c) + 1);
        }
        
        for (char c : after.toCharArray()) {
            if (!used.containsKey(c)) {
                return 0;
            }
            
            used.put(c, used.get(c) - 1);
            
            if (used.get(c) < 0) {
                return 0;
            }
        }
        
        return 1;
    }
}