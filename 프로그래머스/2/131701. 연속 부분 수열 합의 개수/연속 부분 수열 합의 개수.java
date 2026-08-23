import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int[] elements) {
        Set<Integer> sums = new HashSet<>();
        int n = elements.length;

        for (int start = 0; start < n; start++) {
            int sum = 0;

            for (int length = 0; length < n; length++) {
                sum += elements[(start + length) % n];
                sums.add(sum);
            }
        }

        return sums.size();
    }
}