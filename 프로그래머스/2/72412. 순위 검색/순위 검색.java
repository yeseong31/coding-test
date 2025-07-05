import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private void getKeyCombinations(String[] tokens, int seq, String current, List<String> keyCombinations) {
        if (seq == tokens.length - 1) {
            if (current.length() > 0) {
                keyCombinations.add(current);
            }
            return;
        }
        
        getKeyCombinations(tokens, seq + 1, current + tokens[seq], keyCombinations);
        getKeyCombinations(tokens, seq + 1, current + "-", keyCombinations);
    }
    
    private int binarySearch(List<Integer> values, int score) {
        int left = 0;
        int right = values.size() - 1;
        
        while (left < right) {
            int mid = (left + right) / 2;
            
            if (values.get(mid) >= score) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        if (values.get(left) < score) {
            return values.size();
        }
        return left;
    }
    
    public int[] solution(String[] info, String[] query) {
        List<Integer> answer = new ArrayList<>();
        Map<String, List<Integer>> scores = new HashMap<>();
        
        for (String i : info) {
            String[] tokens = i.split(" ");
            int score = Integer.parseInt(tokens[tokens.length - 1]);
            
            List<String> keyCombinations = new ArrayList<>();
            getKeyCombinations(tokens, 0, new String(), keyCombinations);
            
            for (String key : keyCombinations) {
                scores.computeIfAbsent(key, k -> new ArrayList<>()).add(score);
            }
        }
        
        for (List<Integer> value : scores.values()) {
            Collections.sort(value);
        }

        for (String q : query) {
            String[] tokens = q.replaceAll(" and ", " ").split(" ");
            String key = String.join("", Arrays.copyOf(tokens, tokens.length - 1));
            
            if (!scores.containsKey(key)) {
                answer.add(0);
                continue;
            }
            
            List<Integer> values = scores.get(key);
            int score = Integer.parseInt(tokens[tokens.length - 1]);
            
            int result = binarySearch(values, score);
            answer.add(values.size() - result);
        }
        
        return answer.stream()
                .mapToInt(Integer::valueOf)
                .toArray();
    }
}