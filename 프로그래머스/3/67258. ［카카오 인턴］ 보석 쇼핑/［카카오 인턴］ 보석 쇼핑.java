import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public int[] solution(String[] gems) {
        int[] answer = {0, gems.length};
        
        Map<String, Integer> count = new HashMap<>();
        Set<String> kind = new HashSet<>();
        
        for (String gem : gems) {
            kind.add(gem);
        }
        
        int start = 0;
        for (int end = 0; end < gems.length; end++) {
            count.put(gems[end], count.getOrDefault(gems[end], 0) + 1);
            
            while (start <= end && count.size() == kind.size()) {
                count.put(gems[start], count.get(gems[start]) - 1);
                
                if (count.get(gems[start]) == 0) {
                    if (end - start < answer[1] - answer[0]) {
                        answer[0] = start + 1;
                        answer[1] = end + 1;
                    }
                    count.remove(gems[start]);
                }
                start++;
            }
        }
        
        return answer;
    }
}