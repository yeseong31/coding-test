class Solution {
    
    public long solution(int a, int b) {
        int start = Math.min(a, b);
        int end = Math.max(a, b);
        
        long n = end - start + 1;
        return n * (start + end) / 2;
    }
}