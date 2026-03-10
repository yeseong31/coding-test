import java.util.*;

class Solution {

    private int find(long n) {
        if (n == 1) {
            return 0;
        }

        int result = 1;

        for (long x = 2; x * x <= n; x++) {
            if (n % x == 0) {
                result = (int) x;
                if (n / x <= 10000000) {
                    return (int) (n / x);
                }
            }
        }

        return result;
    }

    public int[] solution(long begin, long end) {
        int size = (int) (end - begin + 1);
        int[] answer = new int[size];

        for (long n = begin; n <= end; n++) {
            answer[(int) (n - begin)] = find(n);
        }

        return answer;
    }
}