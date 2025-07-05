import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Solution {
    
    public int[] solution(String[] info, String[] query) {
        List<Integer> answer = new ArrayList<>();
        Map<String, List<Integer>> scores = new HashMap<>();
        
        for (String s : info) {
            String[] tokens = s.split(" ");
            int score = Integer.parseInt(tokens[4]);
            
            List<String> conditions = new ArrayList<>();
            record(0, new StringBuilder(), tokens, conditions);
            
            for (String key : conditions) {
                scores.computeIfAbsent(key, k -> new ArrayList<>());
                scores.get(key).add(score);
            }
        }
        
        for (List<Integer> value : scores.values()) {
            Collections.sort(value);
        }
        
        for (String q : query) {
            String[] tokens = q.replace(" and ", " ").split(" ");
            
            String key = String.join("", Arrays.copyOf(tokens, tokens.length - 1));
            if (!scores.containsKey(key)) {
                answer.add(0);
                continue;
            }
            
            List<Integer> sortedList = scores.get(key);
            int score = Integer.parseInt(tokens[tokens.length - 1]);
            
            int count = binarySearch(sortedList, score);
            answer.add(sortedList.size() - count);
        }
        
        return answer.stream()
                .mapToInt(Integer::new)
                .toArray();
    }
    
    private static int binarySearch(List<Integer> sortedList, int score) {
        int start = 0;
        int end = sortedList.size() - 1;
        
        while (start < end) {
            int mid = (start + end) / 2;
            int target = sortedList.get(mid);
            
            if (target < score) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        
        if (sortedList.get(start) < score) {
            return sortedList.size();
        }
        return start;
    }
    
    private static void record(int index, StringBuilder sb, String[] tokens, List<String> conditions) {
        if (index == tokens.length - 1) {
            if (sb.length() > 0) {
                String key = sb.toString();
                conditions.add(key);
            }
            return;
        }
        
        sb.append(tokens[index]);
        record(index + 1, sb, tokens, conditions);
        sb.delete(sb.length() - tokens[index].length(), sb.length());
        
        sb.append("-");
        record(index + 1, sb, tokens, conditions);
        sb.deleteCharAt(sb.length() - 1);
    }
}