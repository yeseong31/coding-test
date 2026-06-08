import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(String dartResult) {
        List<Integer> answer = new ArrayList<>();
        answer.add(0);

        int len = dartResult.length();
        for (int i = 0; i < len; i++) {
            char c = dartResult.charAt(i);

            if (Character.isDigit(c)) {
                int lastIdx = answer.size() - 1;
                answer.set(lastIdx, answer.get(lastIdx) * 10 + (c - '0'));
            } else if (c == 'S' || c == 'D' || c == 'T') {
                int lastIdx = answer.size() - 1;
                int currentScore = answer.get(lastIdx);
                
                if (c == 'D') {
                    currentScore = currentScore * currentScore;
                } else if (c == 'T') {
                    currentScore = currentScore * currentScore * currentScore;
                }
                
                answer.set(lastIdx, currentScore);
                answer.add(0);
            } else if (c == '*') {
                int size = answer.size();
                answer.set(size - 2, answer.get(size - 2) * 2);
                if (size > 2) {
                    answer.set(size - 3, answer.get(size - 3) * 2);
                }
            } else if (c == '#') {
                int size = answer.size();
                answer.set(size - 2, answer.get(size - 2) * -1);
            }
        }

        int sum = 0;
        for (int score : answer) {
            sum += score;
        }
        return sum;
    }
}