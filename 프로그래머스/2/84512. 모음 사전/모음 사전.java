import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final char[] vowels = {'A', 'E', 'I', 'O', 'U'};
    
    private static void dfs(StringBuilder sb, List<String> words) {
        words.add(sb.toString());
        if (sb.length() == 5) return;
        
        for (char vowel : vowels) {
            sb.append(vowel);
            dfs(sb, words);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
    
    public int solution(String word) {
        List<String> words = new ArrayList<>();
        dfs(new StringBuilder(), words);
        return words.indexOf(word);
    }
}