import java.util.stream.IntStream;

class Solution {
    
    private static final int[][] PERSONS = {
        {1, 2, 3, 4, 5},
        {2, 1, 2, 3, 2, 4, 2, 5},
        {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
    };
    
    public int[] solution(int[] answers) {
        int[] scores = new int[3];
        int maxScore = -1;
        
        for (int i = 0; i < answers.length; i++) {
            for (int j = 0; j < PERSONS.length; j++) {
                if (PERSONS[j][i % PERSONS[j].length] == answers[i]) {
                    scores[j]++;
                    maxScore = Math.max(maxScore, scores[j]);
                }
            }
        }
        
        int finalMaxScore = maxScore;
        return IntStream.range(0, 3)
                .filter(i -> scores[i] == finalMaxScore)
                .map(i -> i + 1)
                .toArray();
    }
}
