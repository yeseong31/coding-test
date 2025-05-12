import java.util.Arrays;

class Solution {
    public int solution(String before, String after) {
        if (before.length() != after.length()) {
            return 0;
        }
        
        char[] a = before.toCharArray();
        char[] b = after.toCharArray();
        
        Arrays.sort(a);
        Arrays.sort(b);
        
        for (int i = 0; i < before.length(); i++) {
            if (a[i] != b[i]) {
                return 0;
            }
        }
        
        return 1;
    }
}