class Solution {
    public int[] solution(String s) {
        int[] answer = {0, 0};
        
        while (!s.equals("1")) {
            int zero = s.replaceAll("1", "").length();
            
            answer[0]++;
            answer[1] += zero;
            
            s = Integer.toString(s.length() - zero, 2);
        }
        
        return answer;
    }
}