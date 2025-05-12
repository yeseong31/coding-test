import java.util.HashSet;
import java.util.Set;

class Solution {
    public String solution(String my_string) {
        Set<Character> checked = new HashSet<>();
        StringBuilder sb = new StringBuilder();
        
        for (char c : my_string.toCharArray()) {
            if (!checked.contains(c)) {
                checked.add(c);
                sb.append(c);
            }
        }
        
        return sb.toString();
    }
}