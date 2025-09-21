import java.util.*;

class Solution {

    public static String[] solution(String[] expressions) {
        int n = expressions.length;

        int[][] nums = new int[n][3];
        char[] ops = new char[n];
        boolean[] isValid = new boolean[n];

        List<Integer> toSolve = new ArrayList<>();
        int maxDigit = -1;

        for (int i = 0; i < n; i++) {
            String[] tokens = expressions[i].split(" ");
            nums[i][0] = Integer.parseInt(tokens[0]);
            nums[i][1] = Integer.parseInt(tokens[2]);
            nums[i][2] = (!tokens[4].equals("X")) ? Integer.parseInt(tokens[4]) : -1;
            ops[i] = tokens[1].charAt(0);

            int max1 = Math.max(nums[i][0] / 10, nums[i][0] % 10);
            int max2 = Math.max(nums[i][1] / 10, nums[i][1] % 10);
            int max3 = Math.max((nums[i][2] % 100) / 10, nums[i][2] % 10);

            maxDigit = Math.max(maxDigit, Math.max(max1, Math.max(max2, max3)));

            if (nums[i][2] != -1) {
                isValid[i] = true;
            } else {
                toSolve.add(i);
            }
        }

        Set<Integer> possibleSysNums = new HashSet<>();

        for (int sysNum = maxDigit + 1; sysNum <= 9; sysNum++) {
            boolean matchAll = true;

            for (int i = 0; i < n; i++) {
                if (!isValid[i]) continue;

                int res = calculate(nums[i][0], nums[i][1], ops[i], sysNum);

                if (res != nums[i][2]) {
                    matchAll = false;
                    break;
                }
            }

            if (matchAll) possibleSysNums.add(sysNum);
        }
        
        for (int i = 0; i < n; i++) {
            if (isValid[i]) continue;

            int res = -1;
            boolean matchAll = true;

            for (int sysNum : possibleSysNums) {
                int tmp = calculate(nums[i][0], nums[i][1], ops[i], sysNum);

                if (res == -1) {
                    res = tmp;
                    continue;
                }
                if (res != tmp) {
                    matchAll = false;
                    break;
                }
            }

            if (matchAll) nums[i][2] = res;
        }

        return toSolve.stream()
                .map(i -> {
                    int num1 = nums[i][0];
                    int num2 = nums[i][1];
                    int res = nums[i][2];
                    char op = ops[i];
                    return num1 + " " + op + " " + num2 + " = " + (res != -1 ? res : "?");
                })
                .toArray(String[]::new);
    }

    private static int calculate(int num1, int num2, char op, int sysNum) {
        num1 = convertToDecimal(num1, sysNum);
        num2 = convertToDecimal(num2, sysNum);

        int res = (op == '+') ? num1 + num2 : num1 - num2;

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