import java.util.ArrayList;
import java.util.List;


class Solution {
    
    private static final char[] vowels = new char[] {'A', 'E', 'I', 'O', 'U'};
    
    public int solution(String word) {
        List<String> result = new ArrayList<>();
        makeDictionary("", result);
        return result.indexOf(word);
    }
    
    private void makeDictionary(final String currentWord, final List<String> result) {
        result.add(currentWord);
        
        if (currentWord.length() == 5) {
            return;
        }
        
        for (char vowel : vowels) {
            makeDictionary(currentWord + vowel, result);
        }
    }
}
