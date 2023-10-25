class Solution {
    boolean solution(String s) {
        s = s.toLowerCase();
        
        int countP = s.length() - s.replace("p", "").length();
        int countY = s.length() - s.replace("y", "").length();
        
        return countP == countY;
    }
}