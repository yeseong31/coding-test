import java.util.ArrayList;
import java.util.List;


class Solution {
    public int solution(String s) {
        int answer = s.length() + 1;
        
        for (int i = 1; i <= s.length(); i++) {
            answer = Math.min(answer, compress(s, i));
        }
        
        return answer;
    }
    
    private int compress(String s, int tokenLength) {
        StringBuilder sb = new StringBuilder();
        int count = 0;
        String last = "";
        
        for (String token : split(s, tokenLength)) {
            if (token.equals(last)) {
                count++;
                continue;
            }
            if (count > 1) {
                sb.append(count);
            }
            count = 1;
            sb.append(last);
            last = token;
        }
        
        if (count > 1) {
            sb.append(count);
        }
        sb.append(last);
        return sb.length();
    }
    
    private List<String> split(String s, int tokenLength) {
        List<String> tokens = new ArrayList<>();
        
        for (int startIndex = 0; startIndex < s.length(); startIndex += tokenLength) {
            int endIndex = startIndex + tokenLength;
            if (endIndex > s.length()) {
                endIndex = s.length();
            }
            String token = s.substring(startIndex, endIndex);
            tokens.add(token);
        }
        
        return tokens;
    }
}