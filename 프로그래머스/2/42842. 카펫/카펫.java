class Solution {
    public int[] solution(int brown, int yellow) {
        int area = brown + yellow;
        
        for (int n = 3; n <= (int) Math.sqrt(area); n++) {
            if (area % n == 0 && (n - 2) * ((area / n) - 2) == yellow) {
                return new int[] {area / n, n};
            }
        }
        
        return null;
    }
}
