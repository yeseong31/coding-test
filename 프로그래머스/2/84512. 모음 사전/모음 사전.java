import java.util.ArrayList;
import java.util.List;


class Solution {
    private static final char[] vowels = new char[] {'A', 'E', 'I', 'O', 'U'};
    
    private void makeDictionary(StringBuilder sb, List<String> dic) {
        if (sb.toString().length() == 5) {
            return;
        }
        
        for (char vowel : vowels) {
            sb.append(vowel);
            dic.add(sb.toString());
            
            makeDictionary(sb, dic);
            
            sb.deleteCharAt(sb.length() - 1);
        }
    }
    
    public int solution(String word) {
        List<String> dic = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        
        makeDictionary(sb, dic);
        
        return dic.indexOf(word) + 1;
    }
}