import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] solution(String[] gems) {
        int[] answer = new int[] {1, gems.length};
        
        Map<String, Integer> kinds = new HashMap<>();
        
        int left = 0;
        long length = Arrays.stream(gems).distinct().count();
        
        for (int right = 0; right < gems.length; right++) {
            kinds.put(gems[right], kinds.getOrDefault(gems[right], 0) + 1);
            
            while (kinds.size() == length) {
                kinds.put(gems[left], kinds.get(gems[left]) - 1);
                
                if (kinds.get(gems[left]) == 0) {
                    if (answer[1] - answer[0] > right - left) {
                        answer[0] = left + 1;
                        answer[1] = right + 1;
                    }
                    
                    kinds.remove(gems[left]);
                }
                
                left++;
            }
        }
        
        return answer;
    }
}