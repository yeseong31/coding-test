import java.util.*;

class Solution {

    private static final List<Integer> toSolve = new ArrayList<>();
    private static final Set<Integer> possibleSysNums = new HashSet<>();

    private static int[][] nums;
    private static char[] ops;
    private static boolean[] isValid;

    public static String[] solution(String[] expressions) {
        int n = expressions.length;

        nums = new int[n][3];
        ops = new char[n];
        isValid = new boolean[n];

        int maxDigit = -1;

        for (int idx = 0; idx < n; idx++) {
            String[] tokens = expressions[idx].split(" ");
            
            int num1 = Integer.parseInt(tokens[0]);
            int num2 = Integer.parseInt(tokens[2]);
            int res = (!tokens[4].equals("X")) ? Integer.parseInt(tokens[4]) : -1;
            char op = tokens[1].charAt(0);

            nums[idx][0] = num1;
            nums[idx][1] = num2;
            nums[idx][2] = res;
            ops[idx] = op;

            maxDigit = Math.max(maxDigit, getMaxNum(num1, num2, res));

            if (res != -1) {
                isValid[idx] = true;
            } else {
                toSolve.add(idx);
            }
        }

        for (int sysNum = maxDigit + 1; sysNum <= 9; sysNum++) {
            boolean matchAll = true;

            for (int idx = 0; idx < n; idx++) {
                if (!isValid[idx]) continue;

                int res = calculate(idx, sysNum);

                if (res != nums[idx][2]) {
                    matchAll = false;
                    break;
                }
            }

            if (matchAll) possibleSysNums.add(sysNum);
        }

        for (int idx = 0; idx < n; idx++) {
            if (isValid[idx]) continue;

            int res = -1;
            boolean matchAll = true;

            for (int sysNum : possibleSysNums) {
                int tmp = calculate(idx, sysNum);

                if (res == -1) {
                    res = tmp;
                } else if (res != tmp) {
                    matchAll = false;
                    break;
                }
            }

            if (matchAll) nums[idx][2] = res;
        }

        return toSolve.stream()
                .map(Solution::getExp)
                .toArray(String[]::new);
    }

    private static String getExp(int idx) {
        int num1 = nums[idx][0];
        int num2 = nums[idx][1];
        int res = nums[idx][2];
        char op = ops[idx];
        return num1 + " " + op + " " + num2 + " = " + (res != -1 ? res : "?");
    }

    private static int getMaxNum(int num1, int num2, int res) {
        int max1 = Math.max(num1 / 10, num1 % 10);
        int max2 = Math.max(num2 / 10, num2 % 10);
        int max3 = (res != -1) ? Math.max((res % 100) / 10, res % 10) : -1;

        return Math.max(max1, Math.max(max2, max3));
    }

    private static int calculate(int idx, int sysNum) {
        int num1 = convertToDecimal(nums[idx][0], sysNum);
        int num2 = convertToDecimal(nums[idx][1], sysNum);

        int res = (ops[idx] == '+') ? num1 + num2 : num1 - num2;

        return convertFromDecimal(res, sysNum);
    }

    private static int convertToDecimal(int num, int sysNum) {
        int res = 0;
        int pow = 1;

        while (num > 0) {
            int digit = num % 10;
            res += digit * pow;
            pow *= sysNum;
            num /= 10;
        }

        return res;
    }

    private static int convertFromDecimal(int num, int sysNum) {
        int res = 0;
        int pow = 1;

        while (num > 0) {
            res += (num % sysNum) * pow;
            num /= sysNum;
            pow *= 10;
        }

        return res;
    }
}