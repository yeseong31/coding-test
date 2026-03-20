import java.util.HashSet;
import java.util.Set;

public class Solution {

    public int solution(String message, int[][] spoiler_ranges) {
        Set<String> spoilerWords = new HashSet<>();
        Set<String> normalWords = new HashSet<>();

        boolean[] isSpoiler = new boolean[message.length()];
        for (int i = 0; i < spoiler_ranges.length; i++) {
            for (int j = spoiler_ranges[i][0]; j <= spoiler_ranges[i][1]; j++) {
                isSpoiler[j] = true;
            }
        }

        StringBuilder sb = new StringBuilder();
        boolean flag = false;

        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);

            if (c == ' ') {
                if (sb.length() > 0) {
                    String word = sb.toString();
                    if (flag && !normalWords.contains(word)) {
                        spoilerWords.add(word);
                    } else {
                        normalWords.add(word);
                    }
                    sb.setLength(0);
                    flag = false;
                }
            } else {
                sb.append(c);
                if (isSpoiler[i]) {
                    flag = true;
                }
            }
        }

        if (sb.length() > 0) {
            String word = sb.toString();
            if (flag && !normalWords.contains(word)) {
                spoilerWords.add(word);
            } else {
                normalWords.add(word);
            }
        }

        int answer = 0;
        for (String word : spoilerWords) {
            if (!normalWords.contains(word)) {
                answer++;
            }
        }

        return answer;
    }
}