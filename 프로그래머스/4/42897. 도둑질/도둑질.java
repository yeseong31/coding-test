public class Solution {

    public int solution(int[] money) {
        int n = money.length;
        int firstIncluded = rob(money, 0, n - 2);
        int lastIncluded = rob(money, 1, n - 1);

        return Math.max(firstIncluded, lastIncluded);
    }

    private int rob(int[] money, int start, int end) {
        int twoBack = 0;
        int oneBack = 0;

        for (int i = start; i <= end; i++) {
            int current = Math.max(oneBack, twoBack + money[i]);
            twoBack = oneBack;
            oneBack = current;
        }

        return oneBack;
    }
}