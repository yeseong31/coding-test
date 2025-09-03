import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int t = 1; t <= T; t++) {
            int dayPrice = sc.nextInt();
            int monthPrice = sc.nextInt();
            int quarterPrice = sc.nextInt();
            int yearPrice = sc.nextInt();

            int[] plan = new int[12];
            for (int i = 0; i < 12; i++) {
                plan[i] = sc.nextInt();
            }

            int[] dp = new int[13];

            for (int i = 1; i <= 12; i++) {
                dp[i] = yearPrice;

                if (plan[i - 1] == 0) {
                    dp[i] = Math.min(dp[i], dp[i - 1]);
                } else {
                    int option = dp[i - 1] + plan[i - 1] * dayPrice;
                    dp[i] = Math.min(dp[i], option);

                    int monthOption = dp[i - 1] + monthPrice;
                    dp[i] = Math.min(dp[i], monthOption);
                }

                if (i >= 3) {
                    int quarterOption = dp[i - 3] + quarterPrice;
                    dp[i] = Math.min(dp[i], quarterOption);
                }
            }

            System.out.println("#" + t + " " + dp[12]);
        }

        sc.close();
    }
}