class Solution {
    
    public int solution(int n) {
        int cnt = 0;

        while (n >= 1) {
            if (n % 2 == 1) {
                cnt++;
                n -= 1;
            } else {
                n /= 2;
            }
        }

        return cnt;
    }
}