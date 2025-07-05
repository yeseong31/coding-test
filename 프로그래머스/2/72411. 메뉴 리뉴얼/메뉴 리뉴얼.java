import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Solution {
    private final Map<String, Integer> combinations = new HashMap<>();
    
    private void saveCombinations(int seq, StringBuilder sb, String order) {
        if (seq == order.length()) {
            if (sb.length() >= 2) {
                String key = sb.toString();
                combinations.put(key, combinations.getOrDefault(key, 0) + 1);
            }
            return;
        }
        
        sb.append(order.charAt(seq));
        saveCombinations(seq + 1, sb, order);
        
        sb.deleteCharAt(sb.length() - 1);
        saveCombinations(seq + 1, sb, order);
    }
    
    public String[] solution(String[] orders, int[] course) {
        List<String> answer = new ArrayList<>();
        Map<Integer, Integer> maxCountMap = new HashMap<>();
        Map<Integer, List<String>> resultMap = new HashMap<>();
        
        for (String order : orders) {
            String key = order.chars()
                    .boxed()
                    .sorted((v1, v2) -> v1 - v2)
                    .collect(StringBuilder::new,
                             StringBuilder::appendCodePoint,
                             StringBuilder::append)
                    .toString();
            saveCombinations(0, new StringBuilder(), key);
        }
        
        for (Map.Entry<String, Integer> entry : combinations.entrySet()) {
            String combination = entry.getKey();
            int count = entry.getValue();
            int number = combination.length();
            
            if (count <= 1) {
                continue;
            }
            
            int currentMax = maxCountMap.getOrDefault(number, 0);
            
            if (count > currentMax) {
                maxCountMap.put(number, count);
                List<String> list = new ArrayList<>();
                list.add(combination);
                resultMap.put(number, list);
            } else if (count == currentMax) {
                resultMap.get(number).add(combination);
            }
        }
        
        for (int seq : course) {
            if (resultMap.containsKey(seq)) {
                List<String> target = resultMap.get(seq);
                answer.addAll(target);
            }
        }
        
        return answer.stream()
                .sorted()
                .toArray(String[]::new);
    }
}