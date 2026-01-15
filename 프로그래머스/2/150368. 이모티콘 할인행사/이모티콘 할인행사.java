class Solution {

    private static final int[] DISCOUNT_OPTIONS = {10, 20, 30, 40};

    private static int[] emoticons;
    private static int[][] users;

    private static int maxSubscribers;
    private static int maxTotalPrice;

    public int[] solution(int[][] usersInput, int[] emoticonsInput) {
        users = usersInput;
        emoticons = emoticonsInput;
        maxSubscribers = 0;
        maxTotalPrice = 0;

        int[] discounts = new int[emoticons.length];
        dfs(0, discounts);

        return new int[]{maxSubscribers, maxTotalPrice};
    }

    private static void dfs(int depth, int[] discounts) {
        if (depth == emoticons.length) {
            evaluate(discounts);
            return;
        }

        for (int d : DISCOUNT_OPTIONS) {
            discounts[depth] = d;
            dfs(depth + 1, discounts);
        }
    }

    private static void evaluate(int[] discounts) {
        int subscribers = 0;
        int totalPrice = 0;

        for (int i = 0; i < users.length; i++) {
            int wantedRate = users[i][0];
            int limitPrice = users[i][1];
            int sum = 0;

            for (int j = 0; j < emoticons.length; j++) {
                if (discounts[j] >= wantedRate) {
                    sum += emoticons[j] * (100 - discounts[j]) / 100;
                }
                if (sum >= limitPrice) {
                    subscribers++;
                    sum = 0;
                    break;
                }
            }
            totalPrice += sum;
        }

        if (subscribers > maxSubscribers ||
            (subscribers == maxSubscribers && totalPrice > maxTotalPrice)) {
            maxSubscribers = subscribers;
            maxTotalPrice = totalPrice;
        }
    }
}