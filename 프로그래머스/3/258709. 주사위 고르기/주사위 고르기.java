import java.util.ArrayList;
import java.util.List;

class Solution {

    private static int[][] inputDices;
    private static int n;
    private static int fullmask;

    public int[] solution(int[][] dice) {
        inputDices = dice;
        n = dice.length;
        fullmask = (1 << n) - 1;

        List<int[]> list = new ArrayList<>();

        for (int i = 0; i < (1 << n); i++) {
            if (Integer.bitCount(i) == n / 2) {
                list.add(new int[]{i, fight(i)});
            }
        }

        int[] bestCase = list.get(0);
        for (int[] target : list) {
            if (target[1] > bestCase[1]) {
                bestCase = target;
            }
        }

        int[] answer = new int[n / 2];
        int mask = bestCase[0];

        for (int i = 0, idx = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                answer[idx++] = i + 1;
            }
        }

        return answer;
    }

    private int fight(int mask) {
        int result = 0;
        int a = mask;
        int b = ~mask & fullmask;

        int[] sumA = getAllSums(a);
        int[] sumB = getAllSums(b);

        for (int sum = 1; sum < sumB.length; sum++) {
            sumB[sum] += sumB[sum - 1];
        }

        int bMax = sumB.length - 1;
        
        for (int sum = 3; sum < sumA.length; sum++) {
            int scoreB = sumB[Math.min(sum - 1, bMax)];
            result += scoreB * sumA[sum];
        }

        return result;
    }

    private int[] getAllSums(int mask) {
        int maxSum = getMaxSum(mask);
        int[] dp = new int[maxSum + 1];
        dp[0] = 1;

        for (int i = 0; i <= n; i++) {
            if ((mask & (1 << i)) == 0) continue;

            int[] next = new int[maxSum + 1];

            for (int sum = 0; sum <= maxSum; sum++) {
                if (dp[sum] == 0) continue;
                for (int face : inputDices[i]) {
                    next[sum + face] += dp[sum];
                }
            }
            dp = next;
        }

        return dp;
    }

    private int getMaxSum(int mask) {
        int sum = 0;
        int i = 0;

        for (int[] dice : inputDices) {
            if ((mask & (1 << i++)) == 0) continue;
            int max = 0;

            for (int d : dice) {
                max = Math.max(max, d);
            }
            sum += max;
        }

        return sum;
    }
}