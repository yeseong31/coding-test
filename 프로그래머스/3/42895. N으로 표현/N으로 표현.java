import java.util.*;

class Solution {
    
    public int solution(int N, int number) {
        if (N == number) {
            return 1;
        }

        List<Set<Integer>> dp = new ArrayList<>();
        for (int i = 0; i <= 8; i++) {
            dp.add(new HashSet<>());
        }

        for (int i = 1; i <= 8; i++) {
            Set<Integer> target = dp.get(i);
            target.add(Integer.parseInt(String.valueOf(N).repeat(i)));

            for (int j = 1; j < i; j++) {
                for (int k : dp.get(j)) {
                    for (int l : dp.get(i - j)) {
                        target.add(k + l);
                        if (k - l > 0) {
                            target.add(k - l);
                        }
                        if (k * l <= number) {
                            target.add(k * l);
                        }
                        if (k != 0 && l != 0) {
                            target.add(k / l);
                        }
                    }
                }
            }

            if (target.contains(number)) {
                return i;
            }
        }

        return -1;
    }
}