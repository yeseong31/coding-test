import java.util.*;

public class Solution {
    public static int solution(int[] arrayA, int[] arrayB) {
        int a = calculGcd(arrayA);
        int b = calculGcd(arrayB);

        List<Integer> answer = new ArrayList<>();

        if (check(arrayA, b)) {
            answer.add(b);
        }
        if (check(arrayB, a)) {
            answer.add(a);
        }

        if (answer.isEmpty()) {
            return 0;
        }
        return Collections.max(answer);
    }

    private static int calculGcd(int[] arr) {
        int result = 0;
        for (int i = 0; i < arr.length; i++) {
            result = (i == 0) ? arr[i] : gcd(result, arr[i]);
        }
        return result;
    }

    private static boolean check(int[] arr, int target) {
        for (int x : arr) {
            if (x % target == 0) {
                return false;
            }
        }
        return true;
    }

    private static int gcd(int x, int y) {
        return (y == 0) ? x : gcd(y, x % y);
    }

    public static void main(String[] args) {
        int[] arrayA = {2, 5, 10};
        int[] arrayB = {3, 5, 15};
        System.out.println(solution(arrayA, arrayB));
    }
}