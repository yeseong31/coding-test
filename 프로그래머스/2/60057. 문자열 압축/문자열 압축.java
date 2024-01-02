import java.lang.StringBuilder;

class Solution {
    public int solution(String s) {
        int answer = s.length();
        for (int token = 1; token <= s.length() / 2; token++) {
            answer = Math.min(answer, compress(s, token));
        }
        return answer;
    }
    
    private int compress(final String s, final int token) {
        StringBuilder sb = new StringBuilder();
        String prev = s.substring(0, token);
        String target;
        int repeat = 1;
        
        for (int index = token; index < s.length(); index += token) {
            target = s.substring(index, Math.min(index + token, s.length()));
            if (prev.equals(target)) {
                repeat += 1;
                continue;
            }
            if (repeat > 1) {
                sb.append(Integer.toString(repeat));
            }
            sb.append(prev);
            prev = target;
            repeat = 1;
        }
        
        if (repeat > 1) {
            sb.append(Integer.toString(repeat));
        }
        sb.append(prev);
        
        return sb.length();
    }
}