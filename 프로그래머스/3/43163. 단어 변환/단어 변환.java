import java.util.*;

public class Solution {
    
    public static int solution(String begin, String target, String[] words) {
        List<String> wordList = Arrays.asList(words);
        if (!wordList.contains(target)) {
            return 0;
        }

        Queue<String> queue = new LinkedList<>();
        Queue<Integer> countQueue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.offer(begin);
        countQueue.offer(0);
        visited.add(begin);

        while (!queue.isEmpty()) {
            String currentWord = queue.poll();
            int count = countQueue.poll();

            if (currentWord.equals(target)) {
                return count;
            }

            for (String word : words) {
                if (visited.contains(word)) {
                    continue;
                }
                if (diffCount(currentWord, word) == 1) {
                    queue.offer(word);
                    countQueue.offer(count + 1);
                    visited.add(word);
                }
            }
        }

        return 0;
    }

    private static int diffCount(String a, String b) {
        int diff = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                diff++;
            }
        }
        return diff;
    }
}