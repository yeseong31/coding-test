import java.util.ArrayList;
import java.util.List;


class Solution {
    public int[][] solution(int n) {
        List<int[]> result = new ArrayList<>();
        hanoi(n, 1, 2, 3, result);
        return result.toArray(new int[0][]);
    }
    
    private void hanoi(final int n, final int start, final int mid, final int end, final List<int[]> result) {
        if (n == 1) {
            result.add(new int[] {start, end});
            return;
        }
        
        hanoi(n - 1, start, end, mid, result);
        hanoi(1, start, mid, end, result);
        hanoi(n - 1, mid, start, end, result);
    }
}
