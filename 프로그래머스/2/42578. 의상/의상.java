import java.util.HashMap;
import java.util.Map;

class Solution {
    
    public int solution(String[][] clothes) {
        Map<String, Integer> counts = new HashMap<>();

        for (String[] cloth : clothes) {
            String category = cloth[1];
            counts.put(category, counts.getOrDefault(category, 0) + 1);
        }

        int answer = 1;
        for (int count : counts.values()) {
            answer *= count + 1;
        }
        return answer - 1;
    }
}