class Solution {
    public int solution(int n) {
        long a = 1;
        long b = 1;
        
        for (int i = 2; i < n; i++) {
            long tmp = a;
            a = b;
            b = (tmp + b) % 1234567;
        }
        
        return (int) b;
    }
}