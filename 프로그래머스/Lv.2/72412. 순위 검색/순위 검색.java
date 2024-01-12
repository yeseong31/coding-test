import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] solution(String[] info, String[] query) {
        List<Integer> answer = new ArrayList<>();
        
        Map<String, List<Integer>> scores = buildScores(info);
        
        for (List<Integer> target : scores.values()) {
            Collections.sort(target);
        }
        
        for (String q : query) {
            String[] tokens = q.split(" (and)?");
            
            String key = String.join("", Arrays.copyOf(tokens, tokens.length - 1));
            int score = Integer.parseInt(tokens[tokens.length - 1]);
            
            answer.add(receiveScore(key, score, scores));
        }
        
        return answer.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
    
    private int receiveScore(String key, int score, Map<String, List<Integer>> scores) {
        if (!scores.containsKey(key)) {
            return 0;
        }
        
        return scores.get(key).size() - binarySearch(score, scores.get(key));
    }
    
    private int binarySearch(int score, List<Integer> target) {
        int start = 0;
        int end = target.size() - 1;
        
        while (start < end) {
            int mid = (start + end) / 2;
            
            if (score <= target.get(mid)) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        
        if (target.get(start) < score) {
            return target.size();
        }
        return start;
    }
    
    private Map<String, List<Integer>> buildScores(String[] info) {
        Map<String, List<Integer>> result = new HashMap<>();
        
        for (String condition : info) {
            String[] splitted = condition.split(" ");
            int score = Integer.parseInt(splitted[splitted.length - 1]);
            
            for (String key : buildKeys(splitted)) {
                result.putIfAbsent(key, new ArrayList<>());
                result.get(key).add(score);
            }
        }
        
        return result;
    }
    
    private List<String> buildKeys(String[] splitted) {
        List<String> keys = new ArrayList<>();
        dfs(0, "", splitted, keys);
        return keys;
    }
    
    private void dfs(int index, String currentKey, String[] splitted, List<String> keys) {
        if (index == splitted.length - 1) {
            keys.add(currentKey);
            return;
        }
        
        dfs(index + 1, currentKey + splitted[index], splitted, keys);
        dfs(index + 1, currentKey + "-", splitted, keys);
    }
}