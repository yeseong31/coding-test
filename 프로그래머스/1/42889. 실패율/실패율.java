import java.util.*;

class Solution {
    
    public int[] solution(int N, int[] stages) {
        List<double[]> result = new ArrayList<>();
        int length = stages.length;

        for (int i = 1; i <= N; i++) {
            int cnt = 0;
            for (int stage : stages) {
                if (stage == i) cnt++;
            }

            if (length > 0) {
                result.add(new double[]{i, (double) cnt / length});
            } else {
                result.add(new double[]{i, 0});
            }

            length -= cnt;
        }

        result.sort((a, b) -> Double.compare(b[1], a[1]));

        int[] answer = new int[N];
        for (int i = 0; i < N; i++) {
            answer[i] = (int) result.get(i)[0];
        }

        return answer;
    }
}