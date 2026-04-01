class Solution {

    public boolean check(long x, int n, int[] target) {
        for (int i = n; i > 0; i--) {
            int mod = (int)(x % 5);
            x /= 5;

            if (mod == 2) {
                return false;
            }

            if (x == 1) {
                return target[mod] == 1;
            }
        }
        return true;
    }

    public int solution(int n, long l, long r) {
        int[] target = {1, 1, 0, 1, 1};
        int answer = 0;

        for (long x = l - 1; x < r; x++) {
            if (check(x, n, target)) {
                answer++;
            }
        }

        return answer;
    }
}