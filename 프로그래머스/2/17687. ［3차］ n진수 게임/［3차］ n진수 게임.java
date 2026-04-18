import java.util.ArrayList;
import java.util.List;

class Solution {
    
    public String solution(int n, int t, int m, int p) {
        StringBuilder answer = new StringBuilder();

        List<Integer> list = new ArrayList<>();
        list.add(0);

        int num = 1;
        while (list.size() < t * m) {
            list.addAll(change(num, n));
            num++;
        }

        int idx = p - 1;
        for (int i = 0; i < t; i++) {
            int target = list.get(idx);

            if (target >= 10) {
                answer.append((char) ('A' + (target - 10)));
            } else {
                answer.append(target);
            }

            idx += m;
        }

        return answer.toString();
    }

    private List<Integer> change(int x, int n) {
        List<Integer> result = new ArrayList<>();

        if (x == 0) {
            result.add(0);
            return result;
        }

        while (x > 0) {
            result.add(0, x % n);
            x /= n;
        }

        return result;
    }
}