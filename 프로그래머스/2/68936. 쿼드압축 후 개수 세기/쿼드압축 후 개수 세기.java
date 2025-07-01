class Solution {
    private void compress(int[][] arr, int x, int y, int n, int[] answer) {
        int v = arr[x][y];
        int k = n / 2;
        
        for (int i = x; i < x + n; i++) {
            for (int j = y; j < y + n; j++) {
                if (arr[i][j] != v) {
                    compress(arr, x, y, k, answer);
                    compress(arr, x, y + k, k, answer);
                    compress(arr, x + k, y, k, answer);
                    compress(arr, x + k, y + k, k, answer);
                    return;
                }
            }
        }
        
        ++answer[v];
    }
    
    public int[] solution(int[][] arr) {
        int[] answer = {0, 0};
        compress(arr, 0, 0, arr.length, answer);
        return answer;
    }
}