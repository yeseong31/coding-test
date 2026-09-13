import java.util.ArrayDeque;
import java.util.Queue;

public class Solution {

    public int solution(String begin, String target, String[] words) {
        boolean[] visited = new boolean[words.length];
        Queue<String> queue = new ArrayDeque<>();

        queue.offer(begin);

        int count = 0;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();

            for (int i = 0; i < levelSize; i++) {
                String current = queue.poll();

                if (current.equals(target)) {
                    return count;
                }

                for (int j = 0; j < words.length; j++) {
                    if (!visited[j] && canConvert(current, words[j])) {
                        visited[j] = true;
                        queue.offer(words[j]);
                    }
                }
            }

            count++;
        }

        return 0;
    }

    private boolean canConvert(String first, String second) {
        int difference = 0;

        for (int i = 0; i < first.length(); i++) {
            if (first.charAt(i) != second.charAt(i)) {
                difference++;

                if (difference > 1) {
                    return false;
                }
            }
        }

        return difference == 1;
    }
}