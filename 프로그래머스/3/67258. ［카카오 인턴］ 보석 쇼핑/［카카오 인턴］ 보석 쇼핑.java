import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Solution {
    
    public int[] solution(String[] gems) {
        int[] answer = {0, gems.length};
        
        Map<String, Integer> counter = new HashMap<>();
        int n = Arrays.stream(gems)
                .distinct()
                .collect(Collectors.toList())
                .size();
        
        int left = 0;
        for (int right = 0; right < gems.length; right++) {
            counter.put(gems[right], counter.getOrDefault(gems[right], 0) + 1);
            
            while (counter.size() == n) {
                counter.put(gems[left], counter.get(gems[left]) - 1);
                if (counter.get(gems[left]) == 0) {
                    counter.remove(gems[left]);
                }
                left++;
            }
            
            if (left == 0) continue;
            
            counter.put(gems[--left], 1);
            
            if (right - left < answer[1] - answer[0]) {
                answer[0] = left + 1;
                answer[1] = right + 1;
            }
        }

        return answer;
    }
}