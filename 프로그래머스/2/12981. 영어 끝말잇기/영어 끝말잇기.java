import java.util.HashSet;
import java.util.Set;

class Solution {
    
    public int[] solution(int n, String[] words) {
        Set<String> used = new HashSet<>();
        used.add(words[0]);
        
        char prev = words[0].charAt(words[0].length() - 1);
        int cnt = 1;
        
        for (int i = 1; i < words.length; i++) {
            String word = words[i];
            
            if (used.contains(word) || prev != word.charAt(0)) {
                return new int[]{cnt % n + 1, cnt / n + 1};
            }
            
            used.add(word);
            cnt++;
            prev = word.charAt(word.length() - 1);
        }
        
        return new int[]{0, 0};
    }
}