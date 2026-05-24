public class Solution {
    
    private double calculate(long r, long w) {
        return Math.sqrt(Math.pow(r, 2) - Math.pow(w, 2));
    }

    public long solution(int r1, int r2) {
        long answer = 0;

        for (int w = 1; w < r2; w++) {
            double h1 = calculate(r1, w);
            double h2 = calculate(r2, w);

            if (w >= r1) {
                answer += (long) Math.floor(h2) + 1;
                continue;
            }

            answer += (long) Math.floor(h2) - (long) Math.floor(h1);

            if (h1 % 1 == 0) {
                answer += 1;
            }
        }

        return 4 * (answer + 1);
    }
}