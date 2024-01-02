import java.lang.StringBuilder;


class Solution {
    public String solution(String s, int n) {
        StringBuilder sb = new StringBuilder();
        
        for (char c : s.toCharArray()) {
            sb.append(push(c, n));
        }
        
        return sb.toString();
    }
    
    private char push(final char c, final int n) {
        if (c == ' ') {
            return c;
        }
        int offset = Character.isUpperCase(c) ? 'A' : 'a';
        int position = (c - offset + n) % ('z' - 'a' + 1);
        return (char) (offset + position);
    }
}