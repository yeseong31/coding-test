import java.util.*;
import java.util.stream.*;

class Solution {
    
    private static final int[][] persons = {
        {1, 2, 3, 4, 5},
        {2, 1, 2, 3, 2, 4, 2, 5},
        {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
    };

    public int[] solution(int[] answers) {

        int[] count = IntStream.range(0, persons.length)
            .map(i -> (int) IntStream.range(0, answers.length)
                .filter(j -> persons[i][j % persons[i].length] == answers[j])
                .count())
            .toArray();

        int max = Arrays.stream(count).max().getAsInt();

        return IntStream.range(0, count.length)
            .filter(i -> count[i] == max)
            .map(i -> i + 1)
            .toArray();
    }
}