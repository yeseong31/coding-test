class Solution {

    public long solution(int[] arr) {
        long answer = arr[0];
        for (int i = 1; i < arr.length; i++) {
            answer = answer / gcd(answer, arr[i]) * arr[i];
        }
        return answer;
    }

    private long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}