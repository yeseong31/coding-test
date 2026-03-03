class Solution {
    
    public int solution(int storey) {
        int answer = 0;

        while (storey != 0) {
            int div = storey / 10;
            int mod = storey % 10;

            if (mod == 0) {
                storey = div;
            } else if (mod >= 6 || (mod == 5 && div % 10 >= 5)) {
                answer += 10 - mod;
                storey += 10 - mod;
            } else {
                answer += mod;
                storey -= mod;
            }
        }

        return answer;
    }
}