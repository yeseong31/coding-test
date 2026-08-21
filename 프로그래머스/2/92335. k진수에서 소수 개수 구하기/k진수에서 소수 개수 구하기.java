import java.util.Arrays;

class Solution {

    public int solution(int n, int k) {
        String converted = Long.toString(n, k);

        return (int) Arrays.stream(converted.split("0+"))
                .filter(s -> !s.isEmpty())
                .mapToLong(Long::parseLong)
                .filter(Solution::isPrime)
                .count();
    }

    private static boolean isPrime(long n) {
        if (n < 2) return false;
        if (n < 4) return true;
        if (n % 2 == 0) return false;

        for (long i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}