import java.util.ArrayList;
import java.util.List;

class Solution {
    private void hanoi(int start, int mid, int end, int n, List<int[]> answer) {
        if (n == 1) {
            answer.add(new int[] {start, end});
            return;
        }
        
        hanoi(start, end, mid, n - 1, answer);
        hanoi(start, mid, end, 1, answer);
        hanoi(mid, start, end, n - 1, answer);
    }
    
    public int[][] solution(int n) {
        List<int[]> answer = new ArrayList<>();
        hanoi(1, 2 ,3, n, answer);
        return answer.toArray(new int[0][]);
    }
}