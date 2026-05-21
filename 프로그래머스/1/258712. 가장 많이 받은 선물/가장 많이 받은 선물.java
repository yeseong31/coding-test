import java.util.*;

class Solution {

    public int solution(String[] friends, String[] gifts) {
        int n = friends.length;
        Map<String, Integer> nameToIndex = new HashMap<>();
        for (int i = 0; i < n; i++) {
            nameToIndex.put(friends[i], i);
        }

        int[][] giftGraph = new int[n][n];
        int[] giftScore = new int[n];

        for (String gift : gifts) {
            String[] participants = gift.split(" ");
            int giver = nameToIndex.get(participants[0]);
            int receiver = nameToIndex.get(participants[1]);
            
            giftGraph[giver][receiver]++;
            giftScore[giver]++;
            giftScore[receiver]--;
        }

        int[] nextMonthGifts = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int iToJ = giftGraph[i][j];
                int jToI = giftGraph[j][i];

                if (iToJ > jToI) {
                    nextMonthGifts[i]++;
                } else if (iToJ < jToI) {
                    nextMonthGifts[j]++;
                } else {
                    if (giftScore[i] > giftScore[j]) {
                        nextMonthGifts[i]++;
                    } else if (giftScore[i] < giftScore[j]) {
                        nextMonthGifts[j]++;
                    }
                }
            }
        }

        return Arrays.stream(nextMonthGifts).max().orElse(0);
    }
}