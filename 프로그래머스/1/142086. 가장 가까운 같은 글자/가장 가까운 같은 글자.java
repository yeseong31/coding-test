import java.util.*;

class Solution {
    
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        Map<Character, Integer> word = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            if (word.containsKey(c)) {
                answer[i] = i - word.get(c);
            } else {
                answer[i] = -1;
            }
            
            word.put(c, i);
        }
        
        return answer;
    }
}