import java.util.HashMap;
import java.util.Map;

class Solution {
    
    public int solution(int[] a) {
        int answer = -1;

        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : a) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }

        for (int k : counter.keySet()) {
            if (counter.get(k) <= answer) continue;

            int cnt = 0;
            int i = 0;

            while (i < a.length - 1) {
                if (a[i] == a[i + 1] || (a[i] != k && a[i + 1] != k)) {
                    i += 1;
                } else {
                    i += 2;
                    cnt += 1;
                }
            }

            answer = Math.max(answer, cnt);
        }

        return answer < 0 ? -1 : answer * 2;
    }
}