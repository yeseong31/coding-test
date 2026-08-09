import java.util.*;
import java.util.regex.*;

class Solution {

    private static final Pattern URL_PATTERN  = Pattern.compile("<meta property[^>]+content=\"(https://[^\"]+)\"");
    private static final Pattern WORD_PATTERN = Pattern.compile("[a-z]+");
    private static final Pattern LINK_PATTERN = Pattern.compile("<a href=\"(https://[^\"]+)\"");

    public int solution(String word, String[] pages) {
        word = word.toLowerCase();

        int n = pages.length;
        String[] urls       = new String[n];
        int[]    scores     = new int[n];
        int[]    extCounts  = new int[n];
        Map<String, Integer> urlIndex = new HashMap<>();
        Map<String, List<Integer>> inbound = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String page = pages[i].toLowerCase();

            Matcher um = URL_PATTERN.matcher(page);
            if (!um.find()) continue;
            urls[i] = um.group(1);
            urlIndex.put(urls[i], i);

            Matcher wm = WORD_PATTERN.matcher(page);
            while (wm.find()) if (wm.group().equals(word)) scores[i]++;

            Matcher lm = LINK_PATTERN.matcher(page);
            while (lm.find()) {
                extCounts[i]++;
                inbound.computeIfAbsent(lm.group(1), k -> new ArrayList<>()).add(i);
            }
        }

        int answer = 0;
        double maxScore = -1;

        for (int i = 0; i < n; i++) {
            if (urls[i] == null) continue;
            double score = scores[i];
            for (int from : inbound.getOrDefault(urls[i], Collections.emptyList())) {
                if (extCounts[from] > 0) score += (double) scores[from] / extCounts[from];
            }
            if (score > maxScore) {
                maxScore = score;
                answer = i;
            }
        }

        return answer;
    }
}