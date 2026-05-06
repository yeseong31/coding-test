import java.util.*;

class Solution {
    
    public int[] solution(String[] id_list, String[] report, int k) {
        Set<String> reportSet = new HashSet<>(Arrays.asList(report));
        Map<String, Set<String>> sanctions = new HashMap<>();

        for (String rep : reportSet) {
            String[] split = rep.split(" ");
            String from = split[0];
            String to = split[1];
            
            sanctions.putIfAbsent(to, new HashSet<>());
            sanctions.get(to).add(from);
        }

        Map<String, Integer> mailCount = new HashMap<>();
        for (String target : sanctions.keySet()) {
            Set<String> reporters = sanctions.get(target);
            if (reporters.size() >= k) {
                for (String reporter : reporters) {
                    mailCount.put(reporter, mailCount.getOrDefault(reporter, 0) + 1);
                }
            }
        }

        int[] answer = new int[id_list.length];
        for (int i = 0; i < id_list.length; i++) {
            answer[i] = mailCount.getOrDefault(id_list[i], 0);
        }

        return answer;
    }
}