import java.util.*;

class Solution {
    
    public int solution(int[] cards) {
        List<Integer> groups = new ArrayList<>();
        boolean[] visited = new boolean[cards.length];

        for (int i = 0; i < cards.length; i++) {
            if (visited[i]) continue;

            visited[i] = true;
            int count = 1;
            int next = i;

            while (!visited[cards[next] - 1]) {
                next = cards[next] - 1;
                visited[next] = true;
                count++;
            }

            groups.add(count);
        }

        if (groups.size() < 2) return 0;

        Collections.sort(groups, Collections.reverseOrder());
        return groups.get(0) * groups.get(1);
    }
}