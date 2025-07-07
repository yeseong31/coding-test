class Solution {
    public int solution(int n) {
        int a = 0;
        int b = 1;
        
        for (int i = 2; i <= n; i++) {
            int temp = a;
            a = b;
            b = (temp + b) % 1234567;
        }
        
        return b;
    }
}