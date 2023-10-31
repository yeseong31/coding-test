import java.util.stream.IntStream;


class Solution {
    
    private static final int[][] PERSONS = {{1, 2, 3, 4, 5}, {2, 1, 2, 3, 2, 4, 2, 5}, {3, 3, 1, 1, 2, 2 ,4, 4, 5, 5}};
    
    public int[] solution(int[] answers) {
        int[] scores = new int[3];
        int topScorerIndex = findTopScorerIndex(answers, scores);
        
        return IntStream.range(0, 3)
                .filter(i -> scores[i] == scores[topScorerIndex])
                .map(i -> i + 1)
                .toArray();
    }
    
    private int findTopScorerIndex(int[] answers, int[] scores) {
        int maxScorerIndex = 0;
        
        for (int i = 0; i < answers.length; i++) {
            for (int j = 0; j < PERSONS.length; j++) {
                if (answers[i] == getPicked(i, j)) {
                    if (scores[maxScorerIndex] < ++scores[j]) {
                        maxScorerIndex = j;
                    }
                }
            }
        }
        
        return maxScorerIndex;
    }
    
    private int getPicked(int seq, int index) {
        int personLength = PERSONS[index].length;
        return PERSONS[index][seq % personLength];
    }
}