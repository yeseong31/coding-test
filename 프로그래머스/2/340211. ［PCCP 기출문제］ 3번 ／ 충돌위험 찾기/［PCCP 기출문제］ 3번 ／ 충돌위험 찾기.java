import java.util.HashMap;
import java.util.Map;

class Solution {

    public int solution(int[][] points, int[][] routes) {
        int robotCount = routes.length;
        int[][] positions = new int[robotCount][2];
        int[] targets = new int[robotCount];
        boolean[] finished = new boolean[robotCount];

        for (int i = 0; i < robotCount; i++) {
            int[] start = points[routes[i][0] - 1];
            positions[i][0] = start[0];
            positions[i][1] = start[1];

            targets[i] = 1;
        }

        int answer = 0;
        int finishedCount = 0;

        while (finishedCount < robotCount) {

            Map<Integer, Integer> count = new HashMap<>();

            for (int i = 0; i < robotCount; i++) {
                if (finished[i]) {
                    continue;
                }

                int key = positions[i][0] * 101 + positions[i][1];
                count.put(key, count.getOrDefault(key, 0) + 1);
            }

            for (int value : count.values()) {
                if (value >= 2) {
                    answer++;
                }
            }

            for (int i = 0; i < robotCount; i++) {
                if (finished[i]) {
                    continue;
                }

                if (targets[i] == routes[i].length) {
                    finished[i] = true;
                    finishedCount++;
                    continue;
                }

                int[] target = points[routes[i][targets[i]] - 1];

                int r = positions[i][0];
                int c = positions[i][1];

                if (r != target[0]) {
                    positions[i][0] += r < target[0] ? 1 : -1;
                } else if (c != target[1]) {
                    positions[i][1] += c < target[1] ? 1 : -1;
                }

                if (positions[i][0] == target[0]
                        && positions[i][1] == target[1]) {
                    targets[i]++;
                }
            }
        }

        return answer;
    }
}