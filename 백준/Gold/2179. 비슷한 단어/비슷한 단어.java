import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        Word[] words = new Word[n];
        for (int i = 0; i < n; i++) {
            words[i] = new Word(br.readLine(), i);
        }

        Arrays.sort(words);

        String[] answer = solution(n, words);
        System.out.println(answer[0] + "\n" + answer[1]);
    }

    private static String[] solution(int n, Word[] words) {
        String[] answer = new String[2];

        int maxLength = -1;
        Word answer1 = null;
        Word answer2 = null;

        for (int i = 0; i < n - 1; i++) {
            Word base = words[i];

            for (int j = i + 1; j < n; j++) {
                Word candidate = words[j];

                int prefixLength = getPrefixLength(base.word, candidate.word);
                if (prefixLength == 0) {
                    break;
                }

                if (prefixLength > maxLength || answer1 == null ||
                        (prefixLength == maxLength && isHigherPriorityWord(base, candidate, answer1, answer2))) {

                    maxLength = prefixLength;
                    if (base.idx < candidate.idx) {
                        answer1 = base;
                        answer2 = candidate;
                    } else {
                        answer1 = candidate;
                        answer2 = base;
                    }
                }
                if (prefixLength < maxLength) {
                    break;
                }
            }
        }

        assert answer1 != null;
        answer[0] = answer1.word;
        answer[1] = answer2.word;

        return answer;
    }

    private static boolean isHigherPriorityWord(Word w1, Word w2, Word a1, Word a2) {
        int min1 = Math.min(w1.idx, w2.idx);
        int min2 = Math.min(a1.idx, a2.idx);
        if (min1 != min2) {
            return min1 < min2;
        }
        int max1 = Math.max(w1.idx, w2.idx);
        int max2 = Math.max(a1.idx, a2.idx);
        return max1 < max2;
    }

    private static int getPrefixLength(String w1, String w2) {
        int length = Math.min(w1.length(), w2.length());
        for (int i = 0; i < length; i++) {
            if (w1.charAt(i) != w2.charAt(i)) {
                return i;
            }
        }
        return length;
    }

    private static class Word implements Comparable<Word> {
        final String word;
        final int idx;

        public Word(String word, int idx) {
            this.word = word;
            this.idx = idx;
        }

        @Override
        public int compareTo(Word other) {
            return this.word.compareTo(other.word);
        }
    }
}