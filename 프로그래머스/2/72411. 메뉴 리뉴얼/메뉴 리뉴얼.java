import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    
    private Map<String, Integer> combinationMap;

    public String[] solution(String[] orders, int[] course) {
        List<String> answer = new ArrayList<>();

        for (int size : course) {
            combinationMap = new HashMap<>();
            int maxCount = 0;

            for (String order : orders) {
                char[] chars = order.toCharArray();
                Arrays.sort(chars);
                generateCombinations(chars, 0, size, new StringBuilder());
            }

            for (int count : combinationMap.values()) {
                maxCount = Math.max(maxCount, count);
            }

            if (maxCount < 2) {
                continue;
            }

            for (Map.Entry<String, Integer> entry : combinationMap.entrySet()) {
                if (entry.getValue() == maxCount) {
                    answer.add(entry.getKey());
                }
            }
        }

        Collections.sort(answer);
        return answer.toArray(new String[0]);
    }

    private void generateCombinations(char[] chars, int index, int targetSize, StringBuilder current) {
        if (current.length() == targetSize) {
            String key = current.toString();
            combinationMap.put(key, combinationMap.getOrDefault(key, 0) + 1);
            return;
        }

        if (index == chars.length) {
            return;
        }

        current.append(chars[index]);
        generateCombinations(chars, index + 1, targetSize, current);
        current.deleteCharAt(current.length() - 1);

        generateCombinations(chars, index + 1, targetSize, current);
    }
}