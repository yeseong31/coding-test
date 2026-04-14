class Solution {
    
    public long solution(long n) {
        double x = Math.sqrt(n);
        
        if (x == (long)x) {
            return (long)Math.pow(x + 1, 2);
        } else {
            return -1;
        }
    }
}