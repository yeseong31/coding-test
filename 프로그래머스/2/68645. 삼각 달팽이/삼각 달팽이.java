class Solution {
    
    private static final int[] dx = {1, 0, -1};
    private static final int[] dy = {0, 1, -1};
    
    public int[] solution(int n) {
        int[][] triangle = new int[n][n];
        
        int x = -1;
        int y = 0;
        int d = 0;
        int v = 1;
        
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                d = i % 3;
                x += dx[d];
                y += dy[d];
                triangle[x][y] = v++;
            }
        }
        
        int[] answer = new int[v - 1];
        int index = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                answer[index++] = triangle[i][j];
            }
        }
        
        return answer;
    }
}