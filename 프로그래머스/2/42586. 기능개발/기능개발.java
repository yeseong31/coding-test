import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int n = progresses.length;
        int[] days = new int[n];

        for (int i = 0; i < n; i++) {
            int remaining = 100 - progresses[i];
            days[i] = (remaining + speeds[i] - 1) / speeds[i];
        }

        List<Integer> answer = new ArrayList<>();

        int releaseDay = days[0];
        int count = 1;

        for (int i = 1; i < n; i++) {
            if (days[i] <= releaseDay) {
                count++;
            } else {
                answer.add(count);
                releaseDay = days[i];
                count = 1;
            }
        }

        answer.add(count);

        return answer.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}