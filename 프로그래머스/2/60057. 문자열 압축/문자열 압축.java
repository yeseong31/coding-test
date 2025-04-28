import java.util.ArrayList;
import java.util.List;



class Solution {
    private int compress(String s, int n) {
        List<String> tokens = new ArrayList<>();
        int index = 0;
        
        while (index < s.length()) {
            int endIndex = (index + n) < s.length() ? (index + n) : s.length();
            String token = s.substring(index, endIndex);
            
            tokens.add(token);
            index += n;
        }
        
        StringBuilder sb = new StringBuilder();
        String prev = null;
        int count = 1;
        
        for (String cur : tokens) {
            if (prev == null) {
                prev = cur;
                continue;
            }
            
            if (prev.equals(cur)) {
                count++;
                continue;
            }
            
            if (count != 1) {
                sb.append(Integer.toString(count));
            }
            
            sb.append(prev);
            prev = cur;
            count = 1;
        }
            
        if (count != 1) {
            sb.append(Integer.toString(count));
        }
        
        sb.append(prev);
        return sb.toString().length();
    }
    
    public int solution(String s) {
        int answer = s.length();
        
        for (int n = 1; n < s.length() / 2 + 1; n++) {
            answer = Math.min(answer, compress(s, n));
        }
        
        return answer;
    }
}