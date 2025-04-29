import java.util.ArrayList;
import java.util.List;


class Solution {
    private static final char[] vowels = new char[] {'A', 'E', 'I', 'O', 'U'};
    
    private void makeDictionary(StringBuilder sb, List<String> dic) {
        if (sb.toString().length() == 5) {
            return;
        }
        
        for (int i = 0; i < 5; i++) {
            sb.append(vowels[i]);
            dic.add(sb.toString());
            
            makeDictionary(sb, dic);
            
            sb.deleteCharAt(sb.toString().length() - 1);
        }
    }
    
    public int solution(String word) {
        List<String> dic = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        
        makeDictionary(sb, dic);
        
        return dic.indexOf(word) + 1;
    }
}