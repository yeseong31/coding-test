public class Solution {
    public static int solution(int n) {
        int cnt = 0;

        for (int i = n; i > 0; i--) {
            int target = n;
            int j = i;

            while (target > 0 && j > 0) {
                target -= j;
                j--;
            }

            if (target == 0) cnt++;
        }

        return cnt;
    }
}