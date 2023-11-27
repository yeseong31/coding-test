import java.util.*;
import java.util.function.Consumer;


class Solution {
    public int[] solution(String[] info, String[] query) {
        int[] answer = new int[query.length];
        Map<String, List<Integer>> scoresMap = buildScoresMap(info);
        
        for (int index = 0; index < answer.length; index++) {
            answer[index] = count(query[index], scoresMap);
        }
        
        return answer;
    }
    
    private int count(String query, Map<String, List<Integer>> scoresMap) {
        String[] tokens = query.split(" (and )?");
        String key = String.join("", Arrays.copyOf(tokens, tokens.length - 1));
        
        if (!scoresMap.containsKey(key)) {
            return 0;
        }
        
        List<Integer> scores = scoresMap.get(key);
        int score = Integer.parseInt(tokens[tokens.length - 1]);
        
        return scores.size() - binarySearch(score, scoresMap.get(key));
    }
    
    private int binarySearch(int score, List<Integer> scores) {
        int start = 0;
        int end = scores.size() - 1;
        
        while (start < end) {
            int mid = (start + end) / 2;
            
            if (scores.get(mid) >= score) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        
        if (scores.get(start) < score) {
            return scores.size();
        }
        return start;
    }
    
    private Map<String, List<Integer>> buildScoresMap(String[] info) {
        Map<String, List<Integer>> scoresMap = new HashMap<>();

        for (String people : info) {
            String[] tokens = people.split(" ");
            int score = Integer.parseInt(tokens[tokens.length - 1]);
            
            forEachKey(0, "", tokens, key -> {
                scoresMap.putIfAbsent(key, new ArrayList<>());
                scoresMap.get(key).add(score);
            });
            
        }
        
        for (List<Integer> scores : scoresMap.values()) {
            Collections.sort(scores);
        }
        
        return scoresMap;
    }
    
    private void forEachKey(int index, String prefix, String[] tokens, Consumer<String> actions) {
        if (index == tokens.length - 1) {
            actions.accept(prefix);
            return;
        }
        
        forEachKey(index + 1, prefix + tokens[index], tokens, actions);
        forEachKey(index + 1, prefix + "-", tokens, actions);
    }
}