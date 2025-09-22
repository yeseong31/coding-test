import java.util.*;

class Solution {

    private static final List<Integer> toSolve = new ArrayList<>();
    private static final List<Integer> candidates = new ArrayList<>();

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

        int maxDigit = -1;

        for (int i = 0; i < n; i++) {
            String[] tokens = expressions[i].split(" ");

            nums1[i] = Integer.parseInt(tokens[0]);
            nums2[i] = Integer.parseInt(tokens[2]);
            results[i] = (!tokens[4].equals("X")) ? Integer.parseInt(tokens[4]) : -1;
            ops[i] = tokens[1].charAt(0);

            maxDigit = Math.max(maxDigit, getMaxNum(nums1[i], nums2[i], results[i]));

            if (results[i] == -1) toSolve.add(i);
        }

        for (int k = maxDigit + 1; k <= 9; k++) {
            boolean matchAll = true;

            for (int i = 0; i < n; i++) {
                if (!toSolve.contains(i) && calculate(i, k) != results[i]) {
                    matchAll = false;
                    break;
                }
            }

            if (matchAll) candidates.add(k);
        }

        for (int i = 0; i < n; i++) {
            if (!toSolve.contains(i)) continue;

            int res = -1;
            boolean matchAll = true;

            for (int k : candidates) {
                int tmp = calculate(i, k);

                if (res == -1) {
                    res = tmp;
                } else if (res != tmp) {
                    matchAll = false;
                    break;
                }
            }

            if (matchAll) results[i] = res;
        }

        return toSolve.stream()
                .map(i ->
                        String.format("%d %c %d = %s",
                                nums1[i], ops[i], nums2[i],
                                (results[i] != -1) ? results[i] : "?"))
                .toArray(String[]::new);
    }

    private static int getMaxNum(int a, int b, int res) {
        int max1 = Math.max(a / 10, a % 10);
        int max2 = Math.max(b / 10, b % 10);
        int max3 = (res != -1) ? Math.max((res % 100) / 10, res % 10) : -1;

        return Math.max(max1, Math.max(max2, max3));
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