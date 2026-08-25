class Solution {
    public long solution(int k, int d) {
        long answer = 0;
        long maxDistanceSquared = (long) d * d;

        for (long x = 0; x <= d; x += k) {
            long yMax = (long) Math.sqrt(
                maxDistanceSquared - x * x
            );

            answer += yMax / k + 1;
        }

        return answer;
    }
}