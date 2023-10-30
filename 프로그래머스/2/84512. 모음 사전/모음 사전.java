import java.util.ArrayList;
import java.util.List;


class Solution {
    
    private static final char[] vowels = "AEIOU".toCharArray();
    
    public int solution(String word) {
        List<String> answer = new ArrayList<>();
        generate("", answer);
        return answer.indexOf(word);
    }
    
    private void generate(String word, List<String> answer) {
        answer.add(word);
        
        if (word.length() == 5) {
            return;
        }
        
        for (char vowel : vowels) {
            generate(word + vowel, answer);
        }
    }
}