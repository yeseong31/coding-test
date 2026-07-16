import java.util.*;

class Solution {

    private Map<String, PriorityQueue<String>> graph;
    private List<String> result;

    public String[] solution(String[][] tickets) {
        graph = new HashMap<>();
        result = new ArrayList<>();

        for (String[] ticket : tickets) {
            graph.computeIfAbsent(ticket[0], k -> new PriorityQueue<>())
                 .offer(ticket[1]);
        }

        dfs("ICN");

        Collections.reverse(result);
        return result.toArray(new String[0]);
    }

    private void dfs(String now) {
        PriorityQueue<String> pq = graph.get(now);
        while (pq != null && !pq.isEmpty()) {
            dfs(pq.poll());
        }
        result.add(now);
    }
}