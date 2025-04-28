class Solution {
    private int countZero(String s) {
        int count = 0;
        
        for (char c : s.toCharArray()) {
            if (c == '0') {
                count++;
            }
        }
        
        return count;
    }
    
    public int[] solution(String s) {
        int seq = 0;
        int total_zero_count = 0;
        
        while (!s.equals("1")) {
            int zero_count = countZero(s);
            total_zero_count += zero_count;
            
            int next_s_length = s.length() - zero_count;
            s = Integer.toString(next_s_length, 2);
            seq++;
        }
        
        return new int[] {seq, total_zero_count};
    }
}