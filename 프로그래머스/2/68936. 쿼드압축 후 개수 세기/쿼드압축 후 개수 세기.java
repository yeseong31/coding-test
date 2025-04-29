class Solution {
    private void separate(int[][] arr, int x, int y, int n, int[] answer) {
        int value = arr[x][y];
        int k = n / 2;
        
        for (int i = x; i < x + n; i++) {
            for (int j = y; j < y + n; j++) {
                if (arr[i][j] != value) {
                    separate(arr, x, y, k, answer);
                    separate(arr, x, y + k, k, answer);
                    separate(arr, x + k, y, k, answer);
                    separate(arr, x + k, y + k, k, answer);
                    return;
                }
            }
        }
        
        answer[value]++;
    }
    
    public int[] solution(int[][] arr) {
        int[] answer = {0, 0};
        separate(arr, 0, 0, arr.length, answer);
        return answer;
    }
}