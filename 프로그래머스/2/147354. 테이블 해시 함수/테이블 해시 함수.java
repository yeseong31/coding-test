import java.util.Arrays;

class Solution {
    
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        Arrays.sort(data, (a, b) -> {
            if (a[col - 1] == b[col - 1]) {
                return b[0] - a[0];
            }
            return a[col - 1] - b[col - 1];
        });

        int answer = -1;

        for (int row = row_begin; row <= row_end; row++) {
            int rowSum = 0;
            for (int value : data[row - 1]) {
                rowSum += value % row;
            }

            int target = rowSum;
            answer = (answer == -1) ? target : answer ^ target;
        }

        return answer;
    }
}