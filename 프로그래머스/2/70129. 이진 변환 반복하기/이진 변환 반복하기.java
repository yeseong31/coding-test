class Solution {
    public int[] solution(String s) {
        int count = 0;
        int removedZero = 0;
        
        while (!s.equals("1")) {
            count += 1;
            int target = countZero(s);
            removedZero += target;
            s = Integer.toString(s.length() - target, 2);
        }
        
        return new int[] {count, removedZero};
    }
    
    private int countZero(String s) {
        int result = 0;
        for (char c : s.toCharArray()) {
            if (c == '0') {
                result++;
            }
        }
        return result;
    }
}