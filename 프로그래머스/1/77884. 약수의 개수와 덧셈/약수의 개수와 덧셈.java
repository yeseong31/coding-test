
class Solution {
    public int solution(int left, int right) {
        int answer = 0;

        for (int n = left; n <= right; n++) {
            if (Math.sqrt(n) % 1 == 0) {
                answer -= n;
            } else {
                answer += n;
            }
        }

        return answer;
    }
}