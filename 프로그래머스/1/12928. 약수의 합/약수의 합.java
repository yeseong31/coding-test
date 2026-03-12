public class Solution {
    
    public int solution(int n) {
        int answer = 0;

        for (int i = 1; i <= Math.sqrt(n); i++) {
            int div = n / i;
            int mod = n % i;

            if (mod == 0) {
                answer += i + div;
                if (i == div) {
                    answer -= div;
                    break;
                }
            }
        }

        return answer;
    }
}