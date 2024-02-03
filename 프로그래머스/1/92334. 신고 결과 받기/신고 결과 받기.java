import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

class Solution {
    
    public int[] solution(String[] id_list, String[] report, int k) {
        Map<String, Integer> count = new HashMap<>();
        List<String> reports = Arrays.stream(report)
            .distinct()
            .collect(Collectors.toList());
        
        for (String r : reports) {
            String target = r.split(" ")[1];
            count.put(target, count.getOrDefault(target, 0) + 1);
        }
        
        return Arrays.stream(id_list)
            .map(user -> select(user, k, count, reports))
            .mapToInt(Long::intValue)
            .toArray();
    }
    
    private long select(String user, int k, Map<String, Integer> count, List<String> reports) {
        List<String> documents = reports.stream()
                .filter(s -> s.startsWith(user + " "))
                .collect(Collectors.toList());
        
        return documents.stream()
            .filter(s -> count.getOrDefault(s.split(" ")[1], 0) >= k)
            .count();
    }
}