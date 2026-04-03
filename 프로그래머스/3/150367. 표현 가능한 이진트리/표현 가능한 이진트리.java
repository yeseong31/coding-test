import java.util.*;

public class Solution {

    public static Object dfs(int start, int end, String tree) {
        if (start >= end) {
            return tree.charAt(start);
        }

        int mid = (start + end) / 2;

        Object left = dfs(start, mid - 1, tree);
        Object right = dfs(mid + 1, end, tree);

        if (left.equals(false) || (left.equals('1') && tree.charAt(mid) == '0')) {
            return false;
        }

        if (right.equals(false) || (right.equals('1') && tree.charAt(mid) == '0')) {
            return false;
        }

        if (left.equals('0') && right.equals('0') && tree.charAt(mid) == '0') {
            return '0';
        }

        return '1';
    }

    public static String convertToFullBinaryTree(String binaryN) {
        int value = 1;

        while ((int)Math.pow(2, value) - 1 < binaryN.length()) {
            value++;
        }

        int targetLength = (int)Math.pow(2, value) - 1;

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < targetLength - binaryN.length(); i++) {
            sb.append('0');
        }
        sb.append(binaryN);

        return sb.toString();
    }

    public static int[] solution(long[] numbers) {
        int[] answer = new int[numbers.length];

        for (int i = 0; i < numbers.length; i++) {
            long n = numbers[i];

            String binaryN = Long.toBinaryString(n);
            String tree = convertToFullBinaryTree(binaryN);

            Object result = dfs(0, tree.length() - 1, tree);
            answer[i] = result.equals(false) ? 0 : 1;
        }

        return answer;
    }
}