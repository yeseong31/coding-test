class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        
        while (a <= n) {
            int div = n / a;
            int mod = n % a;
            
            answer += div * b;
            n = div * b + mod;
        }
        
        return answer;
    }
}