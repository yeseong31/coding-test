class Solution {
    public int solution(int[][] board) {
        int answer = 0;

        int row = board.length;
        int col = board[0].length;
        int n = Math.max(row, col);

        int[][] dp = new int[n + 1][n + 1];

        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= col; j++) {
                if (board[i - 1][j - 1] != 0) {
                    dp[i][j] = Math.min(
                        Math.min(dp[i][j - 1], dp[i - 1][j]),
                        dp[i - 1][j - 1]
                    );
                    answer = Math.max(answer, ++dp[i][j]);
                }
            }
        }

        return answer * answer;
    }
}