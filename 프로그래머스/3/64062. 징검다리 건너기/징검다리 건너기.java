class Solution {

    private int[] stones;
    private int k;

    public int solution(int[] stones, int k) {
        this.stones = stones;
        this.k = k;

        int left = 0, right = 0;
        for (int s : stones) right = Math.max(right, s);

        int answer = 0;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (check(mid)) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return answer;
    }

    private boolean check(int n) {
        int jump = 0;
        for (int stone : stones) {
            if (stone - n >= 0) {
                jump = 0;
            } else if (++jump >= k) {
                return false;
            }
        }
        return true;
    }
}