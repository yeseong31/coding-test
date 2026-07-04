import java.util.*;

class Solution {
    private static int[] nums1;
    private static int[] nums2;
    private static int[] results;
    private static char[] ops;

    public static String[] solution(String[] expressions) {
        int n = expressions.length;
        nums1 = new int[n];
        nums2 = new int[n];
        results = new int[n];
        ops = new char[n];

        List<Integer> toSolve = new ArrayList<>();
        boolean[] isSolve = new boolean[n];
        List<Integer> candidates = new ArrayList<>();

        int maxDigit = -1;

        for (int i = 0; i < n; i++) {
            String[] tokens = expressions[i].split(" ");
            nums1[i] = Integer.parseInt(tokens[0]);
            nums2[i] = Integer.parseInt(tokens[2]);
            results[i] = tokens[4].equals("X") ? -1 : Integer.parseInt(tokens[4]);
            ops[i] = tokens[1].charAt(0);
            maxDigit = Math.max(maxDigit, getMaxDigit(nums1[i], nums2[i], results[i]));
            if (results[i] == -1) {
                toSolve.add(i);
                isSolve[i] = true;
            }
        }

        for (int k = maxDigit + 1; k <= 9; k++) {
            boolean valid = true;
            for (int i = 0; i < n; i++) {
                if (isSolve[i]) continue;
                if (calculate(i, k) != results[i]) {
                    valid = false;
                    break;
                }
            }
            if (valid) candidates.add(k);
        }

        for (int i : toSolve) {
            if (candidates.isEmpty()) continue;
            int res = calculate(i, candidates.get(0));
            boolean unique = true;
            for (int k : candidates) {
                if (calculate(i, k) != res) {
                    unique = false;
                    break;
                }
            }
            if (unique) results[i] = res;
        }

        return toSolve.stream()
                .map(i -> String.format("%d %c %d = %s",
                        nums1[i], ops[i], nums2[i],
                        results[i] != -1 ? results[i] : "?"))
                .toArray(String[]::new);
    }

    private static int getMaxDigit(int a, int b, int res) {
        int max = 0;
        max = Math.max(max, maxDigitOf(a));
        max = Math.max(max, maxDigitOf(b));
        if (res != -1) max = Math.max(max, maxDigitOf(res));
        return max;
    }

    private static int maxDigitOf(int x) {
        int max = 0;
        while (x > 0) {
            max = Math.max(max, x % 10);
            x /= 10;
        }
        return max;
    }

    private static int calculate(int i, int k) {
        int a = convertToDecimal(nums1[i], k);
        int b = convertToDecimal(nums2[i], k);
        int res = (ops[i] == '+') ? a + b : a - b;
        return convertFromDecimal(res, k);
    }

    private static int convertToDecimal(int x, int k) {
        int res = 0;
        int pow = 1;
        while (x > 0) {
            res += (x % 10) * pow;
            pow *= k;
            x /= 10;
        }
        return res;
    }

    private static int convertFromDecimal(int x, int k) {
        if (x < 0) return -convertFromDecimal(-x, k);
        if (x == 0) return 0;
        int res = 0;
        int pow = 1;
        while (x > 0) {
            res += (x % k) * pow;
            x /= k;
            pow *= 10;
        }
        return res;
    }
}