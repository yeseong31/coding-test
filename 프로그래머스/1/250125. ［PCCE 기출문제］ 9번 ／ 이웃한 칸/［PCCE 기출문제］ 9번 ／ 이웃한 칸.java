class Solution {
    public int solution(String[][] board, int h, int w) {
        int count = 0;
        int n = board.length;
        int m = board[0].length;
        String color = board[h][w];

        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int[] d : directions) {
            int nh = h + d[0];
            int nw = w + d[1];

            if (isValid(nh, nw, n, m) && board[nh][nw].equals(color)) {
                count++;
            }
        }

        return count;
    }

    private boolean isValid(int h, int w, int n, int m) {
        return h >= 0 && h < n && w >= 0 && w < m;
    }
}