import java.util.HashSet;
import java.util.Set;

class Solution {

    public int[] solution(int n, String[] words) {
        Set<String> usedWords = new HashSet<>();
        char previousLastChar = '\0';

        for (int i = 0; i < words.length; i++) {
            String word = words[i];

            boolean disconnected =
                    i > 0 && previousLastChar != word.charAt(0);

            boolean duplicated = !usedWords.add(word);

            if (disconnected || duplicated) {
                int player = i % n + 1;
                int turn = i / n + 1;

                return new int[]{player, turn};
            }

            previousLastChar = word.charAt(word.length() - 1);
        }

        return new int[]{0, 0};
    }
}