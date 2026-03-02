import java.util.*;

class Solution {
    
    public int solution(String[] friends, String[] gifts) {
        int n = friends.length;
        Map<String, Integer> idx = new HashMap<>();
        for (int i = 0; i < n; i++) idx.put(friends[i], i);

        int[][] g = new int[n][n];
        for (String s : gifts) {
            String[] p = s.split(" ");
            int a = idx.get(p[0]);
            int b = idx.get(p[1]);
            g[a][b]++;
        }

        int[] giftIndex = new int[n];
        for (int i = 0; i < n; i++) {
            int give = 0;
            int recv = 0;
            for (int j = 0; j < n; j++) {
                give += g[i][j];
                recv += g[j][i];
            }
            giftIndex[i] = give - recv;
        }

        int[] receiveNext = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int ij = g[i][j];
                int ji = g[j][i];

                if (ij > ji) {
                    receiveNext[i]++;
                } else if (ij < ji) {
                    receiveNext[j]++;
                } else {
                    if (giftIndex[i] > giftIndex[j]) receiveNext[i]++;
                    else if (giftIndex[i] < giftIndex[j]) receiveNext[j]++;
                }
            }
        }

        int ans = 0;
        for (int x : receiveNext) ans = Math.max(ans, x);
        return ans;
    }
}