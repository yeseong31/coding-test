class Solution {
    public int[] solution(String s) {
        int countZero = 0;
        int repeat = 0;
        
        while (!s.equals("1")) {
            String target = s.replaceAll("0", "");
            countZero += s.length() - target.length();
            s = Integer.toString(target.length(), 2);
            repeat++;
        }
        
        return new int[] {repeat, countZero};
    }
}
