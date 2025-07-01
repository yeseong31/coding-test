import java.util.Arrays;

class Solution {
    private int countZero(String s) {
        return s.replaceAll("1", "").length();
    }
    
    public int[] solution(String s) {
        int[] answer = {0, 0};
        
        while (!s.equals("1")) {
            int zero = countZero(s);
            
            answer[0]++;
            answer[1] += zero;
            
            s = Integer.toString(s.length() - zero, 2);
        }
        
        return answer;
    }
}