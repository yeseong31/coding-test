import java.util.Arrays;

class Solution {
    private int removeZero(String s) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '0') count++;
        }
        return count;
    }
    
    public int[] solution(String s) {
        int[] answer = {0, 0};
        
        while (!s.equals("1")) {
            int zero = removeZero(s);
            
            answer[0]++;
            answer[1] += zero;
            
            s = Integer.toString(s.length() - zero, 2);
        }
        
        return answer;
    }
}