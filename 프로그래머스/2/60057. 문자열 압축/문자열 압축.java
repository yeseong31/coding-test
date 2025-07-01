import java.lang.StringBuilder;
import java.util.ArrayList;
import java.util.List;

class Solution {

    private List<String> split(String s, int n) {
        List<String> result = new ArrayList<>();
        
        for (int start = 0; start <= s.length(); start += n) {
            int end = start + n;
            
            if (end > s.length()) {
                end = s.length();
            }
            
            result.add(s.substring(start, end));
        }
        
        return result;
    }
    
    private int compress(String s, int n) {
        StringBuilder sb = new StringBuilder();
        List<String> tokens = split(s, n);
        
        String prev = null;
        int count = 1;
        
        for (String token : tokens) {
            if (prev == null) {
                prev = token;
                continue;
            }
            
            if (token.equals(prev)) {
                count++;
                continue;
            }
            
            if (count > 1) sb.append(count);
            sb.append(prev);
            
            count = 1;
            prev = token;
        }
        
        if (count > 1) sb.append(count);
        sb.append(prev);
        
        return sb.length();
    }
    
    public int solution(String s) {
        if (s.length() == 1) {
            return 1;
        }
        
        int answer = s.length() + 1;
        
        for (int i = 1; i <= s.length() / 2; i++) {
            int length = compress(s, i);
            
            if (length < answer) {
                answer = length;
            }
        }
        
        return answer;
    }
}