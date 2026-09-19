import java.util.*;

class Solution {
    
    public int[] solution(String s) {
        String[] groups = s.substring(2, s.length() - 2)
                           .split("\\},\\{");

        Arrays.sort(groups, Comparator.comparingInt(
                group -> group.split(",").length
        ));

        Set<Integer> seen = new HashSet<>();
        List<Integer> answer = new ArrayList<>();

        for (String group : groups) {
            for (String value : group.split(",")) {
                int number = Integer.parseInt(value);

                if (seen.add(number)) {
                    answer.add(number);
                }
            }
        }

        return answer.stream()
                     .mapToInt(Integer::intValue)
                     .toArray();
    }
}